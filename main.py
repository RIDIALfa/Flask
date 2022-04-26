from flask import Flask, render_template
from routes.index import routers
from flask_sqlalchemy import SQLAlchemy
# from models.create_tables import *




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



#Pour gerer les routes
app.register_blueprint(routers)


#Pour la page 404
@app.errorhandler(404)
def not_found(error):
    return render_template('pages/not_found.html'),404



if __name__=='__main__':
    app.run(debug=True,port=5000)