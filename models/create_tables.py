from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask import Flask

# configurations syst
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://groupe3:passer123@localhost/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# creating database connection
mydb=SQLAlchemy(app)

class adresse(mydb.Model):
    __tablename__='adresse'
    users_id = relationship("users", backref="adresse")
    id_addresse = mydb.Column(mydb.Integer, primary_key=True)
    street = mydb.Column(mydb.String(200))
    suite = mydb.Column(mydb.String(200))
    city = mydb.Column(mydb.String(200))
    zipcode = mydb.Column(mydb.String(100))
    lat = mydb.Column(mydb.String(50))
    long = mydb.Column(mydb.String(50))

class company(mydb.Model):
    users = relationship("users", backref="company")
    id_company = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(200))
    catchPhrase = mydb.Column(mydb.String(250))
    bs = mydb.Column(mydb.String(200))
class users(mydb.Model):
    __tablename__='users'
    id_users = mydb.Column(mydb.Integer, primary_key=True)
    userName = mydb.Column(mydb.String(200))
    Email = mydb.Column(mydb.String(200))
    phone = mydb.Column(mydb.String(50))
    website = mydb.Column(mydb.String(200))

    # users childreen relations
    posts = relationship("posts", backref="users")
    todos = relationship("todos", backref="users")
    albums = relationship("albums", backref="users")
    
    # users parents relations
    id_adresse = mydb.Column(mydb.Integer, mydb.ForeignKey('adresse.id_adresse'))
    id_company = mydb.Column(mydb.Integer, mydb.ForeignKey('company.id_company'))
    
class posts(mydb.Model):
    __tablename__='posts'
    id_posts = mydb.Column(mydb.Integer, primary_key=True)
    title_posts = mydb.Column(mydb.String(200))
    body = mydb.Column(mydb.String(200))

    comments = relationship("comments")

    id_users = mydb.Column(mydb.Integer, mydb.ForeignKey('users.id_users'))

class comments(mydb.Model):
    __tablename__='comments'
    id_comments = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(200))
    Email = mydb.Column(mydb.String(100))
    body = mydb.Column(mydb.String(200))

    id_posts = mydb.Column(mydb.Integer, mydb.ForeignKey('posts.id_posts'))

class todos(mydb.Model):
    __tablename__='todos'
    id_todos = mydb.Column(mydb.Integer, primary_key=True)
    title_todos= mydb.Column(mydb.String(200))

    id_users = mydb.Column(mydb.Integer, mydb.ForeignKey('users.id_users'))

class albums(mydb.Model):
    __tablename__='albums'
    id_albums = mydb.Column(mydb.Integer, primary_key=True)
    title_albums= mydb.Column(mydb.String(200))

    photos= relationship("photos")

class photos(mydb.Model):
    __tablename__="photos"
    id_photos = mydb.Column(mydb.Integer, primary_key=True)
    albums = mydb.Column(mydb.String(200))
    title_photos= mydb.Column(mydb.String(200))
    url = mydb.Column(mydb.String(200))
    thambnailUrl= mydb.Column(mydb.String(200))

    id_albums = mydb.Column(mydb.Integer, mydb.ForeignKey('albums.id_albums'))


if __name__=='__main__':
    mydb.create_all()
 