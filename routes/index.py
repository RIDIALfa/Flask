from flask import Blueprint
from controllers.index import afficheUser, creerAlbum, creerComment, creerPhoto, creerPost, creerTodo, creerUser, modifAlbum, modifComments, modifPhoto, modifPost, modifUser, visualisation
from controllers.index import  home, login, compte, posts, post, albums, album, todos, logout
from controllers.index import updated, delete
from controllers.index import show
from controllers.index import load_data, load_photos, dataViz, api_users, api_userType, api_PostComment, api_albumPhoto,api_delete, api_put




routers = Blueprint('root', __name__) 


routers.route('/', methods=['GET','POST'])(home)

routers.route('/connexion/', defaults={'email': ''}, methods=['GET','POST'])(login)
routers.route('/connexion/<email>', methods=['GET','POST'])(login)

routers.route('/compte/')(compte)

routers.route('/posts/', methods=['GET','POST'])(posts)

routers.route('/posts/', defaults={'post_title': ''}, methods=['GET','POST'])(post)
routers.route('/posts/<post_title>/', methods=['GET','POST'])(post)

routers.route('/albums/', methods=['GET','POST'])(albums)

routers.route('/albums/', defaults={'album_name': ''}, methods=['GET','POST'])(album)
routers.route('/albums/<album_name>/', methods=['GET','POST'])(album)

routers.route('/todos/', methods=['GET','POST'])(todos)

routers.route('/logout/')(logout)

#######ROUTE EDIT 
routers.route('/<type>/edit/<id>/',methods=['GET','POST'])(updated)

#######ROUTE DELETE
routers.route('/<type>/delete/<id>/')(delete)

#######ROUTE SHOW ['Comment, todos']
routers.route('/<type>/show/<id>/')(show)

#######LOAD DATA FROM APIs
routers.route('/charger_donnees/<type>/')(load_data)

routers.route('/charger/photos/<name_album>/')(load_photos)

####
routers.route('/dataViz/')(dataViz)

##### router API####
routers.route('/api/users/')(api_users)

routers.route('/api/users/<id>/')(api_users)
#routers.route('/api/users/<id>/')(api_userUpdate)

routers.route('/api/<theType>/')(api_userType)

routers.route('/api/users/<id>/<theType>/')(api_userType)

routers.route('/api/<theType>/<int:num>/')(api_userType)

routers.route('/api/posts/<id>/comments/')(api_PostComment)

routers.route('/api/albums/<id>/photos/')(api_albumPhoto)

routers.route('/api/<type>/<id>/', methods = ['DELETE'])(api_delete)

routers.route('/api/<type>/', methods=['PUT'])(api_put)
# routers.route('/api/posts/')(api_userPosts)

# routers.route('/api/todos/')(api_userTodos)

# routers.route('/api/users/<id>/todos/')(api_userPosts)

# routers.route('/api/albums/')(api_userAlbums)

# routers.route('/api/users/<id>/albums/')(api_userAlbums)

#######VISUALISATION POSTS
routers.route('/viz')(visualisation)
routers.route('/api/users')(afficheUser)

# ajouter des données
routers.route('/api/user',methods=['Post'])(creerUser)
routers.route('/api/todo',methods=['Post'])(creerTodo)
routers.route('/api/post',methods=['Post'])(creerPost)
routers.route('/api/album',methods=['Post'])(creerAlbum)
routers.route('/api/photo',methods=['Post'])(creerPhoto)
routers.route('/api/post/comment',methods=['Post'])(creerComment)

# modifier des données
routers.route('/api/users/<id>',methods=['Put'])(modifUser)
routers.route('/api/post/<id>',methods=['Put'])(modifPost)
routers.route('/api/album/<id>',methods=['Put'])(modifAlbum)
routers.route('/api/albums/photos/<id>',methods=['Put'])(modifPhoto)
routers.route('/api/posts/comments/<id>',methods=['Put'])(modifComments)
