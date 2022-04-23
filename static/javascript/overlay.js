var overlay=document.querySelector('.divOverlay')
var button=document.querySelector('#ajouter')
var btnquit=document.querySelector('#btnQuite')

button.addEventListener("click",()=>{
    overlay.classList.add('show')
})
btnquit.addEventListener("click",()=>{
    overlay.classList.remove('show')
})