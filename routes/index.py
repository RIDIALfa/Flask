from flask import Blueprint
from controllers.index import home, login, compte, posts, post, albums, album, todos



routers = Blueprint('root', __name__)



routers.route('/')(home)

routers.route('/connexion/')(login)

routers.route('/compte/')(compte)

routers.route('/posts/')(posts)

routers.route('/post/')(post)

routers.route('/albums/')(albums)

routers.route('/album/')(album)

routers.route('/todos/')(todos)





