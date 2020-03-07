import flask
from . import osteo
from app.infrastructure.view_modifiers import response
import app.services.angles_service as angles_service

# osteo = flask.osteo('home', __name__, template_folder='templates')


@osteo.route('/')
@response(template_file='home/index.html')
def index():
    return {}


@osteo.route('/about')
@response(template_file='home/about.html')
def about():
    return {}


@osteo.route('/about_01')
@response(template_file='home/about_01.html')
def about_01():
    return {}


@osteo.route('/case')
@response(template_file='home/case.html')
def case():
    return {}


@osteo.route('/index_01')
@response(template_file='home/index_01.html')
def index_01():
    return {}


@osteo.route('/op')
@response(template_file='home/op.html')
def op():
    return {}


@osteo.route('/op_planning')
@response(template_file='home/op_planning.html')
def op_planning():
    test_angles = angles_service.get_angles()
    return {'angles': test_angles}


@osteo.route('/post_op')
@response(template_file='home/post_op.html')
def post_op():
    return {}


@osteo.route('/post_op1')
@response(template_file='home/post_op1.html')
def post_op1():
    return {}


@osteo.route('/details')
@response(template_file='home/details.html')
def details():
    return {}


@osteo.route('/details_01')
@response(template_file='home/details_01.html')
def details_01():
    return {}
