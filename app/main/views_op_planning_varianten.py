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
from ..Calculation_x import CalculateAngles

# variante 1: https://stackoverflow.com/questions/23712986/pre-populate-a-wtforms-in-flask-with-data-from-a-sqlalchemy-object
# answeredMay17'14 at 18:34EricWorkman

@main.route('/op_planning', methods=['GET', 'POST'])
def op_planning():
    coronal_component_C = 13.2
    sagittal_component_S = -10.5
    torsion_component_T = 22
    form = OpPlanningForm()
    form_action = url_for('.op_planning')
    if request.method == 'GET':
        form.coronal_component_C = coronal_component_C
        form.sagittal_component_S = sagittal_component_S
        form.torsion_component_T = torsion_component_T
    if form.validate_on_submit():
        session['coronal_component_C'] = form.coronal_component_C.data
        session['sagittal_component_S'] = form.sagittal_component_S.data
        session['torsion_component_T'] = form.torsion_component_T.data
        # return redirect(url_for('.op_planning_results', **request.args))
        return redirect(url_for('.op_planning_results', coronal_component_C=coronal_component_C,
                                sagittal_component_S=session.get(sagittal_component_S),
                                torsion_component_T=session.get(torsion_component_T)))

    return render_template('op_planning.html', form=form, form_action=form_action,
                           coronal_component_C=coronal_component_C,
                           sagittal_component_S=session.get(sagittal_component_S),
                           torsion_component_T=session.get(torsion_component_T))


@main.route('/op_planning_results', methods=['GET', 'POST'])
def op_planning_results():
    coronal_component_C = request.form.get('coronal_component_C')
    sagittal_component_S = request.form.get('sagittal_component_S')
    torsion_component_T = request.form.get('torsion_component_T')
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
    return render_template('op_planning_results.html', coronal_component_C=coronal_component_C,
                           sagittal_component_S=sagittal_component_S,
                           torsion_component_T=torsion_component_T)
    # ,
    #                    sagittal_component_S=sagittal_component_S,
    #                    torsion_component_T=torsion_component_T)
