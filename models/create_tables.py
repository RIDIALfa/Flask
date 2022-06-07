from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

###############################
######CREATION DES TABLES######
###############################


###TAB UTULISATEUR
class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id_utilisateur = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(75), nullable=False)
    profile = db.Column(db.String, nullable=False)

####TAB COMPAGNY
class Adresses(db.Model):
    __tablename__ = 'adresses'
    
    id_adresse = db.Column(db.Integer, primary_key = True)
    street = db.Column(db.String(250), nullable = False)
    suite = db.Column(db.String(200), nullable = False)
    city = db.Column(db.String(200), nullable = False)
    zipcode = db.Column(db.String(100), nullable = False)
    lat = db.Column(db.String(50), nullable = False)
    long = db.Column(db.String(50), nullable = False)
    
    # Adresses childreen relations
    users = db.relationship('Users', backref = "adresses")

    def __ref__(self):
        return '<Adresses %r>' % self.city



####TAB COMPAGNY
class Compagny(db.Model):
    __tablename__ = 'compagny'

    id_compagny = db.Column(db.Integer, primary_key = True)
    name_compagny = db.Column(db.String(150), nullable = False, unique = True)
    catchPhrase = db.Column(db.String(150), nullable = True)
    bs = db.Column(db.String(150), nullable = False)

    # Compagny childreen relationsh
    users = db.relationship("Users", backref = "compagny")

    def __ref__(self):
        return '<Compagny %r>' % self.name_compagny



####TAB USERS
class Users(db.Model):
    __tablename__ = 'users'
    id_users = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    phone = db.Column(db.String(50), nullable = True)
    website = db.Column(db.String(100), nullable = True)
    password = db.Column(db.String(100), nullable = False)
    origine = db.Column(db.Integer, nullable = False, default=1)
    visible_users = db.Column(db.Integer, default=1)

    # users childreen relations
    posts = db.relationship("Posts", backref = "users")
    todos = db.relationship("Todos", backref = "users")
    albums = db.relationship("Albums", backref = "users")
    
    # users parents relations
    id_adresse_users = db.Column(db.Integer, db.ForeignKey('adresses.id_adresse'))
    id_company_users = db.Column(db.Integer, db.ForeignKey('compagny.id_compagny'))
    
    def __repr__(self):
        return '<Users %r>' % self.fullname



####TAB POSTS
class Posts(db.Model):
    __tablename__ = 'posts'
    id_posts = db.Column(db.Integer, primary_key = True)
    title_posts = db.Column(db.String(150), nullable = False)
    body_posts = db.Column(db.Text, nullable = False)
    id_users_posts = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    visible_posts = db.Column(db.Integer, default=1)

    # users childreen relations
    comments = db.relationship("Comments", backref='posts')

    def __repr__(self):
        return '<Posts %r>' % self.title_posts




####TAB POSTS
class Comments(db.Model):
    __tablename__ = 'comments'
    id_comments = db.Column(db.Integer, primary_key = True)
    name_comments = db.Column(db.String(150), nullable = False)
    email_comments = db.Column(db.String(100), nullable = False)
    body_comments = db.Column(db.Text, nullable = False)
    id_posts_comments = db.Column(db.Integer, db.ForeignKey('posts.id_posts'))
    visible_comments = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Comments %r>' % self.name_comments


####TAB TODOS
class Todos(db.Model):
    __tablename__ = 'todos'
    id_todos = db.Column(db.Integer, primary_key = True)
    title_todos = db.Column(db.String(100), nullable = False)
    status = db.Column(db.Integer, nullable = False)
    id_users_todos = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    visible_todos = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Todos %r>' % self.title_todos



####TAB ALBUMS
class Albums(db.Model):
    __tablename__ = 'albums'
    id_albums = db.Column(db.Integer, primary_key = True)
    title_albums = db.Column(db.String(150), nullable=False)
    id_users_albums = db.Column(db.Integer, db.ForeignKey('users.id_users'))
    visible_albums = db.Column(db.Integer, default=1)

    photos = db.relationship('Photos', backref ='albums')

    def __repr__(self):
        return '<Albums %r>' % self.title_albums




####TAB PHOTOS
class Photos(db.Model):
    __tablename__ = "photos"
    id_photos = db.Column(db.Integer, primary_key = True)
    title_photos = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    thumbnailUrl = db.Column(db.String(150), nullable=False)
    id_albums_photos = db.Column(db.Integer, db.ForeignKey('albums.id_albums'))
    visible_photos = db.Column(db.Integer, default=1)


    def __repr__(self):
        return '<Photos %r>' % self.title_photos



def create_all_tables():
    db.create_all()
