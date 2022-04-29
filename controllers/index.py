from flask import redirect, render_template, request, session, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from models.create_tables import Adresses, Compagny, Users, Posts, Comments, Albums, Photos, Todos, db

import requests



def getApi(param):

    url='https://jsonplaceholder.typicode.com/'

    reponse=requests.get(url+param)
    
    return reponse.json()
    



# Fake datas
users =[
    {'email': 'awa@sa.sn', 'password':'passer789', 'fullname':'awa diop', 'phone': 330000000, 'lat': 34.05855065769437, 'long' : -118.25096592088265},
    {'email': 'alpha@sa.sn', 'password':'passer123', 'fullname':'alpha diallo', 'phone': 440000000, 'lat': 14.872029, 'long' : -17.436139},
    {'email': 'khabane@sa.sn', 'password':'passer456', 'fullname':'khabane fall', 'phone': 550000000, 'lat': 16.7727, 'long' : -19.361339},
]


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
            
        id_adresse = 1
        db.session.add(new_adresse)
        db.session.commit()
        

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

        id_compagny = 1

        db.session.add(new_compagny)
        db.session.commit()

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
            phone = user.get('phone'),
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



# CONTROLLER  editer
def edit(title):
    form_todo = TodoForm(request.form)
    element=Todos.query.filter_by(title_todo=title).first()
    if request.method == 'POST':
        new_title= form_todo.title.data
        Todos.query.filter_by(title_todo=title).update({'title_todo':new_title})
        db.session.commit()
        return redirect('/todos')
    
    print(title)
    return render_template('pages/editer.html',form_todo=form_todo,element=element)
    


def editPost(title):
    form_post = PostForm(request.form)
    element=Posts.query.filter_by(title_post=title).first()
    if request.method == 'POST':
        new_title= form_post.title.data
        new_message=form_post.message.data
        Posts.query.filter_by(title_post=title).update({'title_post':new_title,'body_post':new_message})
        db.session.commit()
        return redirect('/posts')
    
    print(title)
    return render_template('pages/editerPost.html',form_post=form_post,element=element)
  



def editPhoto(title):
    form_photo = PhotoForm(request.form)
    element=Photos.query.filter_by(title_photo=title).first()
    if request.method == 'POST':
        new_title= form_photo.title.data
        new_url= form_photo.url.data
        new_thumnail=form_photo.thumbnail.data
        Photos.query.filter_by(title_photo=title).update({'title_photo':new_title,'thumnail_photo':new_thumnail,'url_photo':new_url})
        db.session.commit()
        return redirect('/albums')
    
    print(title)
    return render_template('pages/editerPhotos.html',form_photo=form_photo,element=element)
    


def editUser(title):
    form_user = UserForm(request.form)
    element=Users.query.filter_by(fullname=title).first()
    if request.method == 'POST':
            new_fullname= form_user.title.data
            new_username= form_user.url.data
            new_email=form_user.thumbnail.data
            new_email=form_user.thumbnail.data
            new_email=form_user.thumbnail.data
            new_email=form_user.thumbnail.data
            Photos.query.filter_by(title_photo=title).update({'title_photo':new_title,'thumnail_photo':new_thumnail,'url_photo':new_url})
            db.session.commit()
            return redirect('/albums')
    
    print(title)
    return render_template('pages/editerPhotos.html',form_user=form_user,element=element)
    



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




def updated(type, id):

    if type == 'posts':
        form_post = PostForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_post=form_post)
    
    elif type == 'photos':
        form_photo = PhotoForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_photo=form_photo)
    
    elif type == 'todos':
        form_todo = TodoForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_todo=form_todo)

    elif type == 'albums':
        form_album = ALbumForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_album=form_album)

    elif type == 'comments':
        form_comment = CommentForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_comment=form_comment)

    elif type == 'users':
        form_user = UserForm(request.form)
        element = Posts.query.filter_by(id_posts = id).first()
        return render_template('pages/alpha_edit.html', type=type, element=element, form_user=form_user)

    else:
        return redirect('/compte')



# CONTROLLER logout
def logout():
    session.clear()
    return redirect(url_for('.login'))

