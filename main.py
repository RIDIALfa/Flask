from crypt import methods
from email import message
from flask import Flask ,render_template, request
from wtforms import Form, StringField, TextAreaField,validators

class PostForm(Form):
    title=StringField('title',[validators.length(max=100),validators.DataRequired()])
    message=TextAreaField('message')




app = Flask(__name__)


@app.route('/test',methods=['GET','POST'])
def teste():
    form=PostForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.title.data,form.message.data)
    else:
        print('error')

    return render_template('test.html',form=form)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/connexion')
def login():
    return render_template('pages/connexion.html')

@app.route('/compte')
def compte():
    return render_template('pages/comptes/information.html')

@app.route('/posts')
def posts():
    return render_template('pages/comptes/posts.html')

@app.route('/post')
def post():
    return render_template('pages/comptes/post.html')

@app.route('/albums')
def albums():
    return render_template('pages/comptes/albums.html')

@app.route('/album')
def album():
    return render_template('pages/comptes/album.html')

@app.route('/todos')
def todos():
    return render_template('pages/comptes/todos.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)