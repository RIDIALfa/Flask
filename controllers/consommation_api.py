from ast import And
from flask import Flask ,jsonify , request , make_response, render_template 
import jwt
import datetime
from models.create_tables import Adresses, Albums, Comments, Compagny, Photos, Posts, Todos, Users, Utilisateur, db
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing!'}),403
        try:
            data=jwt.decode(token,'groupe3')
        except:
            return jsonify({'message':'Token is invalid'}),403
        return f(*args,**kwargs)
    return decorated


def unprotected():
    return jsonify({'message':'Anyone can view this!'})

def protected():
    return jsonify({'message':'This is only available for people with valid tokens.'})


def login():
    # auth=request.authorization  
    # if auth and auth.password=='diop':
    if request.method == 'POST':
        mail=request.form['email']
        passwd=request.form['password']
        user = Utilisateur.query.filter_by(email=mail).first()
        print(user.email,user.password,user.profile, passwd)

        if user:
            if  user.password == passwd:
              token=jwt.encode({'email':user.email,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=50)},'groupe3')
              return jsonify({'token':token})
            else:
                msg="Email ou mot de passe incorrect !"
                return render_template('consommation/connexion.html',msg=msg)


        # mail = None
        # utilisateur = Utilisateur.query.all()
        # if request.method == 'POST':
        #      mail=request.email
        #      passwd=request.password
        # for user in utilisateur:
        #      if user.email == mail and user.password == passwd:
        #         return ''
        
        # return make_response('coule not verify!',401,{'www-Authenticate':'Basic realm="Login Required'})
    
                
               
    return render_template('consommation/connexion.html')




