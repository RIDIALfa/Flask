from flask import render_template, request
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm


# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)
    return render_template('pages/home.html', formUser=form_user)



# CONTROLLER DE LA PAGE DE CONNEXION
users =[
    {'email': 'alpha@sa.sn', 'password':'passer123'},
    {'email': 'khabane@sa.sn', 'password':'passer456'},
    {'email': 'awa@sa.sn', 'password':'passer789'},
]

def login(email):
    return render_template('pages/connexion.html',email=email)
    





# CONTROLLER DE LA PAGE DES POSTS
def posts():
    form_post = PostForm(request.form)
    return render_template('pages/posts.html', formPost = form_post)





# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post():
    form_comment = CommentForm(request.form)
    return render_template('pages/post.html', formComment = form_comment)





# CONTROLLER DE LA PAGE DES ALBUMS
def albums():
    form_album = ALbumForm(request.form)
    return render_template('pages/albums.html', formAlbum = form_album)






# CONTROLLER DE LA PAGE DETAIL D'UN ALBUM
def album():
    form_photo = PhotoForm(request.form)
    return render_template('pages/album.html', formPhoto = form_photo)







# CONTROLLER DE LA PAGE DES TODOS
def todos():
    form_todo = TodoForm(request.form)
    return render_template('pages/todos.html', formTodo = form_todo)





# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    return render_template('pages/information.html')






