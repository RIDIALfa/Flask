from flask import jsonify , request
import jwt
import datetime
from models.create_tables import Utilisateur
from functools import wraps




def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        
        if not token:

            return jsonify({"message" : "Token is missing!"}),403
        
        
        try:
            
            jwt.decode(token,'groupe3', algorithms="HS256")
            
        except:

            print("Token dans le Required: ",token)
            return jsonify({"message" : "Token is invalid"}),403
        
        return f(*args,**kwargs)

    return decorated







def token_decoder():
    token = request.args.get('token')
        
    if not token:
        return jsonify({"message" : "Aucun token n'est chargé"}),403
        
    try:
            
        token_decode = jwt.decode(token,'groupe3', algorithms="HS256")

        return jsonify({
            "token_decode" : token_decode
        })
            
    except:
        return jsonify({"message" : "Le token est invalid"}),403





def login():

    email =  request.get_json().get('email')
    password =  request.get_json().get('password')

    user = Utilisateur.query.filter_by(email = email).first()

    if user:

        if user.password == password:

            # Ici on crée le token avec les informations(email, et profile)
            token = jwt.encode({
                'email' : user.email,
                'profile': user.profile,
                'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)
                }, 
                'groupe3', algorithm="HS256")


            return jsonify({
                'token': token
            })
        
        else:
            return jsonify({
                "message": "Email ou mot de passe incorrect !"
            })
    else:
        return jsonify({
            "message" : "Désolé il n'existe pas un utilisateur avec cette adresse email !"
        })




