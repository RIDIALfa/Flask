from flask import  render_template, request
from models.create_tables import Adresses, Albums, Comments, Compagny, Photos, Posts, Todos, Users, db

def test():
    return render_template('consommation/test.html')