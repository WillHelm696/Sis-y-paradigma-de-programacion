//****************************
//INICIAR SECION
//****************************
function inisiar_secion(){
    const msj=document.getElementById("mensaje")
    const data={
        user:document.getElementById("user").value,
        pasw:document.getElementById("pasw").value
    }
    let rta = ""

    if (data.user === "" ){
        rta+="Usuario No ingresado <br>"
    }if (data.pasw === "" ){
        rta+="Contraseña no ingresado <br>"
    }if (rta.length > 0){
        msj.innerHTML = rta
        return 
    }
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },success: function(respuesta){
            if (respuesta.success ){
                window.location.href= "/temperaturas"
            }else{
                msj.innerHTML=respuesta.mensaje
            }
        },error: function(error){
            msj.innerHTML = "Error al iniciar sesion" + error
        }
    })
}
//****************************
//AGREGAR TEMPERATURA
//****************************
function Agregar_temperatura(){
const msj = document.getElementById("mensaje")
    const tempInput = document.getElementById('temperatura')
    if (!tempInput){
        msj.innerHTML = "Elemento de temperatura no encontrado en la página."
        return
    }
    const data = { temperatura: parseFloat(tempInput.value) }

    if (isNaN(data.temperatura)){
        msj.innerHTML = "Ingrese un número válido"
        return
    }
    $.ajax({
        type: 'POST',
        url: '/agregar_temperatura',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },success: function(respuesta){
            if (!respuesta.success){
                alert(respuesta.mensaje)
                window.location.href= "/"
            }
            msj.innerHTML = respuesta.mensaje
        },error: function(error){
            msj.innerHTML = "Error al iniciar sesion" + error
        }
    })
}
//****************************
//CALCULAR PROMEDIO
//****************************
function Mostrar_promedio(){
    const msj=document.getElementById("mensaje")
    $.ajax({
        type: 'POST',
        url: '/mostrar_promedio',
        data: JSON.stringify({}),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },success: function(respuesta){
            if (!respuesta.success){
                alert(respuesta.mensaje)
                window.location.href= "/"
            }
            msj.innerHTML=respuesta.mensaje
        },error: function(error){   
            msj.innerHTML = "Error al iniciar sesion" + error
        }
    })
}