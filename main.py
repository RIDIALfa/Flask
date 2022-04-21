from flask import Flask ,render_template, request
from wtforms import Form, StringField, TextAreaField,validators
from forms import PostForm, CommentForm, TodoForm, ALbumForm, PhotoForm, UserForm




app = Flask(__name__)


@app.route('/forms',methods=['GET','POST'])
def teste():
    form = PostForm(request.form)
    formComment = CommentForm(request.form)
    formTodo = TodoForm(request.form)
    formAlbum = ALbumForm(request.form)
    formPhoto = PhotoForm(request.form)
    formUser = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.title.data,form.message.data)
    else:
        print('error')

    return render_template('forms.html', form=form, formComment=formComment, 
        formTodo=formTodo, formAlbum=formAlbum, 
        formPhoto=formPhoto, formUser=formUser
        )

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