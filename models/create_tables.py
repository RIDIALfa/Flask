from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from main import app
from sqlalchemy.orm import relationship

# configurations syst

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://groupe3:passer123@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# creating database connection
mydb=SQLAlchemy(app)

class adresse(mydb.Model):
    __tablename__='adresse'
    users_id = relationship("users", backref="adresse")
    id_addresse = mydb.Column(mydb.Integer, primary_key=True)
    street = mydb.Column(mydb.String(200), nullable=False)
    suite = mydb.column(mydb.String(200), nullable=False)
    city = mydb.Column(mydb.String(200), nullable=False)
    zipcode = mydb.Column(mydb.String(100), nullable=False)
    lat = mydb.Column(mydb.String(50), nullable=False)
    long = mydb.Column(mydb.String(50), nullable=False)

class company(mydb.Model):
    users = relationship("users", backref="company")
    id_company = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(200), nullable=False)
    catchPhrase = mydb.column(mydb.String(200), nullable=False)
    bs = mydb.Column(mydb.String(200), nullable=False)
class users(mydb.Model):
    __tablename__='users'
    id_users = mydb.Column(mydb.Integer, primary_key=True)
    userName = mydb.Column(mydb.String(200), nullable=False)
    Email = mydb.column(mydb.String(200), nullable=False)
    phone = mydb.Column(mydb.String(50), nullable=False)
    website = mydb.Column(mydb.String(200), nullable=False)

    # users childreen relations
    posts = relationship("posts", backref="users")
    todos = relationship("todos", backref="users")
    albums = relationship("albums", backref="users")
    
    # users parents relations
    id_adresse = mydb.column(mydb.Integer, mydb.ForeignKey('adresse.id_adresse'))
    id_company = mydb.column(mydb.Integer, mydb.ForeignKey('company.id_company'))
    
class posts(mydb.Model):
    __tablename__='posts'
    id_posts = mydb.Column(mydb.Integer, primary_key=True)
    title_posts = mydb.Column(mydb.String(200), nullable=False)
    body = mydb.column(mydb.String(200), nullable=False)

    comments = relationship("comments")

    id_users = mydb.column(mydb.Integer, mydb.ForeignKey('users.id_users'))

class comments(mydb.Models):
    __tablename__='comments'
    id_comments = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(200), nullable=False)
    Email = mydb.column(mydb.String(100), nullable=False)
    body = mydb.column(mydb.String(200), nullable=False)

    id_posts = mydb.column(mydb.Integer, mydb.ForeignKey('posts.id_posts'))

class todos(mydb.Models):
    __tablename__='todos'
    id_todos = mydb.Column(mydb.Integer, primary_key=True)
    title_todos= mydb.column(mydb.String(200), nullable=False)

    id_users = mydb.column(mydb.Integer, mydb.ForeignKey('users.id_users'))

class albums(mydb.Models):
    __tablename__='albums'
    id_albums = mydb.Column(mydb.Integer, primary_key=True)
    title_albums= mydb.column(mydb.String(200), nullable=False)

    photos= relationship("photos")

class photos(mydb.Models):
    __tablename__="photos"
    id_photos = mydb.Column(mydb.Integer, primary_key=True)
    albums = mydb.column(mydb.String(200), nullable=False)
    title_photos= mydb.column(mydb.String(200), nullable=False)
    url = mydb.column(mydb.String(200), nullable=False)
    thambnailUrl= mydb.column(mydb.String(200), nullable=False)

    id_albums = mydb.column(mydb.Integer, mydb.ForeignKey('albums.id_albums'))
