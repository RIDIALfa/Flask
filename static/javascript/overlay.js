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





// *****************************
// INNER TEXT FOR TEXTAREA EDIT
// *****************************
let elementTextarea = document?.querySelector('.divUpdated textarea')
if (elementTextarea){
    elementTextarea.innerText = elementTextarea.getAttribute("content")
}


// *********************************
// DEFAULT VALUE SELECT OPTION TODOS
// *********************************
let elementSelect = document?.querySelector('.divUpdated .selectOptions')
let options = document?.querySelectorAll('.divUpdated .selectOptions option')
if (elementSelect){
    let selectValue = elementSelect.getAttribute('select')
    for(let option of options){
        if(option.value == selectValue){
            option.setAttribute('selected', 'selected')
        }
    }
}






// *******************************************************
// ********DESACTIVE LE LINK CHARGER AU PREMIER CLICK*****
// *******************************************************
let loadPosts = document?.querySelector('#loadPosts')
loadPosts && loadPosts.addEventListener('click', () => {
    loadPosts.classList.add('clicked')
    loadPosts.style.display = 'none'
})