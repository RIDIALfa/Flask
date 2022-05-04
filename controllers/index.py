from tkinter import NONE
from turtle import pos
import requests
from flask import redirect, render_template, request, session, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from models.create_tables import Adresses, Compagny, Users, Posts, Comments, Albums, Photos, Todos, db




def getApi(param):

    url='https://jsonplaceholder.typicode.com/'

    reponse=requests.get(url+param)
    
    return reponse.json()
    



def add_adresse(city, street, suite, zipcode, lat, long):
    check_adresse_value = Adresses.query.filter_by(suite = suite).first()

    if(check_adresse_value != None):
        id_adresse = check_adresse_value.id_adresse
        
    else:

        new_adresse = Adresses(
            city = city,
            street = street,
            suite = suite,
            zipcode = zipcode,
            lat = lat,
            long = long
        )
            
        db.session.add(new_adresse)
        db.session.commit()

        id_adresse = Adresses.query.filter_by(suite = suite).first()

    return id_adresse




def add_compagny(name_compagny, catchPhrase, bs):
    check_compagny_value = Compagny.query.filter_by(name_compagny = name_compagny).first()

    if(check_compagny_value != None):
        id_compagny = check_compagny_value.id_compagny
            
    else:

        new_compagny = Compagny(
            name_compagny = name_compagny,
            catchPhrase = catchPhrase,
            bs = bs
        )

    
        db.session.add(new_compagny)
        db.session.commit()

        id_compagny = Compagny.query.filter_by(name_compagny = name_compagny).first()

    return id_compagny





def add_users_from_apis(users):
    
    
    for user in users:

        idAddr = add_adresse( user.get('address')['city'], user.get('address')['street'], user.get('address')['suite'], 
            user.get('address')['zipcode'], user.get('address')['geo']['lat'], user.get('address')['geo']['lng'])

        idComp = add_compagny( user.get('company')['name'], user.get('company')['catchPhrase'], user.get('company')['bs'])

        print("id :", idAddr, idComp)

        new_user = Users(
            fullname = user.get('name'),
            username = user.get('username'),
            email = user.get('email'),
            phone = user.get('phone').split('x')[0],
            website = user.get('website'),
            password = "passer",
            id_adresse_users = idAddr,
            id_company_users = idComp
        )
        print("Utilisateur ",new_user.fullname, new_user.email)



        db.session.add(new_user)
        db.session.commit()



# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)
    users = Users.query.all()

    print(users)

    for user in users:
        print(user.email)

    if request.method == 'POST':
        

        if request.form.get('nombre') :
            nombre =  request.form.get('nombre')

            users_api = getApi('users')[0:int(nombre)]
            
            add_users_from_apis(users_api)

            return redirect('/')

        else:
        

            idComp = add_compagny(form_user.compagny.data, form_user.catch.data, form_user.bs.data)

            idAddr = add_adresse( form_user.ville.data, form_user.rue.data, form_user.suite.data, 
            form_user.zipcode.data, form_user.lat.data, form_user.long.data)

            new_user = Users(
                fullname = form_user.fullname.data,
                username = form_user.username.data,
                email = form_user.email.data,
                phone = form_user.phone.data,
                website = form_user.website.data,
                password = "passer",
                origine = 0,
                id_adresse_users = idAddr,
                id_company_users = idComp
            )

            print(new_user.fullname, new_user.id_adresse_users, new_user.id_company_users)
            db.session.add(new_user)
            db.session.commit()

        
            print(new_user)

            return redirect('/')
        
    return render_template('pages/home.html', formUser=form_user, users = users )





# CONTROLLER DE LA PAGE DE CONNEXION
def login(email):

    if request.method == 'POST':
        users = Users.query.all()

        mail=request.form['email']
        passwd=request.form['password']

        for user in  users:
            if user.email == mail and user.password == passwd:
                session["email"] = mail
                return redirect('/compte')
            
        msg = "Email ou mot de passe incorrect !"
        return render_template("pages/connexion.html", msg=msg)
        

    return render_template('pages/connexion.html',email=email)
    



# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    if "email" in session:
        user = Users.query.filter_by(email = session['email']).first()
        adresse = Adresses.query.filter_by(id_adresse = user.id_adresse_users ).first()
        compagny = Compagny.query.filter_by(id_compagny = user.id_company_users ).first()

        return render_template('pages/information.html', user = user, compagny = compagny, adresse = adresse)

    else:
        return redirect('/connexion')







