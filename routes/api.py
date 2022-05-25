from flask import Blueprint

from controllers.apis import afficheUser
from controllers.apis import api_PostComment, api_albumPhoto, api_delete, api_put, api_userType, api_users
from controllers.apis import creerAlbum, creerComment, creerPhoto, creerPost, creerTodo, creerUser
from controllers.apis import modifComments, modifPhoto, modifPost, modifUser, modifAlbum


apis = Blueprint('api', __name__) 



##### router API####
apis.route('/api/users/')(api_users)

apis.route('/api/users/<id>/')(api_users)

apis.route('/api/<theType>/')(api_userType)

apis.route('/api/users/<id>/<theType>/')(api_userType)

apis.route('/api/<theType>/<int:num>/')(api_userType)

apis.route('/api/posts/<id>/comments/')(api_PostComment)

apis.route('/api/albums/<id>/photos/')(api_albumPhoto)

apis.route('/api/<type>/<id>/', methods = ['DELETE'])(api_delete)

apis.route('/api/<type>/', methods=['PUT'])(api_put)





apis.route('/api/users')(afficheUser)

# ajouter des données
apis.route('/api/user',methods=['Post'])(creerUser)
apis.route('/api/todo',methods=['Post'])(creerTodo)
apis.route('/api/post',methods=['Post'])(creerPost)
apis.route('/api/album',methods=['Post'])(creerAlbum)
apis.route('/api/photo',methods=['Post'])(creerPhoto)
apis.route('/api/post/comment',methods=['Post'])(creerComment)

# modifier des données
apis.route('/api/users/<id>',methods=['Put'])(modifUser)
apis.route('/api/post/<id>',methods=['Put'])(modifPost)
apis.route('/api/album/<id>',methods=['Put'])(modifAlbum)
apis.route('/api/albums/photos/<id>',methods=['Put'])(modifPhoto)
apis.route('/api/posts/comments/<id>',methods=['Put'])(modifComments)