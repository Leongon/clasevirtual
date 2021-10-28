var form=document.getElementById("form_login");

/*
form.addEventListener("submit",function(e){
    
    e.preventDefault();
    var datos=new FormData(form);
    var datojson=JSON.stringify({"usuario":datos.get("inputuser"),"pass":datos.get("inputPassword")})
    console.log(datojson);

    fetch('/apiLogin',{
        method:'POST',
        headers:{'Accept' : 'application/json',
                'Content-Type':'application/json'},
        body:datojson
    })

    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })

})
*/

form.addEventListener('submit',function(e){
    e.preventDefault();
    var datos=new FormData(form);
    var datojson={"usuario":datos.get("inputuser"),"pass":datos.get("inputPassword")}
    axios({
        method:'POST',
        url:'/apiLogin',
        data: datojson
    })
    .then(res=>console.log(res.data))
    
})
