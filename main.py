from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/test')
def teste():
    return render_template('test.html')

@app.route('/connexion')
def login():
    return render_template('pages/connexion.html')

@app.route('/compte')
def compte():
    return render_template('pages/compte.html')


@app.route('/user')
def account():
    return render_template('pages/comptes/userInfo.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)