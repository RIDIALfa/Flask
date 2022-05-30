from flask import Blueprint

from controllers.consommation_api import test


consommation = Blueprint('cons', __name__) 

consommation.route('/test')(test)
