from flask import render_template, redirect, url_for, abort, flash, request, \
    current_app, make_response, session
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, PostForm, \
    CommentForm, OpPlanningForm
from .. import db
from ..auth.forms import LoginForm
from ..models import Permission, Role, User, Post, Comment
from ..decorators import admin_required, permission_required
from ..Calculation import CalculateAngles as ca
import os

@main.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['FLASKY_SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if current_user.can(Permission.WRITE) and form.validate_on_submit():
        post = Post(body=form.body.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('index.html', form=form)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    return render_template('user.html', user=user, posts=posts,
                           pagination=pagination)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
                          post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been published.')
        return redirect(url_for('.post', id=post.id, page=-1))
    page = request.args.get('page', 1, type=int)
    if page == -1:
        page = (post.comments.count() - 1) // \
               current_app.config['FLASKY_COMMENTS_PER_PAGE'] + 1
    pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
        page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('post.html', posts=[post], form=form,
                           comments=comments, pagination=pagination)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and \
            not current_user.can(Permission.ADMIN):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    form.body.data = post.body
    return render_template('edit_post.html', form=form)


@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if current_user.is_following(user):
        flash('You are already following this user.')
        return redirect(url_for('.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are now following %s.' % username)
    return redirect(url_for('.user', username=username))


@main.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if not current_user.is_following(user):
        flash('You are not following this user.')
        return redirect(url_for('.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following %s anymore.' % username)
    return redirect(url_for('.user', username=username))


@main.route('/followers/<username>')
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followers.paginate(
        page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'],
        error_out=False)
    follows = [{'user': item.follower, 'timestamp': item.timestamp}
               for item in pagination.items]
    return render_template('followers.html', user=user, title="Followers of",
                           endpoint='.followers', pagination=pagination,
                           follows=follows)


@main.route('/followed_by/<username>')
def followed_by(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followed.paginate(
        page, per_page=current_app.config['FLASKY_FOLLOWERS_PER_PAGE'],
        error_out=False)
    follows = [{'user': item.followed, 'timestamp': item.timestamp}
               for item in pagination.items]
    return render_template('followers.html', user=user, title="Followed by",
                           endpoint='.followed_by', pagination=pagination,
                           follows=follows)


@main.route('/all')
@login_required
def show_all():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '', max_age=30 * 24 * 60 * 60)
    return resp


@main.route('/followed')
@login_required
def show_followed():
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed', '1', max_age=30 * 24 * 60 * 60)
    return resp


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def moderate():
    page = request.args.get('page', 1, type=int)
    pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_COMMENTS_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('moderate.html', comments=comments,
                           pagination=pagination, page=page)


@main.route('/moderate/enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE)
def moderate_enable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.moderate',
                            page=request.args.get('page', 1, type=int)))


@main.route('/moderate/disable/<int:id>')
@login_required
@permission_required(Permission.MODERATE)
def moderate_disable(id):
    comment = Comment.query.get_or_404(id)
    comment.disabled = True
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('.moderate',
                            page=request.args.get('page', 1, type=int)))


@main.route('/op_planning', methods=['GET', 'POST'])
def op_planning():
    if os.environ['FLASK_DEBUG']:
        coronal_component_C = 13.3
        sagittal_component_S = -10.5
        torsion_component_T = 22
    else:
        coronal_component_C = None
        sagittal_component_S = None
        torsion_component_T = None
    values = {}
    form = OpPlanningForm()
    if request.method == 'GET':
        form.coronal_component_C.data = coronal_component_C
        form.sagittal_component_S.data = sagittal_component_S
        form.torsion_component_T.data = torsion_component_T
        # form.filename.data = f"osteotomy_result_{coronal_component_C}" + "_" + f"{sagittal_component_S}" + "_" + \
        #                      f"{torsion_component_T}" + ".txt"
    if form.validate_on_submit():
        filename, c_a_d, s_a_d, t_a_d, c_a, s_a, t_a, a_tad, a_oa, a_azi, a_ele, a_aor = \
            ca.calculate(form.coronal_component_C.data,
                         form.sagittal_component_S.data,
                         form.torsion_component_T.data)
        session['values'] = {
            "coronal_component_C": c_a_d,
            "sagittal_component_S": s_a_d,
            "torsion_component_T": t_a_d,
            "coronal_component_C_radians": c_a,
            "sagittal_component_S_radians": s_a,
            "torsion_component_T_radians": t_a,
            "true_angular_deformity": a_tad
            "orientation_angle": a_oa
            "azimuth_of_vektor_k"
            ""
            ""

                A = {degrees(a_tad): 6.1f}
        degrees({a_tad: 7.4f}
        rad )

        (16)
        {chr(945)} = {degrees(a_oa): 6.1f}
        degrees({a_oa: 7.4f}
        rad )

      (angle
        between
        z1
        axis and the
        axis
        of
        rotation
        of
        vector
        k ) (13)
        {chr(int("3A6", 16))} = {degrees(a_azi): 6.1f}
        degrees({a_azi: 7.4f}
        rad )

        angle
        of
        rotation
        between
        x1
        axis and the
        projection
        of
        k
        onto
        the
        x1 - y1
        plane(12)
        {chr(int("398", 16))} = {degrees(a_ele): 6.1f}
        degrees({a_ele: 7.4f}
        rad )

        angle
        of
        rotation
        around
        k(14)
        {chr(int("3B2", 16))} = {degrees(a_aor): 6.1f}
        degrees({a_aor: 7.4f}
        rad )

        }
        result = request.form
        return redirect(url_for('.op_planning_results', result=result, values=session['values']))

    return render_template('op_planning.html', form=form)
    # return render_template('op_planning.html', form=form,
    #                        coronal_component_C=coronal_component_C,
    #                        sagittal_component_S=session.get(sagittal_component_S),
    #                        torsion_component_T=session.get(torsion_component_T))


@main.route('/op_planning_results', methods=['GET', 'POST'])
def op_planning_results():
    result = request.args
    # coronal_component_C = request.form.get('coronal_component_C')
    # sagittal_component_S = request.form.get('sagittal_component_S')
    # torsion_component_T = request.form.get('torsion_component_T')
    # angles = request.form.getlist('coronal_component_C', 'sagittal_component_S', 'torsion_component_T')
    # coronal_component_C  = request.args
    # coronal_component_C, sagittal_component_S, torsion_component_T  = request.args
    # coronal_component_C = request.args['coronal_component_C',
    #                                    'sagittal_component_S',
    #                                    'torsion_component_T']
    # coronal_component_C, sagittal_component_S, torsion_component_T = request.args['coronal_component_C',
    #                                                                               'sagittal_component_S',
    #                                                                               'torsion_component_T']
    # coronal_component_C = request.args['coronal_component_C']
    # sagittal_component_S = request.args['sagittal_component_S']
    # torsion_component_T = request.args['torsion_component_T']
    calc_angles = CalculateAngles
    return render_template('op_planning_results.html', result=result, values=session['values'])
    # return render_template('op_planning_results.html', coronal_component_C=coronal_component_C,
    #                        sagittal_component_S=sagittal_component_S,
    #                        torsion_component_T=torsion_component_T)
    # ,
    #                    sagittal_component_S=sagittal_component_S,
    #                    torsion_component_T=torsion_component_T)

# def get_galaxies():
#     galaxies = ["Messier 81", "StarBurst", "Black Eye", "Cosmos Redshift", "Sombrero", "Hoags Object", "Andromeda",
#                 "Pinwheel", "Cartwheel",
#                 "Mayall's Object", "Milky Way", "IC 1101", "Messier 87", "Ring Nebular", "Centarus A", "Whirlpool",
#                 "Canis Major Overdensity", "Virgo Stellar Stream"]

# Erstelle ein Formular mit Flask. Baue ein Formular ein, in dem Du einen Strassennamen in ein Eingabefeld eingibst und über einen Knopf das Formular abschickst. Der HTML-Code sollte etwa folgendes enthalten:
#
# <form action="/suchen">
#   <input name="suchtext"></input>
#   <input type="submit" value="Strasse suchen"></input>
# </form>
#
# Die URL /suchen kann nun auf den Inhalt des Textfeldes mit dem Namen suchtext zugreifen:
#
# from flask import request
#
# # in der aufgerufenen Funktion
# text = request.args.get('suchtext')
