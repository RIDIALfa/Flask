from flask import Blueprint
from controllers.index import home, login, compte, posts, post, albums, album, todos, delete_post,  delete_album, logout, edit, editPhoto, editPost



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

routers.route('/posts/delete/<indice_post>')(delete_post)

routers.route('/editer/<title>',methods=['GET','POST'])(edit)


routers.route('/editerPost/<title>',methods=['GET','POST'])(editPost)

routers.route('/logout/')(logout)


routers.route('/editerPhotos/<title>',methods=['GET','POST'])(editPhoto)

routers.route('/album/delete/<indice_album>')( delete_album)
