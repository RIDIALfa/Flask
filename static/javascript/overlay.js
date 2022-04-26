var overlay = document?.querySelector('.divOverlay')
var button = document?.querySelector('#ajouter')
var btnquit = document?.querySelector('#btnQuite')
var formLoad = document?.querySelector('#formLoad')
var inputNumber = document?.querySelector('#inputNumber')

button && button.addEventListener("click",()=>{
    overlay.classList.add('show')
})
btnquit && btnquit.addEventListener("click",()=>{
    overlay.classList.remove('show')
})


inputNumber && inputNumber.addEventListener('focusout',(e)=>{
    let value = e.target.value

    if( value < 1 || value > 5){
        e.target.value = '' 
    }
})


formLoad && formLoad.addEventListener('submit',(e)=>{
    e.preventDefault()
})
