var formRe = document.getElementById("form_registro");
/*USUARIO*/
$(document).ready(function () {
    $("#Usuario").keyup(function () {
        var texto_escrito = $(this).val();
        console.log($(":text#Usuario").val().length)
        if($(":text#Usuario").val().length>=5){
            var datos = new FormData(formRe);
            var datojson = { "usuario": datos.get("Usuario") }
            axios({
                method: 'POST',
                url: '/apiSearchUsuario',
                data: datojson
            })
            .then(res => {
                    console.log(res.data.msj)
                    if (res.data.msj==="ok") {
                        $(".prob_usu").html('<label style="color:green">El usuario esta disponible </label>')
                        $(".conU").removeClass("cursor-not-allowed");
                        $('.conU').removeAttr('disabled');
                    } else {
                        $(".prob_usu").html('<label style="color:red">'+res.data.msj+'</label>')
                        $(".conU").addClass("cursor-not-allowed");
                        $('.conU').prop('disabled', true);
                }
            })
        }else{
            $(".prob_usu").html('<label style="color:red"></label>')
            $(".conU").addClass("cursor-not-allowed");
            $('.conU').prop('disabled', true);
        }
    })
})

/*Correo*/
$(document).ready(function () {
    $("#email").keyup(function () {
        var email=document.getElementById("email").value;
            var expReg= /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
            var esValido=expReg.test(email);
            console.log(esValido)
            if(esValido==true){
                console.log("valido")
                var datos = new FormData(formRe);
                var datojson = { "correo": datos.get("email") }
                axios({
                method: 'POST',
                url: '/apiSearchCorreo',
                data: datojson
            })
            .then(res => {
                    console.log(res.data.msj)
                    if (res.data.msj==="ok") {
                        $(".prob_co").html('<label style="color:green">El correo esta disponible</label>')
                        $(".conL").removeClass("cursor-not-allowed");
                        $('.conL').removeAttr('disabled');
                    } else {
                        $(".prob_co").html('<label style="color:red">'+res.data.msj+'</label>')
                        $(".conL").addClass("cursor-not-allowed");
                        $('.conL').prop('disabled', true);
                }
            })
        }else{
            $(".prob_co").html('<label style="color:green"></label>')
            $(".conL").addClass("cursor-not-allowed");
            $('.conL').prop('disabled', true);
        }
        
    })
})

/*Telefono */
$(document).ready(function () {
    $("#tel").keyup(function () {

        console.log($(":text#tel").val().length)
        if($(":text#tel").val().length==9){
            var datos = new FormData(formRe);
            var datojson = { "telefono": datos.get("tel") }
            console.log(datojson)
            axios({ 
                method: 'POST',
                url: '/apiSearchTelefono',
                data: datojson
            })
            .then(res => {
                    console.log(res.data.msj)
                    if (res.data.msj==="ok") {
                        $(".prob_tel").html('<label style="color:green">El Numero cel esta disponible</label>')
                        $(".conT").removeClass("cursor-not-allowed");
                        $('.conT').removeAttr('disabled');
                    } else {
                        $(".prob_tel").html('<label style="color:red">'+res.data.msj+'</label>')
                        $(".conU").addClass("cursor-not-allowed");
                        $('.conU').prop('disabled', true);
                    }
                    
            })
        }else{
            $(".prob_tel").html('<label style="color:red"></label>')
            $(".conU").addClass("cursor-not-allowed");
            $('.conU').prop('disabled', true);
        }


    })
})

/*registrar*/

function registro () {
    var datos = new FormData(formRe);
    var datojson = { "usuario": datos.get("Usuario"), "pass": datos.get("pass"), "nombres": datos.get("Nombre"), "apellidos": datos.get("Apellido"), "correo": datos.get("email"),"telefono": datos.get("tel")}
    console.log(datojson)
    axios({
        method: 'POST',
        url: '/apiRegistro',
        data: datojson
    })
        .then(res => {
            console.log(res.data)
            if (res.data === "Registro correcto") {
                $(".alert").html('<div class="flex items-center bg-green-50 text-center"> <svg xmlns="http://www.w3.org/2000/svg"     class="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"     viewBox="0 0 24 24" stroke="currentColor">      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"         d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path> </svg>  <div class="flex flex-col ml-3"> <div class="font-medium leading-none">'+res.data+'</div>  </div>  </div>')  
                window.location.href = "/login";
            } else {
                $(".alert").html('<div class="flex items-center bg-red-400 text-center"> <svg xmlns="http://www.w3.org/2000/svg"     class="w-16 h-16 rounded-2xl p-3 border border-blue-100 text-blue-400 bg-blue-50" fill="none"     viewBox="0 0 24 24" stroke="currentColor">      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"         d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path> </svg>  <div class="flex flex-col ml-3"> <div class="font-medium leading-none">'+res.data+'</div>  </div>  </div>') 
            }
        })
}

$.validator.setDefaults({
    submitHandler: function () {
        registro ()
    }
});
$(document).ready(function () {
    $('#form_registro').validate({
        rules: {

            Nombre: {
                required: true,


            },
            Apellido: {
                required: true
            },
            tel: {
                required: true,
                number: true,
                rangelength: [9, 9]
            },
            email: {
                required: true,
                email:true

            },
            Usuario: {
                required: true,
                minlength: 5
            },
            pass: {
                required: true,
                minlength: 6,
            },
            pass_confirmar: {
                required: true,
                minlength: 6,
                equalTo: "#pass"
            },
            agree: "required"
        },
        messages: {
            Nombre: {
                required: "Por favor llene sus Nombres",
            },
            Usuario: {
                required: "Por favor llene el campo Usuario",
                minlength: "Tu Usuario debe se mayor de 5 caracteres de longitud"
            },
            Apellido: {
                required: "Por favor llene sus Apellidos",
            },
            tel: {
                required: "ingrese su numero celular",
                number: "Solo acepta numeros ",
                rangelength: " ingrese su numero celular de 9 digitos"
            },

            email: {
                required: "ingrese su Correo electronico",
                email: "Correo electronico invalido"
            },

            pass: {
                required: "Por favor ingresa una contraseña",
                minlength: "Tu Contraseña debe se mayor de 6 caracteres de longitud"
            },
            pass_confirmar: {
                required: "Ingresa un password",
                minlength: "Tu Contraseña debe se mayor de 6 caracteres de longitud",
                equalTo: "Por favor ingresa la misma contraseña de arriba"
            },


        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            // Add the `help-block` class to the error element
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        }
    });
});


