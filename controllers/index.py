from flask import redirect, render_template, request, session, url_for
from models.forms import CommentForm, PhotoForm, TodoForm, UserForm, PostForm, ALbumForm


# CONTROLLER DE LA PAGE HOME
def home():
    form_user = UserForm(request.form)
    return render_template('pages/home.html', formUser=form_user)



# CONTROLLER DE LA PAGE DE CONNEXION
users =[
    {'email': 'awa@sa.sn', 'password':'passer789'},
    {'email': 'alpha@sa.sn', 'password':'passer123'},
    {'email': 'khabane@sa.sn', 'password':'passer456'},
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
    if "email" in session:
        return render_template('pages/posts.html', formPost = form_post)
    else:
        return render_template('pages/connexion.html')







# CONTROLLER DE LA PAGE DETAIL D'UN POST
def post():
    form_comment = CommentForm(request.form)
    if "email" in session:
        return render_template('pages/post.html', formComment = form_comment)
    else:
        return render_template('pages/connexion.html')







# CONTROLLER DE LA PAGE DES ALBUMS
def albums():
    form_album = ALbumForm(request.form)
    if "email"  in session:
        return render_template('pages/albums.html', formAlbum = form_album)
    else:
        return render_template('pages/connexion.html')





# CONTROLLER DE LA PAGE DETAIL D'UN ALBUM
def album():
    form_photo = PhotoForm(request.form)
    return render_template('pages/album.html', formPhoto = form_photo)
    






# CONTROLLER DE LA PAGE DES TODOS
def todos():
    form_todo = TodoForm(request.form)
    if  "email"  in session:
    
        return render_template('pages/todos.html', formTodo = form_todo)
    else:
        return render_template('pages/connexion.html')





# CONTROLLER DE LA PAGE MON COMPTE
def compte():
    if "email" in session:
        return render_template('pages/information.html')






