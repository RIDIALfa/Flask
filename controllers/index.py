from hashlib import new
from flask import flash, redirect, render_template, request, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from models.creates_tables import Posts, Todos, Comments, Albums, Photos, db



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
    posts = Posts.query.filter_by(userId_post = 1).all()

    for post in posts:
        print(post)

    if request.method == 'POST' and form_post.validate():
        
        new_post = Posts(
            title_post = form_post.title.data, 
            body_post = form_post.message.data, 
            userId_post = 1
        )

        print(new_post)
        print("Information de l'article : ",new_post.title_post, new_post.body_post)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('.posts'))
    
    return render_template('pages/posts.html', formPost = form_post, posts=posts)





# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post(post_title):
    form_comment = CommentForm(request.form)
    post = Posts.query.filter_by(title_post=post_title).first()
    comments = Comments.query.filter_by(postId_comment = post.postId).all()

    # print(posts)

    if request.method == 'POST' and form_comment.validate():
            
        new_comment = Comments(
            name_comment = form_comment.title.data, 
            body_comment = form_comment.message.data,
            email_comment = 'alpha@sa.sn',
            postId_comment = post.postId
        )

        print(new_comment)
        db.session.add(new_comment)
        db.session.commit()

        return redirect('/posts/'+post_title)

    return render_template('pages/post.html', formComment = form_comment, post = post,comments = comments)





# CONTROLLER DE LA PAGE DES ALBUMS
def albums():
    form_album = ALbumForm(request.form)
    albums = Albums.query.all()

    if request.method == 'POST' and form_album.validate():
            
        new_album = Albums(
            title_album = form_album.title.data, 
            userId_album = 1
        )
        db.session.add(new_album)
        db.session.commit()

        return redirect('/albums')
    
    return render_template('pages/albums.html', formAlbum = form_album, albums=albums)






# CONTROLLER DE LA PAGE DETAIL D'UN ALBUM
def album(album_name):
    form_photo = PhotoForm(request.form)
    
    albumId = Albums.query.filter_by(title_album=album_name).first().albumId

    if request.method == 'POST' and form_photo.validate():
        
        new_photo = Photos(
            title_photo = form_photo.title.data,
            url_photo = form_photo.url.data,
            thumnail_photo = form_photo.thumbnail.data,
            albumId_photo = albumId
        )

        db.session.add(new_photo)
        db.session.commit()

        return redirect('/albums/'+album_name)

    if request.method == "GET":
        photos = Photos.query.filter_by(albumId_photo = albumId).all()

        return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos)







# CONTROLLER DE LA PAGE DES TODOS
def todos():
    form_todo = TodoForm(request.form)
    todos = Todos.query.all()

    if request.method == 'POST' and form_todo.validate():
            
        new_todo = Todos(
            title_todo = form_todo.title.data,
            etat_todo = form_todo.etat.data,
            userId_todo = 1
        )

        print(new_todo)
        print(new_todo.title_todo, new_todo.etat_todo)
        db.session.add(new_todo)
        db.session.commit()

        return redirect('/todos')

    return render_template('pages/todos.html', formTodo = form_todo, todos=todos )





# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    return render_template('pages/information.html')




