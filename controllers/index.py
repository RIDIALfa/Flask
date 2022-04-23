from flask import render_template, request
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from flask_googlemaps import Map

import json

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
    json_data = {
        'user' : {
            'x' : 37.50611,
            'y' : 127.0616346
        }
    }
    user_location = (json_data['user']['x'], json_data['user']['y'])
    circle = { 
        'stroke_color': '#0000FF',
        'stroke_opacity': .5,
        'stroke_weight': 5,
        'fill_color': '#FFFFFF', 
        'fill_opacity': .2,
        'center': {
            'lat': user_location[0],
            'lng': user_location[1]
        }, 
        'radius': 500 
    }
    map = Map(
        identifier = "map", 
        varname = "map",
        lat = user_location[0], 
        lng = user_location[1], 
        zoom = 15,

        circles = [circle]
    )

    return render_template('pages/information.html', map=map)






