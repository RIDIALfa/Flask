from crypt import methods
from flask import Blueprint

from controllers.consommation_api import login


consommation = Blueprint('cons', __name__) 

consommation.route('/login', methods=['GET','POST'])(login)
