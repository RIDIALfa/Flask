from flask import Flask ,render_template, request,Blueprint
from wtforms import Form, StringField, TextAreaField,validators
from forms import PostForm, CommentForm, TodoForm, ALbumForm, PhotoForm, UserForm



user_route=Blueprint('user_route',__name__)


user_route.route('/forms',methods=['GET','POST'])
def teste():
    form = PostForm(request.form)
    formComment = CommentForm(request.form)
    formTodo = TodoForm(request.form)
    formAlbum = ALbumForm(request.form)
    formPhoto = PhotoForm(request.form)
    # formUser = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.title.data,form.message.data)
    else:
        print('error')

    return render_template('forms.html', form=form, formComment=formComment, 
        formTodo=formTodo, formAlbum=formAlbum, 
        formPhoto=formPhoto
        )

user_route.route('/connexion/')
def login():
    return render_template('pages/connexion.html')

user_route.route('compte/')
def compte():
    return render_template('pages/comptes/information.html')

user_route.route('/posts/')
def posts():
    formPost = PostForm(request.form)
    return render_template('pages/comptes/posts.html', formPost = formPost)

user_route.route('/post/')
def post():
    return render_template('pages/comptes/post.html')

user_route.route('/albums/')
def albums():
    return render_template('pages/comptes/albums.html')

user_route.route('/album/')
def album():
    return render_template('pages/comptes/album.html')

user_route.route('/todos/')
def todos():
    return render_template('pages/comptes/todos.html')

