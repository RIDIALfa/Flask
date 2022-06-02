from crypt import methods
from flask import Blueprint

from controllers.consommation_api import home, login, protected, todos, unprotected


consommation = Blueprint('cons', __name__) 

consommation.route('/login',methods=['GET','POST'])(login)

consommation.route('/unprotected')(unprotected)
consommation.route('/protected')(protected)

