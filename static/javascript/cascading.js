Delete = function(x){
    console.log("delete")
    x.parentNode.parentNode.parentNode.remove()
}
var table=document.getElementById("postTable")
var table_nb=document.getElementById('tbody').childElementCount
console.log(table_nb)