from flask import Blueprint
from controllers.index import home, login, compte, posts, post, albums, album, todos


routers = Blueprint('root', __name__)


routers.route('/')(home)

routers.route('/connexion/', defaults={'email': ''})(login)
routers.route('/connexion/<email>')(login)

routers.route('/compte/')(compte)

routers.route('/posts/', methods=['GET','POST'])(posts)

routers.route('/posts/', defaults={'post_title': ''}, methods=['GET','POST'])(post)
routers.route('/posts/<post_title>', methods=['GET','POST'])(post)

routers.route('/albums/', methods=['GET','POST'])(albums)

routers.route('/albums/', defaults={'album_name': ''}, methods=['GET','POST'])(album)
routers.route('/albums/<album_name>', methods=['GET','POST'])(album)

routers.route('/todos/', methods=['GET','POST'])(todos)





