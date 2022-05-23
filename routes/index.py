from crypt import methods
from flask import Blueprint
from controllers.index import afficheUser, creerAlbum, creerComment, creerPhoto, creerPost, creerTodo, creerUser, home, login, compte, modifAlbum, modifComments, modifPhoto, modifPost, modifUser, posts, post, albums, album, todos, logout,visualisation
from controllers.index import updated, delete
from controllers.index import show
from controllers.index import load_data, load_photos




routers = Blueprint('root', __name__)


routers.route('/', methods=['GET','POST'])(home)

routers.route('/connexion/', defaults={'email': ''}, methods=['GET','POST'])(login)
routers.route('/connexion/<email>', methods=['GET','POST'])(login)

routers.route('/compte/')(compte)

routers.route('/posts/', methods=['GET','POST'])(posts)

routers.route('/posts/', defaults={'post_title': ''}, methods=['GET','POST'])(post)
routers.route('/posts/<post_title>', methods=['GET','POST'])(post)

routers.route('/albums/', methods=['GET','POST'])(albums)

routers.route('/albums/', defaults={'album_name': ''}, methods=['GET','POST'])(album)
routers.route('/albums/<album_name>', methods=['GET','POST'])(album)

routers.route('/todos/', methods=['GET','POST'])(todos)

routers.route('/logout/')(logout)

#######ROUTE EDIT 
routers.route('/<type>/edit/<id>',methods=['GET','POST'])(updated)

#######ROUTE DELETE
routers.route('/<type>/delete/<id>')(delete)

#######ROUTE SHOW ['Comment, todos']
routers.route('/<type>/show/<id>')(show)

#######LOAD DATA FROM APIs
routers.route('/charger_donnees/<type>')(load_data)

routers.route('/charger/photos/<name_album>')(load_photos)


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
