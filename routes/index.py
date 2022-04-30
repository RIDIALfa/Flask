from crypt import methods
from flask import Blueprint
from controllers.index import home, login, compte, posts, post, albums, album, todos, logout
from controllers.index import delete_post,  delete_album
from controllers.index import updated
from controllers.index import load_posts




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
routers.route('/album/delete/<indice_album>')( delete_album)

routers.route('/posts/delete/<indice_post>')(delete_post)

#LOAD DATA FROM APIs
routers.route('/charger_donnees/<type>')(load_posts)

