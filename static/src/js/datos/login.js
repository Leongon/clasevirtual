var form = document.getElementById("form");
var alertdanger = document.getElementsByClassName("alert")

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

form.addEventListener('submit', function (e) {
    e.preventDefault();
    var datos = new FormData(form);
    var datojson = { "usuario": datos.get("email"), "pass": datos.get("pass") }
    console.log(datojson)
    axios({
        method: 'POST',
        url: '/apiLogin',
        data: datojson
    })
        .then(res => {
            console.log(res.data)
            if (res.data === "Bienvenido") {
                $(".alert").html('<div class="flex items-center bg-green-50 text-center"> <svg xmlns="http://www.w3.org/2000/svg"     class="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"     viewBox="0 0 24 24" stroke="currentColor">      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"         d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path> </svg>  <div class="flex flex-col ml-3"> <div class="font-medium leading-none">Bienvenidos</div>  </div>  </div>')  
            } else {
                $(".alert").html('<div class="flex items-center bg-red-400 text-center"> <svg xmlns="http://www.w3.org/2000/svg"     class="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"     viewBox="0 0 24 24" stroke="currentColor">      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"         d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path> </svg>  <div class="flex flex-col ml-3"> <div class="font-medium leading-none">Contraseña o usuario incorrecto</div>  </div>  </div>') 
            }
        })

})
