// const promesse1=new Promise((resolu, rejected) =>{
//     const alea=Math.trunc(Math.random()*10)+1;
//     if(alea <= 5) {
//         resolu("Entre 1 et 5")
//     } else{
//         rejected("Entre 5 et 10!")
//     }
// })
// .then((txt)=>{
//     console.log(txt)
// })
// .catch((txt)=>{
//     console.log(txt)
// })
// function newPromise(){
//     return new Promise((resolve)=>{
//                 if(true){ resolve('ok !!')}
//         })
//     }
// async function opera(){
//     const attent=await newPromise()
//     console.log(attent)
// }
// opera()

// async function dogs(){
//     let response=await fetch('https://dog.ceo/api/breeds/image/random')
//     let data=await response.json()
//     console.log(data)
//     document.querySelector('img1').src=data.message
// }
// dogs()
var ligne=""
var dumper=document.getElementById('tbody')
dumper.innerHTML=''
fetch('http://localhost:5000/api/users/')
.then(response => response.json())
.then((datas) => {
    datas.forEach((data) => { 
    ligne+=`<tr>
                <td class='td id_td' text=${data.id}></td>
                <td class="no" id="pass"> <input type="checkbox" name="rowcheck" class="rowcheck"></td>
                <td class='td'>${data.fulname}</td>
                <td class='td'>${data.email}</td>
                <td class='td'>${data.phone}</td>
                <td class='td'>${data.website}</td>
                <td class="no">
                <input type="button" value="DELETE" class="buttonClasse">
                <input type="button" value="EDIT" class="buttonClasse EDITE">
                <input type="button" value="See More" class="buttonClasse">
                </td>
            </tr>`
    } )

///////////////////////////////////////////
/////////    //////////////////////
    // var tocheck= document.getElementsByClassName("rowcheck")
    // console.log(tocheck)

    // for(var i=0; i<tocheck.length; i++){
    //     console.log(i)

    //     if(tocheck[i].checked==true){
    //         console.log("checked")
    //     }
    //     // mycheck[i].onclick=function(){
    //     // var parent=this.parentElement.parentElement;   
    //     // var child=parent.querySelectorAll(".td")
    //     // }
    // }

/////////////////////////////////////////////
//////////////////////////////////////////////

dumper.innerHTML=ligne

var table=document.getElementById('tbody');
var cells=table.querySelectorAll('#tbody .td');
//console.log("hgfgfghf s",cells);
for(var i=0; i<cells.length; i++){
cells[i].onclick=function (){
   // console.log(this.innerText, this.hasAttribute('data-clicked'), this.hasAttribute('class'))
        
        if(this.hasAttribute('data-clicked')){
            return;
        }
        
        if(this.hasAttribute('value')){
            return;
        }
        if(this.hasAttribute('id')){
            return;
        }
        if(this.hasAttribute('text')){
            return;
        }
        
        this.setAttribute('data-clicked', 'yes')
        this.setAttribute('data-text', this.innerText)
        
        var input=document.createElement('input');
        input.setAttribute('type', 'text');
        input.value=this.innerText  ;
        input.style.width=this.clientWidth;
        input.style.height=this.clientHeight;
        input.style.fontFamily="inherit";
        input.style.border="0px";
        input.style.fontSize="inherit";
        input.style.textAlign="inherit";
        //input.style.backgroundColor="lightGoldenRodYellow";

        input.onblur=function(){
            var td = input.parentElement;
            var orig_text=input.parentElement.getAttribute('data-text');
            var current_text=this.value;
            
            if (orig_text==current_text){
                input.style.backgroundColor='inherit';
                input.value=orig_text; 
            }
        }
        this.innerText  ='';
        this.style.cssTxt='padding: 0px 0px';
        this.append(input);
        this.firstElementChild.select();     
    }
}
    //////////////////////////////////////////////
    /////////////  style for all elelments of a row ////////////
    /////////////////////////////////////////////

var table=document.getElementById("exemple");
var rows=document.getElementsByTagName("tr");
for(var i=1; i< rows.length-1;i++){
    currentRow = table.rows[i];
    currentRow.onclick=function(){
    Array.from(this.parentElement.children).forEach(element => {
        element.classList.remove('selected-row');
    });
    this.classList.add('selected-row');
    }   
}


/////////////////////////////////////////////
/////////// checkbox activated  ////////////
///////////////////////////////////////////
var mycheck=document.getElementsByClassName("rowcheck")
//console.log(mycheck)
for(var i=0; i<mycheck.length; i++){
    mycheck[i].onclick=function(){
    var parent=this.parentElement.parentElement;   
    var child=parent.querySelectorAll(".td")
    

    //console.log(i)

//////////////////////////deactive the other checkbox  /////////////////////////////////////////
   // console.log(this.checked)
    
    if(this.checked!=true){
        for(var j=0; j<mycheck.length; j++){
            mycheck[j].checked=false;  
    }
    }else{
        for(var j=0; j<mycheck.length; j++){
            mycheck[j].checked=false;          
    }
        this.checked=true;
    }
    //console.log(this.checked)


//////////////////////////                                   //////////////////////////////////
if(this.checked){   
for(var j=1; j<child.length; j++){
    //child[i].onclick=function (){
        if(this.hasAttribute('data-clicked')){
            return;
        }
        
        if(this.hasAttribute('value')){
            return;
        }
        if(this.hasAttribute('id')){
            return;
        }
        
        if(this.hasAttribute('text')){
            return;
        } 
            
            if(child[j].innerText){
                child[j].setAttribute('data-clicked', 'yes')
                child[j].setAttribute('data-text', child[j].innerText)
                var contenu=child[j].innerText
            }
            else{
               // contenu=child[j].parentElement.getAttribute('data-text')
               var contenu=child[j].getAttribute("data-text")
            }

            var input=document.createElement('input');
            
            input.setAttribute('type', 'text');
            input.value=contenu  ;
            input.style.width=child[j].clientWidth;
            input.style.height=child[j].clientHeight;
            input.style.fontFamily="inherit";
            input.style.border="0px";
            input.style.fontSize="inherit";
            input.style.textAlign="inherit";
            //input.style.backgroundColor="lightGoldenRodYellow";
    
            input.onblur=function(){
                var td = input.parentElement;
                var orig_text=input.parentElement.getAttribute('data-text');
                var current_text=this.value;
                
                if (orig_text==current_text){
                    input.style.backgroundColor='inherit';
                    input.value=orig_text; 
                }
            }
            child[j].innerText  ='';
            child[j].style.cssTxt='padding: 0px 0px';
            child[j].append(input);
            child[j].firstElementChild.select();
            
        //}
    }
}

/////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////
}
}

var ajout=document.getElementById("ajouter");
ajout.onclick=function(){
    document.querySelector(".popup").style.display='block';
}
var quit=document.getElementById("btnQuite");
quit.onclick=function(){
    document.querySelector(".popup").style.display='none';
}
var edits=document.querySelectorAll(".EDITE");
var pop= document.querySelector(".popup");

for(edit of edits){
    edit.onclick=function(){
        pop.style.display='block';

        var file=function(x,data){
            return [data[x].fulname, data[x].lastname, data[x].email, data[x].phone, data[x].website, data[x].adresse.city,
             data[x].adresse.street, data[x].adresse.suite, data[x].adresse.zipcode, data[x].adresse.geo.lat, data[x].adresse.geo.long, 
             data[x].compagny.name, data[x].compagny.bs, data[x].compagny.catchPhase ]
        }
        var nbpop=pop.querySelectorAll("input")
        var id=edit.parentElement.parentElement.firstElementChild.getAttribute("text")
        id=id-1;
        for(var i=0;i<nbpop.length;i++){
                nbpop[i].value=file(id, datas)[i]
                //console.log(el.value);

            }
            
    }
}

var submite=document.getElementById("btnSend");
submite.addEventListener('click',(e)=>{
    /////
        e.preventDefault()  // envoyer que sur ordre
        var data = {
            name: document.getElementById("fullname").value,
            username : document.getElementById("username").value,
            email : document.getElementById("email").value,
            phone : document.getElementById("phone").value,
            website : document.getElementById("website").value,
            street: document.getElementById("ville").value,
            suite: document.getElementById("rue").value,
            city: document.getElementById("suite").value,
            zipcode: document.getElementById("zipcode").value,
            lat: document.getElementById("lat").value,
            lng: document.getElementById("long").value,
            company_name: document.getElementById("compagny").value,
            catchphrase: document.getElementById("bs").value,
            bs: document.getElementById("catch").value
        }
        var id=edit.parentElement.parentElement.firstElementChild.getAttribute("text")
       

        fetch(`http://localhost:5000/api/users/${id}`,{
            method : 'PUT',
            headers:{
                'accept': 'application/json',
                'Content-Type' : 'application/json',
                
            },
            
            body : JSON.stringify(data)
        })
        pop.style.display='none';
        console.log(data)
        //window.location.href = '../templates/affiche_user.html'
    })



})
// console.log(ligne)

// var cells=table.querySelectorAll('#tbody td');
// console.log("hgfgfghf s",cells);
// for(var i=1; i<cells.length; i++){
// cells[i].onclick=function (){

//         if(this.hasAttribute('data-clicked')){
//             return;
//         }
//         if(this.hasAttribute('class')){
//             return;
//         }















//.then(data => document.querySelector('img').src=data.message)

// var eleve={
//     moyenne: function(){
//     var somme =0
//     for(var i=0; i<this.notes.length;i++){
//         somme +=this.notes[i]
//     }
//     return somme/this.notes.length
//     },
//     present: function(){
//         console.log(this.nom +"present")
//     }
// }
// var jean=Object.create(eleve)

// jean. nom='jean'
// jean.notes = [12,15]

// console.log(jean.present, jean.moyenne)
// var Eleve=function (nom){
//     this.nom=nom
// }

// Eleve.prototype.moyenne=function(){
//     var somme =0
//         for(var i=0; i<this.notes.length;i++){
//             somme +=this.notes[i]
//         }
//         return somme/this.notes.length
// }

// var jean=new Eleve('jean')





