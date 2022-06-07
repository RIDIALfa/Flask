var ligne=""
var dumper=document.getElementById('tbody')
dumper.innerHTML=''

fetch('http://localhost:5000/api/todos/')
.then(response => response.json())
.then((datas) => {
    datas.forEach((data) => { 
    ligne+=`<tr key=${data.id}>
                <td class="no" id="pass"> <input type="checkbox" name="rowcheck" class="rowcheck"></td>
                <td class='td' id='title'>${data.title_todos}</td>
                <td class='td' id='status'>${data.status}</td>
                <td class="but_modif">
                <input type="button" value="EDITE" class="buttonClasse">
                <input type="button" value="Modifier" class="buttonClasse">
                <input type="button" value="DELETE" id="delete" class="buttonClasse" >
                </td>
            </tr>`

    } )
dumper.innerHTML=ligne
var table=document.getElementById('tbody');
var bouton=table.querySelectorAll('#tbody #delete');
var table=document.getElementById('tbody');
var el=table.querySelectorAll('#tbody .td');

bouton.addEventListener('click',()=>{
    fetch(`http://localhost:5000/api/todos/${id}`,{
    method:'DELETE'

})
    
})
for(i of el){
    i.addEventListener('click',(e)=>{
        id = Number(e.target.parentElement.getAttribute('key'))

}
)}




var table=document.getElementById('tbody');
var ele=table.querySelectorAll('#tbody .td');
for (i of ele){
    i.addEventListener('click',(e)=>{
        td = e.target
        contenu = td.innerText

        td.innerText=''
        var input=document.createElement("input")
        td.replaceWith(input)
        input.style.marginLeft="45%"
        input.value=contenu
        key=td.getAttribute("id");

        input.addEventListener('mouseout',(e)=>{
            let val = e.target.value 
            input.replaceWith(td)
           td.innerText = val
           valeur=td.innerText;
           id=td.parentElement.getAttribute("key");

           new_dict={}
           new_dict[`${key}`]=valeur
           fetch(`http://localhost:5000/api/todo/${id}`,{
            method : 'PUT',
            headers:{
                "Content-type":'application/json'
            },
            body:JSON.stringify( 
                new_dict
            )
                
            
        
        })
        
        

         })
        
         
    })
}

})

