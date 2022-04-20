from flask import Flask ,render_template
from wtforms import Form, StringField, validators


app = Flask(__name__)


@app.route('/test')
def teste():
    return render_template('test.html')
class postForm(Form):
    title=StringField('title',[])
@app.route('/')
def home():
    return render_template('pages/home.html')















@app.route('/connexion')
def login():
    return render_template('pages/connexion.html')

@app.route('/compte')
def compte():
    return render_template('pages/compte.html')
if __name__=='__main__':
    app.run(debug=True,port=5000)