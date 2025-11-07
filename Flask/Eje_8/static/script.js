function Enviar_mensaje(respuesta){
    let mensaje = (document.getElementById('mensaje'))
    mensaje.innerHTML = respuesta
}

function notas_materia(){
    return {
        'nota1':parseInt(document.getElementById('nota1').value),
        'nota2':parseInt(document.getElementById('nota2').value),
        'nota3':parseInt(document.getElementById('nota3').value),
        'nota4':parseInt(document.getElementById('nota4').value),
        'nota5':parseInt(document.getElementById('nota5').value)
    }
    
}

function informacion_personal(){
    return {
        'nombre' : document.getElementById('nombre').value,
        'apellido' : document.getElementById('apellido').value,
        'fecha' : parseInt(document.getElementById('fecha').value),
        'dni' : parseInt(document.getElementById('dni').value)
    }
}

function datos_completos(solicitud){    
    let notas = notas_materia()
    let datos = informacion_personal()

    let respuesta = "";
    
    
    if (!datos.nombre){
        respuesta += "Falta colocar Nombre <br>"
    }if (!datos.apellido){
        respuesta += "Falta colocar Apellido <br>"
    }if (isNaN(datos.fecha)){
        respuesta += "Fala colocar Fecha <br>"
    }if (isNaN(datos.dni)){
        respuesta += "Falta colocar dni <br>"
    }if ( isNaN(notas.nota1) || isNaN(notas.nota2) || isNaN(notas.nota3) || isNaN(notas.nota4) || isNaN(notas.nota5)){
        respuesta += "Complete el campo de notas"
    }

    if (isNaN(respuesta ) === true){
        Enviar_mensaje(respuesta)
        return
    }if (solicitud==="1"){
        return notas
    }if (solicitud === "2"){
        return datos
    }
}


function calcular(){
    notas = datos_completos("1")

    if (!notas){
        return
    }else{
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/promedio_nota",
            data:JSON.stringify(notas),
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            success: function(respuesta){
                let html  =
                `Promedio de Nota:${respuesta.promedio} <br>
                 Mayror Nota ${respuesta.mayor} <br>                
                `;
            Enviar_mensaje(html)

            },
            error: function (){
                alert("Error al comunicarse con el servidor");
            } 
        })        
    }
    
}


function verificar() {
    informacion = datos_completos("1")

    if (isNaN(informacion)){
        return
    }else{
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/veridicar_adultes",
            data:JSON.stringify(informacion),
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            succes: function(respuesta){

                
                
            },
            error: function (){
                alert("Error al comunicarse con el servidor");
            } 
        })
    }
}
