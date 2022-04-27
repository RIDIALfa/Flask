from flask import redirect, render_template, request, session, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from models.create_tables import Adresses, Compagny, Users, Posts, Comments, Albums, Photos, Todos, db

# Fake datas
users =[
    {'email': 'awa@sa.sn', 'password':'passer789', 'fullname':'awa diop', 'phone': 330000000, 'lat': 34.05855065769437, 'long' : -118.25096592088265},
    {'email': 'alpha@sa.sn', 'password':'passer123', 'fullname':'alpha diallo', 'phone': 440000000, 'lat': 14.872029, 'long' : -17.436139},
    {'email': 'khabane@sa.sn', 'password':'passer456', 'fullname':'khabane fall', 'phone': 550000000, 'lat': 16.7727, 'long' : -19.361339},
]



# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)

    if request.method == 'POST':

        check_compagny_value = Compagny.query.filter_by(name_compagny = form_user.compagny.data).first()
        check_adresse_value = Adresses.query.filter_by(suite = form_user.suite.data).first()

        if(check_compagny_value != None):
            id_compagny = check_compagny_value.id_compagny
        
        else:
            new_compagny = Compagny(
                name_compagny = form_user.compagny.data,
                catchPhrase = form_user.catch.data,
                bs = form_user.bs.data
            )
            db.session.add(new_compagny)
            db.session.commit()

            id_compagny = Compagny.query.filter_by(name_compagny = form_user.compagny.data).first().id_compagny


        if (check_adresse_value != None):
            id_adresse = check_adresse_value.id_adresse

        else:
            new_adresse = Adresses(
                city = form_user.ville.data,
                street = form_user.rue.data,
                suite = form_user.suite.data,
                zipcode = form_user.zipcode.data,
                lat = form_user.lat.data,
                long = form_user.long.data,
            )
            db.session.add(new_adresse)
            db.session.commit()

            id_adresse = Adresses.query.filter_by(suite = form_user.suite.data).first().id_adresse


        new_user = Users(
            fullname = form_user.fullname.data,
            username = form_user.username.data,
            email = form_user.email.data,
            phone = form_user.phone.data,
            website = form_user.website.data,
            password = "passer",
            id_adresse_users = id_adresse,
            id_company_users = id_compagny
        )
        db.session.add(new_user)
        db.session.commit()

    
        print(new_user)

        return redirect('/')
        
    return render_template('pages/home.html', formUser=form_user, users = users)





# CONTROLLER DE LA PAGE DE CONNEXION
def login(email):

    if request.method == 'POST':

        mail=request.form['email']
        passwd=request.form['password']

        for i in  users:
            if i['email']==mail and i['password']==passwd:
                session["email"] = mail
                return redirect('/compte')
            
        msg = "Email ou mot de passe incorrect !"
        return render_template("pages/connexion.html", msg=msg)
        

    return render_template('pages/connexion.html',email=email)
    






# CONTROLLER DE LA PAGE DES POSTS
def posts():
    form_post = PostForm(request.form)
    
    posts = Posts.query.filter_by(id_users_posts = 1).all()

    if "email" in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

        if request.method == 'POST' and form_post.validate():
            
            new_post = Posts(
                title_posts = form_post.title.data, 
                body_posts = form_post.message.data, 
                id_users_posts = 1
            )

            db.session.add(new_post)
            db.session.commit()

            return redirect('/posts')

        return render_template('pages/posts.html', formPost = form_post, posts=posts,user=user)
    else:

        return redirect('/connexion')







# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post(post_title):
    form_comment = CommentForm(request.form)
    post = Posts.query.filter_by(title_posts = post_title).first()

    if post == None:
            return redirect('/posts')

    comments = Comments.query.filter_by(id_posts_comments = post.id_posts).all()

    if "email" in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

        if request.method == 'POST' and form_comment.validate():
            
            new_comment = Comments(
                name_comments = form_comment.title.data, 
                body_comments = form_comment.message.data,
                email_comments = session['email'],
                id_posts_comments = post.id_posts
            )

            db.session.add(new_comment)
            db.session.commit()

            return redirect('/posts/'+post_title)

        return render_template('pages/post.html', formComment = form_comment, post = post,comments = comments,user=user)

    else:
        return redirect('/connexion')







# CONTROLLER DE LA PAGE DES ALBUMS
def albums():
    form_album = ALbumForm(request.form)
    albums = Albums.query.all()

    if "email"  in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

        if request.method == 'POST' and form_album.validate():
            
            new_album = Albums(
                title_albums = form_album.title.data, 
                id_users_albums = 1
            )
            
            db.session.add(new_album)
            db.session.commit()

            return redirect('/albums')
        
        return render_template('pages/albums.html', formAlbum = form_album, albums=albums,user=user)

    else:
        return redirect('/connexion')








# CONTROLLER DE LA PAGE DETAIL D'UN ALBUM
def album(album_name):
    form_photo = PhotoForm(request.form)
    album = Albums.query.filter_by(title_albums = album_name).first()

    if album == None:
        return redirect('/albums')
        
    photos = Photos.query.filter_by(id_albums_photos = album.id_albums).all()
    
    if  "email"  in session:
        for i in users:
             if i['email']==session['email']:
                 user = i
    
        if request.method == 'POST' and form_photo.validate():
            
            new_photo = Photos(
                title_photos = form_photo.title.data,
                url = form_photo.url.data,
                thambnailUrl = form_photo.thumbnail.data,
                id_albums_photos = album.id_albums
            )

            db.session.add(new_photo)
            db.session.commit()

            return redirect('/albums/'+album_name)

        return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos,user=user)
    else:
        return redirect('/connexion')

    return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos, albumId = albumId )






# CONTROLLER DE LA PAGE DES TODOS
def todos():
    form_todo = TodoForm(request.form)
    todos = Todos.query.all()

    if  "email"  in session:
        for i in users:
             if i['email']==session['email']:
                 user = i
        if request.method == 'POST' and form_todo.validate():
                
            new_todo = Todos(
                title_todos = form_todo.title.data,
                status = form_todo.etat.data,
                id_users_todos = 1
            )

            db.session.add(new_todo)
            db.session.commit()

            return redirect('/todos')

        return render_template('pages/todos.html', formTodo = form_todo, todos=todos ,user=user)
        
    else:
        return redirect('/connexion')









# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    user = {}
    if "email" in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

        return render_template('pages/information.html', user=user)

    else:
        return redirect('/connexion')


# fonction supprimer post

def delete_post(indice_post):
    p=Posts.query.get(indice_post)
    db.session.delete(p)
    db.session.commit()
    return redirect('/posts')
    
def delete_album(indice_album):
    p=Albums.query.get(indice_album)
    db.session.delete(p)
    db.session.commit()
    return redirect('/albums')



# CONTROLLER logout
def logout():
    session.clear()
    return redirect(url_for('.login'))







