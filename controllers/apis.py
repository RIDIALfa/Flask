from flask import jsonify
from requests import request
from models.create_tables import Adresses, Albums, Comments, Compagny, Photos, Posts, Todos, Users, db


# ############################
# #############KAWA###########
# ############################
def afficheUser():
    user=[]
    list_users=Users.query.all()

    for el in list_users:
        id=el.id_adresse_users
        id_comp=el.id_company_users
        adresse=Adresses.query.filter_by(id_adresse=id).first()
        compagnie=Compagny.query.filter_by(id_compagny=id_comp).first()

        dict={
            "name":el.fullname,
            "username":el.username,
            "email":el.email,
            "phone":el.phone,
            "website":el.website,  
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
        user.append(dict)

    return jsonify(user)



def creerUser():
    data=request.get_json()
    adr = Adresses(city=data.get("adresse")['city'],street=data.get("adresse")['street'],suite=data.get("adresse")['suite'],zipcode=data.get("adresse")['zipcode'],lat=data.get("adresse")['geo']['lat'],long=data.get("adresse")['geo']['long'])
    compagnie=Compagny(bs=data.get("compagny")['bs'],catchPhrase=data.get("compagny")['catchPhrase'],name_compagny=data.get("compagny")['name'])
    
    db.session.add(adr)
    db.session.add(compagnie)
    db.session.commit()

    get_id_add = Adresses.query.filter_by(city=data.get("adresse")['city']).first().id_adresse
    get_id_comp=Compagny.query.filter_by(bs=data.get("compagny")['bs']).first().id_compagny


    user = Users(fullname=data.get("username"),username=data.get("name"),email=data.get("email"),phone=data.get("phone"),website=data.get("website"),password="paser",id_adresse_users=get_id_add,id_company_users=get_id_comp)
    db.session.add(user)
    db.session.commit()
    # print(data)

    return 'ok'
def creerTodo():
    data=request.get_json()
    todo=Todos(title_todos=data.get("title"),status=data.get("status"),id_users_todos=data.get("userid"))
    db.session.add(todo)
    db.session.commit()
    return 'ok'

def creerPost():
    data=request.get_json()
    post=Posts(title_posts=data.get("titre"),body_posts=data.get("extrait"),id_users_posts=data.get("id_post"))
    db.session.add(post)
    db.session.commit()
    return 'ok'

def creerAlbum():
    data=request.get_json()
    album=Albums(title_albums=data.get("title"),id_users_albums=data.get("id_user"))
    db.session.add(album)
    db.session.commit()

    return 'ok'

def creerPhoto():
    data=request.get_json()
    photo=Photos(title_photos=data.get("title"),url=data.get("url"),thumbnailUrl=data.get("thumbnailUrl"),id_albums_photos=data.get("id_album"))
    db.session.add(photo)
    db.session.commit()

    return 'ok'

def creerComment():
    data= request.get_json()
    comment=Comments(name_comments=data.get("name"),email_comments=data.get("email"),body_comments=data.get("comment"),id_posts_comments=data.get("id_post_comment"))
    db.session.add(comment)
    db.session.commit()
    return 'ok'

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



###################################
####        API USERS            ##
###################################

def userdict(user):
    nodict={
                'fulname':user.fullname,
                'lastname':user.username,
                'id': user.id_users,
                'email':user.email,
                'phone': user.phone,
                'website': user.website,
                'origin': user.origine 
            }
    return nodict

def postDict(post):
    nodict={ 
        'id':post.id_posts,
        'title_posts': post.title_posts,
        'body_posts': post.body_posts,
        'id_users_posts': post.id_users_posts,
        'visible_posts': post.visible_posts
    }
    return  nodict

def todosDict(todo):
    nodict={
        'id':todo.id_todos, 
    'title_todos': todo.title_todos,
    'status': todo.status, 
    'id_users_todos': todo.id_users_todos
    }
    return nodict
def albumDict(album):
    nodict={
        'id_albums': album.id_albums,
        'title_albums': album.title_albums,
        'id_users_albums': album.id_users_albums,
        'visible_albums' : album.visible_albums
    }
    return nodict

def commentDict(com):
    nodict={
        'name_comments': com.name_comments,
        'email_comments': com.email_comments,
        'body_comments' : com.body_comments,
        'id_posts_comments' : com.id_posts_comments
    }

def photoDict(post):
    nodict={

    'title_photos': post.title_photos,
    'url': post.url,
    'thumbnailUrl': post.thumbnailUrl,
    'id_albums_photos': post.id_albums_photos
    }
    return nodict

def api_users(id='maobe'):
    userlist=[]

    if id=='maobe':
        users=Users.query.all()
        for user in users:
            userDict=userdict(user)
            userlist.append(userDict)
    else:
        user=Users.query.filter_by(id_users =  id).first()
        userDict=userdict(user)
        userlist.append(userDict)

    return jsonify(userlist)   



def api_userType(id='maobé', theType='', num='maobé',use='maobé'):
    
    result=[]
    if id=='maobé':
            
        if theType=='posts':
            posts=Posts.query.all()
            for post in posts:
                if post.id_posts==num:
                    result=[]
                    postd=postDict(post)
                    result.append(postd)
                    break
                else: 
                    postd=postDict(post)
                    result.append(postd)
    
        elif theType=='todos':
            todos=Todos.query.all()
            for todo in todos:
                if todo.id_todos==num:
                    result=[]
                    todod=todosDict(todo)
                    result.append(todod)
                    break
                else:
                    todod=todosDict(todo)
                    result.append(todod)
            
        elif theType=='albums':
            albs=Albums.query.all()
            for alb in albs:
                
                if alb.id_albums==num:
                    result=[]
                    albd=albumDict(alb)
                    result.append(albd)
                    break
                else:
                    albd=albumDict(alb)
                    result.append(albd)
                        
        elif theType=='photos':
            photos=Photos.query.all()
            for el in photos:
                if el.id_photos==num:
                    result=[]
                    phot=photoDict(el)
                    result.append(phot)
                    break
                else:
                    phot=photoDict(el)
                    result.append(phot)
        elif theType=='comments':
            comments=Comments.query.all()
            for el in comments:
                if el.id_comments==num:
                    result=[]
                    com=commentDict(el)
                    result.append(com)  
                    break
                else:
                    com=commentDict(el)
                    result.append(com) 
    else:
        
            if theType=='posts':
                posts=Users.query.filter_by(id_users =  id).first().posts
                for post in posts:
                    postd=postDict(post)
                    result.append(postd)
        
            elif theType=='todos':
                todos=Users.query.filter_by(id_users =  id).first().todos
                for todo in todos:
                    todod=todosDict(todo)
                    result.append(todod)
                
            elif theType=='albums':
                albs=Users.query.filter_by(id_users =  id).first().albums
                for alb in albs:
                    albd=albumDict(alb)
                    result.append(albd)

    return jsonify(result)

def api_PostComment(id):
    post=Posts.query.filter_by(id_posts=id).first()
    coms=Comments.query.all()
    liste=[] 
    for com in coms:
        if com.id_posts_comments==post.id_posts:
                pos=commentDict(com)
                liste.append(pos)
    return jsonify(liste)
    
def api_albumPhoto(id):
    liste=[]
    photos=Albums.query.filter_by(id_albums=id).first().photos
    for photo in photos:
        phot=photoDict(photo)
        liste.append(phot)
    return jsonify(liste)


def api_delete(id, type):
    if type=='users':
        user=Users.query.filter_by(id_users=id).first()
        posts=user.posts
        albums=user.albums
       # photos=albums.photos
        todos=user.todos
        for post in posts:
            post.visible_posts=0
        for album in albums:
            album.visible_photos=0
        #for photo in photos:
        #    photo.update({'visible_photos':0})
        for todo in todos:
            todo.visible_todos=0
        return user.fullname+' and his childreen were deleted with succes'
    elif type=='posts':
        posts=Posts.query.filter_by(id_posts=id).first()
        comments=posts.comments
        thisUser=request.get_json().get('userid')
        postUser=posts.id_users_posts

        if thisUser==postUser:
            for comment in comments:
                comment.visible_comments=0
            posts.visible_posts=0
            return 'the post and his comments were deleted with succes'
        else:
            return 'ce post n est pas celui de cet utilsateur',403
    elif type=='todos':
        todo=Todos.query.filter_by(id_todos=id).first()
        thisTodo=request.get_json().get('userid')
        todoUser=todo.id_users_todos

        if thisTodo==todoUser:
            todo.visible_todos=0
            return 'todo deleted succesfully'
        else:
            return 'ce todo n est pas celui de l\'utilasateur connecté', 403

    
    elif type=='albums':
        album=Albums.query.filter_by(id_albums=id).first()
        thisAlb=request.get_json().get('userid')
        albUser=album.id_users_albums

        if thisAlb==albUser:
            album.visible_albums=0
            photos=album.photos
            for photo in photos:
                photo.visible_photos
            return 'album with his phtoos were deleted succesfully'

        else:
            return 'cet album n\'est pas celui de l\'utilasateur connecté', 403

    elif type=='photos':
        photo=Photos.query.filter_by(id_photos=id).first()
        thisPhoto=request.get_json().get('userid')
        photoUser=photo.id_users_albums

        if thisPhoto==photoUser:
            photo.visibile_photos=0
            return 'photo deleted with succes'
        else:
            return 'this photo is not for the connected user', 403
    elif type=='comments':
        comment=Comments.query.filter_by(id_comments=id).first()
        thisComment=request.get_json().get('userid')
        commentUser=comment.id_users_comments

        if thisComment==commentUser:
            comment.visibile_comments=0
            return 'comment deleted with succes'
        else:
            return 'this comment is not for the connected user', 403

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