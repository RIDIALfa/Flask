from flask import Flask, render_template
from routes.index import routers
from routes.api import apis
from routes.visualisation import visualisations
from flask_sqlalchemy import SQLAlchemy
from models.create_tables import create_all_tables

app = Flask(__name__)
app.config['SECRET_KEY'] = 'groupe3'


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)


#Pour gerer les routes
app.register_blueprint(routers)
app.register_blueprint(apis)
app.register_blueprint(visualisations)


#Pour la page 404
@app.errorhandler(404)
def not_found(error):
    return render_template('pages/not_found.html'),404



if __name__=='__main__':
    create_all_tables()
    app.run(debug=True,port=5000)