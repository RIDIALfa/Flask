from flask import Flask, render_template
from routes.index import routers



app = Flask(__name__)


#Pour gerer les routes
app.register_blueprint(routers)




#Pour la page 404
@app.errorhandler(404)
def not_found(error):
    return render_template('pages/not_found.html'),404



if __name__=='__main__':
    app.run(debug=True,port=5000)