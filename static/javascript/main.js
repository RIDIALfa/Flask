// DECLARATION DES VARIABLES
let userContainer = document.querySelector(".userContainer")
let bars = document.querySelector("#bars")
let btnQuite = document.querySelector("#btnQuite")

let divOverlayPostForm = document.querySelector(".divOverlay")
let btnPostForm = document.querySelector(".btnForm")


// LES EVENEMENTS
// && permet de verifier si la variable est != de null
btnPostForm && btnPostForm.addEventListener('click', ()=>{
    divOverlayPostForm.classList.add('show')
})

btnPostForm && btnQuite.addEventListener('click', ()=>{
    divOverlayPostForm.classList.remove('show')
})

// DEPLACER LE FORMULAIRE
divOverlayPostForm && userContainer.insertBefore(divOverlayPostForm, bars)



// GERER LE LIEN ACTIVE
let ulLinks = document.querySelectorAll(".ulLinks li")
let linkUser = document.querySelector(".ulLinks li.user")
let linkPosts = document.querySelector(".ulLinks li.posts")
let linkAlbums = document.querySelector(".ulLinks li.albums")
let linkTodos = document.querySelector(".ulLinks li.todos")

for(let li of ulLinks){
    if(li.classList.contains('active')){
        li.classList.remove('active')
    }
}

let pathname = window.location.pathname

switch(pathname){

    case '/posts/':
    case '/post/':
        linkPosts.classList.add('active')
        break

    case '/albums/':
    case '/album/':
        linkAlbums.classList.add('active')
        break
    
    case '/todos/':
        linkTodos.classList.add('active')
        break

    default:
        linkUser.classList.add('active')
        console.log("pas dans todo")
}