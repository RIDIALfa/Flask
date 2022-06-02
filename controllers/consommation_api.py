from flask import   redirect, render_template, request
from models.create_tables import Adresses, Albums, Comments, Compagny, Photos, Posts, Todos, Users, Utilisateur, db

def login():
    utilisateur = Utilisateur.query.all()
    if request.method == 'POST':
        mail=request.form['email']
        passwd=request.form['password']
        for user in utilisateur:
             if user.email == mail and user.password == passwd:
                 return redirect('/')
        
        return render_template("consommation/connexion.html")
    
                # print(request.form)
               
    return render_template('consommation/connexion.html')