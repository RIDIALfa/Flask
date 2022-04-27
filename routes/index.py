from flask import Blueprint
from controllers.index import edit, editPost, home, login, compte, posts, post, albums, album, todos,logout


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

routers.route('/editer/<title>',methods=['GET','POST'])(edit)

routers.route('/editerPost/<title>',methods=['GET','POST'])(editPost)





