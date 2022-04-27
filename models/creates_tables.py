from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe3:passer123@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = "users"
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username % self.email


class Posts(db.Model):
    __tablename__ = "posts"
    postId = db.Column(db.Integer, primary_key=True)
    title_post = db.Column(db.String(80), nullable=False)
    body_post = db.Column(db.Text, nullable=False)
    userId_post = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Posts %r>' % self.title_post


class Comments(db.Model):
    __tablename__ = "comments"
    commentId = db.Column(db.Integer, primary_key=True)
    name_comment = db.Column(db.String(100), nullable=False)
    email_comment = db.Column(db.String(80), nullable=False)
    body_comment = db.Column(db.Text, nullable=False)
    postId_comment = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Comments %r>' % self.name_comment 


class Albums(db.Model):
    __tablename__ = "albums"
    albumId = db.Column(db.Integer, primary_key=True)
    title_album = db.Column(db.String(100), nullable=False)
    userId_album = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Albums %r>' % self.title_album



class Photos(db.Model):
    __tablename__ = "photos"
    photoId = db.Column(db.Integer, primary_key=True)
    title_photo = db.Column(db.String(100), nullable=False)
    url_photo = db.Column(db.String(100), nullable=False)
    thumnail_photo = db.Column(db.String(100), nullable=False)
    albumId_photo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Albums %r>' % self.title_photo


class Todos(db.Model):
    __tablename__ = "todos"
    todoId = db.Column(db.Integer, primary_key=True)
    title_todo = db.Column(db.String(100), nullable=False)
    etat_todo = db.Column(db.Integer, nullable=False)
    userId_todo = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Todos %r>' % self.title_todo



if __name__=='__main__':
    db.create_all()