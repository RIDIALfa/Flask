from flask import Blueprint


from controllers.consommation_api import login, token_decoder


consommation = Blueprint('cons', __name__) 


consommation.route('/login',methods=['GET','POST'])(login)

consommation.route('/decoder')(token_decoder)