# CONTROLLER DE LA PAGE DES POSTS
def posts():
    form_post = PostForm(request.form)


    if "email" in session:
        user = Users.query.filter_by(email = session['email']).first()

        posts = Posts.query.filter_by(id_users_posts = user.id_users).all()

        page = request.args.get('page', 1, type=int)
        posts_paginate = Posts.query.filter_by(id_users_posts = user.id_users).paginate(page=page, per_page = 5)

        print(posts_paginate.pages, "Nombre totale de page")
        print(posts_paginate.page, "Page courant")
        print(posts_paginate.has_next, "Page suivant")

        if request.method == 'POST' and form_post.validate():
            
            new_post = Posts(
                title_posts = form_post.title.data, 
                body_posts = form_post.message.data, 
                id_users_posts = user.id_users
            )

            db.session.add(new_post)
            db.session.commit()

            return redirect('/posts')

        # posts_ = Posts.query.paginate(per_page = 2)
        # print(posts_.pages, "Nombre totale de page")
        # print(posts_.page, "Page courant")
        # print(posts_.has_next, "Page suivant")

        return render_template('pages/posts.html', formPost = form_post, posts=posts,user=user, posts_paginate= posts_paginate)
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
        user = Users.query.filter_by(email = session['email']).first()


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

    if "email"  in session:

        user = Users.query.filter_by(email = session['email']).first()
        albums = Albums.query.filter_by(id_users_albums = user.id_users).all()

        if request.method == 'POST' and form_album.validate():
            
            new_album = Albums(title_albums = form_album.title.data, id_users_albums = user.id_users)
            
            db.session.add(new_album)
            db.session.commit()

            return redirect('/albums')
        
        return render_template('pages/albums.html', formAlbum = form_album, albums = albums, user=user)

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
        user = Users.query.filter_by(email = session['email']).first()
    
        if request.method == 'POST' and form_photo.validate():
            
            new_photo = Photos(
                title_photos = form_photo.title.data,
                url = form_photo.url.data,
                thumbnailUrl = form_photo.thumbnail.data,
                id_albums_photos = album.id_albums
            )

            db.session.add(new_photo)
            db.session.commit()

            return redirect('/albums/'+album_name)

        return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos,user=user, album=album)
    else:
        return redirect('/connexion')

    return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos, albumId = albumId )






# CONTROLLER DE LA PAGE DES TODOS
def todos():
    form_todo = TodoForm(request.form)
    

    if  "email"  in session:
        user = Users.query.filter_by(email = session['email']).first()
        todos = Todos.query.filter_by(id_users_todos = user.id_users).all()

        if request.method == 'POST' and form_todo.validate():
                
            new_todo = Todos(
                title_todos = form_todo.title.data,
                status = form_todo.etat.data,
                id_users_todos = user.id_users
            )

            db.session.add(new_todo)
            db.session.commit()

            return redirect('/todos')

        return render_template('pages/todos.html', formTodo = form_todo, todos=todos ,user=user)
        
    else:
        return redirect('/connexion')




# CONTROLLER logout
def logout():
    session.clear()
    return redirect(url_for('.login'))







