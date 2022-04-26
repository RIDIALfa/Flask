from errno import EUSERS
from flask import redirect, render_template, request, session, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm
from models.creates_tables import Posts, Todos, Comments, Albums, Photos, db

# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)
    return render_template('pages/home.html', formUser=form_user)



# CONTROLLER DE LA PAGE DE CONNEXION

34.05855065769437, -118.25096592088265
users =[
    {'email': 'awa@sa.sn', 'password':'passer789', 'fullname':'awa diop', 'phone': 330000000, 'lat': 34.05855065769437, 'long' : -118.25096592088265},
    {'email': 'alpha@sa.sn', 'password':'passer123', 'fullname':'alpha diallo', 'phone': 440000000, 'lat': 14.872029, 'long' : -17.436139},
    {'email': 'khabane@sa.sn', 'password':'passer456', 'fullname':'khabane fall', 'phone': 550000000, 'lat': 16.7727, 'long' : -19.361339},
]

def login(email):

    if request.method == 'POST':
        mail=request.form['email']
        passwd=request.form['password']
        print("saisie : ",mail, passwd)
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
    posts = Posts.query.filter_by(userId_post = 1).all()
    if "email" in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

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

            return redirect('/posts')
            # return render_template('pages/posts.html', formPost = form_post, posts=posts)

        return render_template('pages/posts.html', formPost = form_post, posts=posts,user=user)
    else:

        return redirect('/connexion')







# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post(post_title):
    form_comment = CommentForm(request.form)
    post = Posts.query.filter_by(title_post=post_title).first()
    comments = Comments.query.filter_by(postId_comment = post.postId).all()

    if "email" in session:
        for i in users:
             if i['email']==session['email']:
                 user = i

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
                title_album = form_album.title.data, 
                userId_album = 1
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
    albumId = Albums.query.filter_by(title_album=album_name).first().albumId
    photos = Photos.query.filter_by(albumId_photo = albumId).all()
    
    if  "email"  in session:
        for i in users:
             if i['email']==session['email']:
                 user = i
    

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

        return render_template('pages/album.html', formPhoto = form_photo, album_name = album_name, photos=photos,user=user)
    else:
        return redirect('/connexion')









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
                title_todo = form_todo.title.data,
                etat_todo = form_todo.etat.data,
                userId_todo = 1
            )

            print(new_todo)
            print(new_todo.title_todo, new_todo.etat_todo)
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
                #  user.append(i['fullname'])
                #  user.append(i['phone'])
                #  user.append(i['email'])
                 print(user)


        
        return render_template('pages/information.html', user=user)

    else:
        return redirect('/connexion')

# CONTROLLER logout

def logout():

    session.clear()
    return redirect(url_for('.login'))







