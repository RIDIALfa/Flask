let url= "http://localhost:5000//api/utilisateur/"


 var el=document.querySelector('#submit').addEventListener('click', (e)=>{
    //  e.preventDefault()
    var email=document.getElementById("mail").value
    var pass=document.getElementById("passwd").value
    var error=document.getElementById("msg")

    async function getApi(email){
        
        let response=await fetch(url+email)
        let data=await response.json()

if(email==""|| pass==""){
    error.innerHTML="veuillez remplir les champs"
    error.style.color="red"
}
else{

    if( Object.keys(data).length>0){
          if (pass==data.password){
            //   window.location.pathname='/'
            console.log('cool');
            }
         else{
                error.innerHTML="mot de passe incorrect"
                 error.style.color="red"

             }
         }
    else{
            error.innerHTML="l'utilisateur ou le  mot passe  n existe pas"
            error.style.color="red"

        }
    }
       
 }

    getApi(email)
})

