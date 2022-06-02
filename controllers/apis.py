from flask import jsonify, request
from models.create_tables import Adresses, Albums, Comments, Compagny, Photos, Posts, Todos, Users, Utilisateur, db



# RETURNS ALL DICTS
def userdict(user):
    
    adresse = Adresses.query.filter_by(id_adresse = user.id_adresse_users).first()
    compagnie = Compagny.query.filter_by(id_compagny = user.id_company_users).first()

    return {
        'id': user.id_users,
        'fulname':user.fullname,
        'lastname':user.username,
        'email':user.email,
        'phone': user.phone,
        'website': user.website,
        "adresse": {
            "street":adresse.street,
            "suite":adresse.suite,
            "city":adresse.city,
            "zipcode":adresse.zipcode,
            "geo":{
                "lat":adresse.lat,
                "long":adresse.long
            }
        },
        "compagny":{
            "name":compagnie.name_compagny,
            "catchPhrase":compagnie.catchPhrase,
            "bs":compagnie.bs
        }
    }




def postdict(post):

    return { 
        'id':post.id_posts,
        'title_posts': post.title_posts,
        'body_posts': post.body_posts,
        'id_users_posts': post.id_users_posts,
        'visible_posts': post.visible_posts
    }





def todosdict(todo):

    return {
        'id':todo.id_todos, 
        'title_todos': todo.title_todos,
        'status': todo.status, 
        'id_users_todos': todo.id_users_todos
    }



def albumdict(album):
    
    return {
        'id_albums': album.id_albums,
        'title_albums': album.title_albums,
        'id_users_albums': album.id_users_albums,
        'visible_albums' : album.visible_albums
    }




def commentdict(com):
    
    return {
        'name_comments': com.name_comments,
        'email_comments': com.email_comments,
        'body_comments' : com.body_comments,
        'id_posts_comments' : com.id_posts_comments
    }




def photodict(post):
    
    return {
        'title_photos': post.title_photos,
        'url': post.url,
        'thumbnailUrl': post.thumbnailUrl,
        'id_albums_photos': post.id_albums_photos
    }





# ##############################
# ############# AWA ############
# ##############################

def creerUser():
    data=request.get_json()
    
    adr = Adresses(city=data.get("adresse")['city'],
        street = data.get("adresse")['street'],
        suite = data.get("adresse")['suite'],
        zipcode = data.get("adresse")['zipcode'],
        lat = data.get("adresse")['geo']['lat'],
        long = data.get("adresse")['geo']['long']
    )

    compagnie = Compagny(bs = data.get("compagny")['bs'],
        catchPhrase = data.get("compagny")['catchPhrase'],
        name_compagny = data.get("compagny")['name']
    )
    
    db.session.add(adr)
    db.session.add(compagnie)
    db.session.commit()

    get_id_add = Adresses.query.filter_by(city = data.get("adresse")['city']).first().id_adresse
    get_id_comp = Compagny.query.filter_by(bs = data.get("compagny")['bs']).first().id_compagny


    user = Users(
        fullname = data.get("username"),
        username = data.get("name"),
        email = data.get("email"),
        phone = data.get("phone"),
        website = data.get("website"),
        password = "paser",
        id_adresse_users = get_id_add,
        id_company_users = get_id_comp
    )

    db.session.add(user)
    db.session.commit()

    return "L'utilisateur a été ajouté avec succès !"



def creerPost():
    try:
        title = request.get_json().get('titre')
        body = request.get_json().get('message')
        user = request.get_json().get('userid')

        if title and body and user:
            post=Posts(
                title_posts = title,
                body_posts = body,
                id_users_posts = user
            )

            db.session.add(post)
            db.session.commit()

            return "L'article a été ajouté avec succès !"

        else : 
            return "Donner des valeurs aux différentes clés (titre, extrait, userid)", 400

    except AttributeError:
        return "Ce triplet de clés (titre, extrait, userid) n'existe pas dans le JSON", 400




def creerComment():
    
    try:

        data = request.get_json()
        name = data.get("titre"),
        email = data.get("email"),
        body = data.get("message"),
        post = data.get("postid")

        if name and email and body and post :

            comment = Comments(
                name_comments = name,
                email_comments = email,
                body_comments = body,
                id_posts_comments = post
            )

            db.session.add(comment)
            db.session.commit()

            return "Le commentaire a été ajouté avec succès !"

        else :
            return "Donner des valeurs aux différentes clés (titre, email, message, postid) ou format de données incorrect !", 400
    
    except AttributeError:
        return "Ce quadriplet de clés (titre, email, message, postid) n'existe pas dans le JSON", 400






def creerAlbum():

    try :
        data=request.get_json()
        title = data.get("titre")
        user = data.get("userid")

        if title and user and type(user) == int:

            album=Albums(
                title_albums = title,
                id_users_albums = user
            )

            db.session.add(album)
            db.session.commit()

            return "L'album a été ajouté avec succès !"
        else :
            return "Donner des valeurs aux différentes clés (titre, userid) ou format de données incorrect !", 400
    
    except AttributeError:
        return "Ce couple de clés (titre, userid) n'existe pas dans le JSON", 400



