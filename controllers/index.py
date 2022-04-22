from flask import render_template, request
from models.forms import UserForm, PostForm


# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)
    return render_template('pages/home.html', formUser=form_user)



# CONTROLLER DE LA PAGE DE CONNEXION
def login():
    return render_template('pages/connexion.html')
    





# CONTROLLER DE LA PAGE DES POSTS
def posts():
    form_post = PostForm(request.form)
    return render_template('pages/posts.html', formPost = form_post)





# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post():
    return render_template('pages/post.html')





# CONTROLLER DE LA PAGE DES ALBUMS
def albums():
    return render_template('pages/albums.html')






# CONTROLLER DE LA PAGE DETAIL D'UN ALBUM
def album():
    return render_template('pages/album.html')







# CONTROLLER DE LA PAGE DES TODOS
def todos():
    return render_template('pages/todos.html')





# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    return render_template('pages/information.html')






