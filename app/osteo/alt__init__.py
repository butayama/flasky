from flask import Blueprint

osteo = Blueprint('osteo', __name__)

from . import views