def creerPhoto():

    try:
        data = request.get_json()
        title = data.get('titre')
        url = data.get("url"),
        thumbnail = data.get("thumbnail"),
        album = data.get("albumid")

        if title and url and thumbnail and album and type(album) == int:

            photo = Photos(
                title_photos = title,
                url = url,
                thumbnailUrl = thumbnail,
                id_albums_photos = album
            )

            db.session.add(photo)
            db.session.commit()

            return "La photo a été ajouté avec succès !"
        
        else :
            return "Donner des valeurs aux différentes clés (titre, url, thumbnail, albumid) ou format de données incorrect !", 400
    
    except AttributeError:
        return "Ce quadriplet de clés (titre, url, thumbnail, albumid) n'existe pas dans le JSON", 400





def creerTodo():
    
    try:
        data=request.get_json()
        title = data.get('titre')
        etat = data.get('etat')
        user = data.get('userid')

        if title and etat and user and type(etat)== int:

            todo = Todos (
                title_todos = title,
                status = etat,
                id_users_todos = user
            )

            db.session.add(todo)
            db.session.commit()

            return "Le Todo a été ajouté avec succès !"
        else:
            return "Donner des valeurs aux différentes clés (titre, etat, userid), ou format de donné incorrect !", 400

    except AttributeError:
        return "Ce triplet de clés (titre, etat, userid) n'existe pas dans le JSON", 400



# ##################################
# ######## MODIFICATION ############
# ##################################

def modifUser(id):
    users=[]
    data=request.get_json()
    list_users=Users.query.all()

    for el in list_users:
        if id==el.id_users:
            el.fullname=data.get("fullname")
            el.username=data.get("username")
            el.email=data.get('email')
            el.phone=data.get('phone')
            el.website=data.get('website')
            el. adresse.street=data.get('street')
            el.adresse.suite=data.get('suite')
            el.adresse.city=data.get('city')
            el.adresse.zipcode=data.get('zipcode')
            el.adresse.lat=data.get('lat')
            el.adresse.long=data.get('long')
            el.compagny.name_compagny=data.get('name_compagnie')
            el.compagny.catchPhrase=data.get('catchPhrase')
            el.compagny.bs=data.get('bs')
            db.session.commit()

    return 'ok'

def modifPost(id):
    data=request.get_json()
    post = Posts.query.get(id)
    post.title_posts = data.get('title')
    post.body_posts = data.get('body')
    post.id_users_posts = data.get('userId')

    db.session.commit()
    return 'ok'


def modifAlbum(id):
    data=request.get_json()
    album=Albums.query.get(id)
    album.title_albums=data.get('title')
    album.id_users_albums=data.get('userId')

    db.session.commit()
    return 'ok'

def modifPhoto(id):
    data=request.get_json()
    photo=Photos.query.get(id)
    photo.title_photos=data.get('title')
    photo.url=data.get('url')
    photo.thumbnailUrl=data.get('thumbnailUrl')
    photo.id_albums_photos=data.get('albumId')

    db.session.commit()
    return 'ok'


def modifComments(id):
    data=request.get_json()
    comment=Comments.query.get(id)
    comment.name_comments=data.get('name')
    comment.email_comments=data.get('email')
    comment.body_comments=data.get('body')
    comment.id_posts_comments=data.get('postId')

    db.session.commit()
    return 'ok'




def api_put(type):
    if type=='albums':

        id=request.get_json().get('id_albums')
        alb=Albums.query.filter_by(id_albums=id).first()

        alb.title_albums= request.get_json().get('title_albums')
        alb.id_users_albums= request.get_json().get('id_users_albums'),
        alb.visible_albums= request.get_json().get('visible_albums')
        return 'album updated succesfully'

    elif type=='photos':
        id=request.get_json().get('id_photos')
        photo=Photos.query.filter_by(id_photos=id).first()
        
        photo.title_photos= request.get_json().get('title_photos')
        photo.id_albums_photos= request.get_json().get('id_albums_photos'),
        photo.url= request.get_json().get('url')
        photo.thumbnailUrl= request.get_json().get('thumbnailUrl')

        return 'photos updated succesfully'



###################################
####        API USERS            ##
###################################
def api_users(id = None):
    userlist=[]

    if id == None :
        users=Users.query.all()

        for user in users:
            user_dict = userdict(user)
            userlist.append(user_dict)
    
    else:

        user=Users.query.filter_by(id_users = id).first()
        user_dict=userdict(user)
        userlist.append(user_dict)

    return jsonify(userlist)   



