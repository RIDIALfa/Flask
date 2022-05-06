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


// *************************************
// *******LOAD FORM BLOCK REFRESH*******
// *************************************

// $("#formLoad").on('submit', (e)=>{
//     $.ajax({
//         data : {
//             nombre : $('#inputNumber').val(),
//         },
//         type : 'POST',
//         url : '/'
//     })
//     .done((data) => {
//         if (data.error) {
//             console.error('Bakhoul')
//         }
//         else {

//             $('#inputNumber').val('')
//             console.log(data.users)
//             setTimeout(function(){
//                 $( "#tableHome" ).load('#tableHome');
//              }, 10); 
//         }
//     });
//     e.preventDefault()
// })


