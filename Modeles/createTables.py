from tokenize import Number
from connexion import Base
from sqlalchemy import Column, PrimaryKeyConstraint,String,Integer,Float



class Adresse(Base):
    __tablename__='Adresse'
    id_add=Column(Integer,PrimaryKey=True)
    stree=Column(String(250),nullable=False)
    suite=Column(String(250),nullable=False)
    city=Column(String(250),nullable=False)
    zipcode=Column(String(250),nullable=False)
    longitude=Column(Float,nullable=False)
    latitude=Column(Float,nullable=False)

class Compagny(Base):
    __tablename__='Compagny'
    id_comp=Column(Integer,PrimaryKey=True)
    name_comp=Column(String(250),nullable=False)
    catch_phrase=Column(String(250),nullable=False)
    bs=Column(String(250),nullable=False)

class User(Base):
    __tablename__='User'
    id_user=Column(Integer,PrimaryKey=True)
    name_user=Column(String(250),nullable=False)
    username=Column(String(250),nullable=False,unique=True)
    email=Column(String(250),nullable=False,unique=True)
    phone=Column(String(50),nullable=False)
    website=Column(String(100))
    
    class Posts(Base):
     __tablename__='Posts'
    id_posts=Column(Integer,PrimaryKey=True)
    title=Column(String(100),nullable=False)
    body=Column(String(100),nullable=False)
    city=Column(String(250),nullable=False)
    
class Todos(Base):
    __tablename__='Todods'
    id_todos=Column(Integer,PrimaryKey=True)
    title=Column(String(100),nullable=False)

class Albums(Base):
    __tablename__='Albums'
    id_albums=Column(Integer,PrimaryKey=True)
    title=Column(String(100),nullable=False)
    
    



