from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from main import app
from sqlalchemy.orm import relationship

# configurations syst

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://groupe3:passer123@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# creating database connection
db = SQLAlchemy(app)

class adresse(db.Model):
    __tablename__='adresse'
    users_id = relationship("users", backref="adresse")
    id_addresse = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(200), nullable=False)
    suite = db.column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    zipcode = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.String(50), nullable=False)
    long = db.Column(db.String(50), nullable=False)





class company(db.Model):
    users = relationship("users", backref="company")
    id_company = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    catchPhrase = db.column(db.String(200), nullable=False)
    bs = db.Column(db.String(200), nullable=False)





class users(db.Model):
    __tablename__='users'
    id_users = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(200), nullable=False)
    Email = db.column(db.String(200), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    website = db.Column(db.String(200), nullable=False)

    # users childreen relations
    posts = relationship("posts", backref="users")
    todos = relationship("todos", backref="users")
    albums = relationship("albums", backref="users")
    
    # users parents relations
    id_adresse = db.column(db.Integer, db.ForeignKey('adresse.id_adresse'))
    id_company = db.column(db.Integer, db.ForeignKey('company.id_company'))




    
class posts(db.Model):
    __tablename__='posts'
    id_posts = db.Column(db.Integer, primary_key=True)
    title_posts = db.Column(db.String(200), nullable=False)
    body = db.column(db.String(200), nullable=False)

    comments = relationship("comments")

    id_users = db.column(db.Integer, db.ForeignKey('users.id_users'))




class comments(db.Models):
    __tablename__='comments'
    id_comments = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    Email = db.column(db.String(100), nullable=False)
    body = db.column(db.String(200), nullable=False)

    id_posts = db.column(db.Integer, db.ForeignKey('posts.id_posts'))




class todos(db.Models):
    __tablename__='todos'
    id_todos = db.Column(db.Integer, primary_key=True)
    title_todos= db.column(db.String(200), nullable=False)

    id_users = db.column(db.Integer, db.ForeignKey('users.id_users'))


    

class albums(db.Models):
    __tablename__='albums'
    id_albums = db.Column(db.Integer, primary_key=True)
    title_albums= db.column(db.String(200), nullable=False)

    photos= relationship("photos")




class photos(db.Models):
    __tablename__="photos"
    id_photos = db.Column(db.Integer, primary_key=True)
    albums = db.column(db.String(200), nullable=False)
    title_photos= db.column(db.String(200), nullable=False)
    url = db.column(db.String(200), nullable=False)
    thambnailUrl= db.column(db.String(200), nullable=False)

    id_albums = db.column(db.Integer, db.ForeignKey('albums.id_albums'))
