function controles_logicos(){
    var nombre = document.getElementById('nombre').value
    var apellido = document.getElementById('apellido').value
    var direccion = document.getElementById('direccion').value
    const dni = document.getElementById('dni').value
    const fecha = document.getElementById('nacimiento').value

    var Faltante ="Faltan los sigientes datos: "
    if (nombre == "") {
        Faltante += " Nombre "
    }if (apellido == ""){
        Faltante += " Apellido "
    }if (direccion == ""){
        Faltante += " Direcion "
    }if (isNaN(dni)   ){
        Faltante += " Dni "
    }if ( fecha.trim() === '' ){
        Faltante += " Fecha "
    }

    if (Faltante != "Faltan los sigientes datos: "){        
        alert(Faltante)
    }

    var Invalido="Los sigientes datos son invalido: "
    if (es_String_Sin_Numero(nombre)) {
        Invalido += " Nombre "
    }if ( es_String_Sin_Numero(apellido)){
        Invalido += " Apellido "
    }if ( typeof dni != "number"){
        Invalido += " Dni "
    }

    alert(Invalido)
}

function es_String_Sin_Numero(variable){
    if (typeof variable){
        return false
    }

    const contieneNumero = /\d/.test(variable)
    return !contieneNumero
}