var formlogin = document.getElementById("form");

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

function login () {
    var datos = new FormData(formlogin);
    var datojson = { "usuario": datos.get("email"),"pass": datos.get("pass") }
    console.log(datojson)
    axios({
        method: 'POST',
        url: '/apiLogin',
        data: datojson
    })
        .then(res => {
            console.log(res.data)
            if (res.data === "No existe el usuario o la contraseña es incorrecta") {
               $(".alert").html('<div class="alert-desvanece flex items-center bg-red-400 text-center"> <svg xmlns="http://www.w3.org/2000/svg"     class="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"     viewBox="0 0 24 24" stroke="currentColor">      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"         d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path> </svg>  <div class="flex flex-col ml-3"> <div class="font-medium leading-none">'+res.data+'</div>  </div>  </div>') 
                setTimeout(function(){
                  $(".alert-desvanece").fadeOut(500,function(){
                      $(this).remove();
                  });
              },3000);
                
            } else {
               $(".alert").html('<div>'+res.data+'</div>')  
            }
        })
}

$.validator.setDefaults( {
    submitHandler: function () {
       login()
    }
 });
 $(document).ready(function(){
    $('#form').validate({
       rules: {
          email: {
             required: true
          },
          pass: {
             required: true,
                
          },
        
          agree: "required"
       },
       messages: {
          email: {
             required: "ingrese su usuario",
          },
          
          pass: {
             required: "Por favor ingresa una contraseña",
             minlength: "Tu contraseña debe ser de no menos de 5 caracteres de longitud"
          },
          
       },
       errorElement: "em",
       errorPlacement: function (error, element) {
          // Add the `help-block` class to the error element
          error.addClass("help-block");
 
          if (element.prop( "type" ) === "checkbox") {
             error.insertAfter(element.parent("label") );
          } else {
             error.insertAfter(element);
          }
       }
    });
 });

 