# CONTROLLER UPDATE DATAS FROM DB
def updated(type, id):

    user = Users.query.filter_by(email = session['email']).first()



    if type == 'posts':
        form_post = PostForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        if request.method == 'POST':
            new_title= form_post.title.data
            new_message=form_post.message.data
            print(new_title)
            Posts.query.filter_by(id_posts = id).update({'title_posts':new_title,'body_posts':new_message})
            db.session.commit()
            return redirect('/posts')
        
        return render_template('pages/edit.html', type=type, element=element, form_post=form_post)


    elif type == 'photos':
        form_photo = PhotoForm(request.form)
        element=Photos.query.filter_by(id_photos =id).first()

        if request.method == 'POST':
            new_title= form_photo.title.data
            new_url= form_photo.url.data
            new_thumnail=form_photo.thumbnail.data
            Photos.query.filter_by(id_photos =id).update({'title_photos':new_title, 'url':new_url, 'thumbnailUrl':new_thumnail})
            db.session.commit()
            return redirect('/albums')

        return render_template('pages/edit.html', type=type, element=element, form_photo=form_photo)


    elif type == 'todos':
        form_todo = TodoForm(request.form)
        element = Todos.query.filter_by(id_todos = id).first()
        
        if request.method == 'POST':
            new_title= form_todo.title.data
            new_etat = form_todo.etat.data
            Todos.query.filter_by(id_todos=id).update({'title_todos':new_title, 'status':new_etat})
            db.session.commit()
            return redirect('/todos')
        
        return render_template('pages/edit.html', type=type, element=element, form_todo=form_todo)


    elif type == 'albums':
        form_album = ALbumForm(request.form)
        element = Albums.query.filter_by(id_albums = id).first()
        if request.method == 'POST':
            new_title= form_album.title.data
            Albums.query.filter_by(id_albums=id).update({'title_albums':new_title})
            db.session.commit()
            return redirect('/albums')
        return render_template('pages/edit.html', type=type, element=element, form_album=form_album)


    elif type == 'comments':
        form_comment = CommentForm(request.form)
        element = Comments.query.filter_by(id_comments = id).first()
        return render_template('pages/edit.html', type=type, element=element, form_comment=form_comment)


    elif type == 'users':
        form_user = UserForm(request.form)
        element = Users.query.filter_by(id_users = id).first()
        compagny =  Compagny.query.filter_by(id_compagny  = element.id_company_users).first()
        adresse = Adresses.query.filter_by(id_adresse  = element.id_adresse_users ).first()
        print(compagny.name_compagny, adresse.zipcode)
        
        if request.method == 'POST':
            new_fullname = form_user.fullname.data
            new_username = form_user.username.data
            new_email = form_user.email.data
            new_phonel = form_user.phone.data
            new_website = form_user.website.data
            new_ville = form_user.ville.data
            new_rue = form_user.rue.data
            new_suite = form_user.suite.data
            new_zipcode = form_user.zipcode.data
            new_lat = form_user.lat.data
            new_long = form_user.long.data
            new_compagny = form_user.compagny.data
            new_bs = form_user.bs.data
            new_catch = form_user.catch.data
            # Users.query.filter_by(id_users = id).update({''})
            # db.session.commit()
            return redirect('/information')
    
        return render_template('pages/edit.html', type=type, element=element, form_user=form_user, compagny = compagny , adresse = adresse)
    
    else:
        return redirect('/compte')






# CONTROLLER DELETE DATAS FROM DB
list_pages_delete = ['posts', 'albums', 'todos']

def redirect_after_delete(page):
    for item in list_pages_delete:
        if page == item:
            return page
    return 'albums' 



def delete(type, id):

    if type == 'posts':
        element = Posts.query.get(id)

    elif type == 'albums':
        element = Albums.query.get(id)

    elif type == 'photos':
        element = Photos.query.get(id)

    elif type == 'todos':
        element = Todos.query.get(id)

    db.session.delete(element)
    db.session.commit()

    current_page = redirect_after_delete(type)

    return redirect(f"/{current_page}")





# CONTROLLER SHOW SINGLE COMMENT AND TODOS
def show(type,id):
    
    if type == 'todos':
        form_todo = TodoForm(request.form)
        element = Todos.query.filter_by(id_todos = id).first()        
        return render_template('pages/show.html', type=type, element=element, form_todo=form_todo)


    elif type == 'comments':
        form_comment = CommentForm(request.form)
        element = Comments.query.filter_by(id_comments = id).first()
        return render_template('pages/show.html', type=type, element=element, form_comment=form_comment)

    else:
        return redirect(url_for('.compte'))



# FUNCTIONS LOADERS
def load_posts(type):
    

    # GET CURRENT USER ID FROM APIs
    users_api = getApi('users')
    for user in users_api:
        if user.get('email') == session['email']:
            user_id = user.get('id')

    if type == 'posts':

        all_posts_from_apis = getApi(type)
        all_comments_from_apis = getApi('comments')
        current_user_id = Users.query.filter_by(email = session['email']).first().id_users

        for post in all_posts_from_apis :
            if post.get('userId') == user_id:
                new_post = Posts(
                    title_posts = post.get('title'), 
                    body_posts = post.get('body'), 
                    id_users_posts = current_user_id
                )
                db.session.add(new_post)
                db.session.commit()

                # Ajout les commentaires pour l'actuel post 
                for comment in all_comments_from_apis:
                    if comment.get('postId') == post.get('id'):
                        print("element dans comment",new_post.id_posts)

                        new_comment = Comments(
                            name_comments = comment.get('name'), 
                            body_comments = comment.get('body'),
                            email_comments = comment.get('email'),
                            id_posts_comments = new_post.id_posts
                        )
                        db.session.add(new_comment)
            
            db.session.commit()
                    
        return redirect(url_for('.posts'))
    
    elif type == 'todos':
        return redirect(url_for('.todos'))

    elif type == 'albums':
        return redirect(url_for('.albums'))

    elif type == 'photos':
        return redirect(url_for('.album'))

