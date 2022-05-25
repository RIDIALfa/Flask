from flask import render_template
from models.create_tables import Todos, Users


# ############################
# #############AWA############
# ############################

def visualisation():
        
    users=Users.query.all()
    todos=Todos.query.all()
    status=[]
    listuser=[]
    listpost=[]
    length_afaire = 0
    length_termine = 0
    length_encours = 0
    for todo in todos:
        if todo.status==1:
            length_afaire+=1
        elif todo.status==2:
            length_encours+=1
        elif todo.status==3:
            length_termine+=1

    nb_status=[length_afaire,length_encours,length_termine]
    for user in users:
        listuser.append(user.username)
        listpost.append(len(user.posts))

    return render_template('pages/viz.html', listuser=listuser,listpost=listpost,nb_status=nb_status,status=status)






# ############################
# #############KHABS##########
# ############################
def dataViz():
    listename=[]
    listepost=[]
    users=Users.query.all()
    # posts=Posts.query.all()
    for user in users:
        listename.append(user.username)
        listepost.append(len(user.posts))
    
    liste=['users','posts']
    val=[listename, listepost]

    todos=Todos.query.all()
    todosValue=[0,0,0]
    listeValue=["A faire", "Terminer", "En cour"]
    for todo in todos:
        if todo.status==1:
            todosValue[0]+=1
        elif todo.status==2:
            todosValue[1]+=1
        else: 
            todosValue[2]+=1
    

    return render_template('pages/dataViz.html', listename=listename, listepost=listepost)