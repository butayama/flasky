import flask

from ..infrastructure.view_modifiers import response
import app.services.angles_service as angles_service

blueprint = flask.Blueprint('..templates/home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='..templates/home/index.html')
def index():
    return {}


@blueprint.route('/about')
@response(template_file='..templates/home/about.html')
def about():
    return {}


@blueprint.route('/about_01')
@response(template_file='..templates/home/about_01.html')
def about_01():
    return {}


@blueprint.route('/case')
@response(template_file='..templates/home/case.html')
def case():
    return {}


@blueprint.route('/index_01')
@response(template_file='home/index_01.html')
def index_01():
    return {}


@blueprint.route('/op')
@response(template_file='home/op.html')
def op():
    return {}


@blueprint.route('/op_planning')
@response(template_file='home/op_planning.html')
def op_planning():
    test_angles = angles_service.get_angles()
    return {'angles': test_angles}


@blueprint.route('/post_op')
@response(template_file='home/post_op.html')
def post_op():
    return {}


@blueprint.route('/details')
@response(template_file='home/details.html')
def details():
    return {}


@blueprint.route('/details_01')
@response(template_file='home/details_01.html')
def details_01():
    return {}
