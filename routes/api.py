from flask import Blueprint

from controllers.apis import api_PostComment, api_albumPhoto, api_delete, api_put, api_userType, api_users, api_utilisateur, api_utilisateur_current
from controllers.apis import creerAlbum, creerComment, creerPhoto, creerPost, creerTodo, creerUser
from controllers.apis import modifComments, modifPhoto, modifPost, modifUser, modifAlbum

apis = Blueprint('api', __name__) 


###########################################
######## APIs | GET | DELETE ##############
###########################################

apis.route('/api/users/')(api_users)
apis.route('/api/users/<id>/')(api_users)


apis.route('/api/users/<id>/<type>/')(api_userType)
apis.route('/api/<type>/')(api_userType)
apis.route('/api/<type>/<int:num>/')(api_userType)


apis.route('/api/posts/<id>/comments/')(api_PostComment)


apis.route('/api/albums/<id>/photos/')(api_albumPhoto)


apis.route('/api/<type>/<id>/', methods = ["DELETE"])(api_delete)





###########################################
######## APIs | POST | PUT ##############
###########################################

### METHODE POST
apis.route('/api/user',methods = ['POST'])(creerUser)
apis.route('/api/todo',methods = ['POST'])(creerTodo)
apis.route('/api/post',methods = ['POST'])(creerPost)
apis.route('/api/album',methods = ['POST'])(creerAlbum)
apis.route('/api/photo',methods = ['POST'])(creerPhoto)
apis.route('/api/post/comment',methods = ['POST'])(creerComment)

### METHODE PUT
apis.route('/api/users/<id>',methods = ['PUT'])(modifUser)
apis.route('/api/post/<id>',methods = ['PUT'])(modifPost)
apis.route('/api/album/<id>',methods = ['PUT'])(modifAlbum)
apis.route('/api/albums/photos/<id>',methods = ['PUT'])(modifPhoto)
apis.route('/api/posts/comments/<id>',methods = ['PUT'])(modifComments)

apis.route('/api/<type>/', methods = ['PUT'])(api_put)



apis.route('/api/utilisateurs/')(api_utilisateur)
apis.route('/api/utilisateur/<email>/')(api_utilisateur_current)