def api_userType(id = None, type = '', num = None):
    
    result=[]
    if id == None:

        if type=='posts':
            posts=Posts.query.filter_by(visible_posts = 1).all()
            for post in posts:
                if post.id_posts==num:
                    result=[]
                    postd=postdict(post)
                    result.append(postd)
                    break
                else: 
                    postd=postdict(post)
                    result.append(postd)
    
        elif type=='todos':
            todos=Todos.query.filter_by(visible_todos = 1).all()
            for todo in todos:
                if todo.id_todos==num:
                    result=[]
                    todod=todosdict(todo)
                    result.append(todod)
                    break
                else:
                    todod=todosdict(todo)
                    result.append(todod)
            
        elif type=='albums':
            albs=Albums.query.filter_by(visible_albums = 1).all()
            for alb in albs:
                
                if alb.id_albums==num:
                    result=[]
                    albd=albumdict(alb)
                    result.append(albd)
                    break
                else:
                    albd=albumdict(alb)
                    result.append(albd)
                        
        elif type=='photos':
            photos=Photos.query.filter_by(visible_photos = 1).all()
            for el in photos:
                if el.id_photos==num:
                    result=[]
                    phot=photodict(el)
                    result.append(phot)
                    break
                else:
                    phot=photodict(el)
                    result.append(phot)

        elif type=='comments':
            comments=Comments.query.filter_by(visible_comments = 1).all()
            for el in comments:
                if el.id_comments==num:
                    result=[]
                    com=commentdict(el)
                    result.append(com)  
                    break
                else:
                    com=commentdict(el)
                    result.append(com) 
    else:

        if type=='posts':
            posts=Users.query.filter_by(id_users =  id).first().posts
            for post in posts:
                postd=postdict(post)
                result.append(postd)
        
        elif type=='todos':
            todos=Users.query.filter_by(id_users =  id).first().todos
            for todo in todos:
                todod=todosdict(todo)
                result.append(todod)
                
        elif type=='albums':
            albs=Users.query.filter_by(id_users =  id).first().albums
            for alb in albs:
                albd=albumdict(alb)
                result.append(albd)

    return jsonify(result)





def api_PostComment(id):

    result = [] 
    comments = Posts.query.filter_by(id_posts=id).first().comments

    for com in comments:

        comment = commentdict(com)
        result.append(comment)

    return jsonify(result)
    




def api_albumPhoto(id):
    
    result = []
    photos = Albums.query.filter_by(id_albums=id).first().photos

    for photo in photos:
        photo = photodict(photo)
        result.append(photo)
    
    return jsonify(result)



visible = 0

def api_delete(id, type):

    if type == 'users':
        user=Users.query.filter_by(id_users=id).first()
        posts = user.posts
        albums = user.albums
        todos = user.todos
        
        for post in posts:
            post.visible_posts = visible

            for comment in post.comments:
                comment.visible_comments = visible
        
        for album in albums:
            album.visible_albums = visible
            
            for photo in album.photos:
                photo.visible_photos = visible
        
        for todo in todos:
            todo.visible_todos = visible

        return user.fullname + ' supprimé avec succès !'



    elif type == 'posts':
        posts = Posts.query.filter_by(id_posts=id).first()
        comments = posts.comments
        current_user = request.get_json().get('userid')
        post_user_id = posts.id_users_posts

        if current_user == post_user_id:

            for comment in comments:
                comment.visible_comments = visible
            
            posts.visible_posts = visible
            
            return "L'article et ses commentaires ont été supprimés avec succès."
        
        else:
            return "Désolé vous ne pouvez pas supprimé cet Article. Assurez-vous d'avoir les accès nécessaires.", 403



    elif type=='todos':
        todo=Todos.query.filter_by(id_todos=id).first()
        current_user=request.get_json().get('userid')
        todo_user_id=todo.id_users_todos

        if current_user == todo_user_id:
            todo.visible_todos = visible
            
            return "Todo supprimé avec succès"
        
        else:
            return "Désolé vous ne pouvez pas supprimé ce Todo. Assurez-vous d'avoir les accès nécessaires.", 403


    
    elif type == 'albums':
        album = Albums.query.filter_by(id_albums=id).first()
        current_user = request.get_json().get('userid')
        todo_user_id = album.id_users_albums

        if current_user == todo_user_id:

            for photo in album.photos:
                photo.visible_photos = visible
            
            album.visible_albums = visible
            
            return "L'album avec ses photos ont été supprimés avec succès."

        else:
            return "Désolé vous ne pouvez pas supprimé cet Album. Assurez-vous d'avoir les accès nécessaires.", 403




    elif type == 'photos':
        photo = Photos.query.filter_by(id_photos=id).first()
        current_user = request.get_json().get('userid')
        photo_user_id = photo.id_users_albums

        if current_user == photo_user_id:
            photo.visibile_photos = visible

            return 'Photo supprimée avec succès'

        else:
            return "Désolé vous ne pouvez pas supprimé cette photo. Assurez-vous d'avoir les accès nécessaires.", 403

    
    elif type=='comments':
        comment=Comments.query.filter_by(id_comments=id).first()
        current_user=request.get_json().get('userid')
        comment_user_id=comment.id_users_comments

        if current_user == comment_user_id:

            comment.visibile_comments=visible
            
            return 'Commentaire supprimé avec succès'

        else:
            return "Désolé vous ne pouvez pas supprimé ce commentaire. Assurez-vous d'avoir les accès nécessaires.", 403




def api_utilisateur():
    utilisateurs = Utilisateur.query.all()
    listes = []

    for user in utilisateurs:
        new_dict = {
            "email" : user.email,
            "password" : user.password,
            "profile" : user.profile
        }
        listes.append(new_dict)

    return jsonify(listes)