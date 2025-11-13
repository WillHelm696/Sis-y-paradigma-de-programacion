function datos(){
    return {
        cuit : parseInt(document.getElementById("cuit").value),
        nombre : document.getElementById("nombre").value.trim(),
        apellido : document.getElementById("apellido").value.trim(),
        inmueble : parseInt(document.getElementById("inmueble").value),
        valor : parseFloat(document.getElementById("valor").value)
    };
}

function verificar(objDatos){
    let respuesta = '';
    let mensaje = document.getElementById("mensaje");

    if (isNaN(objDatos.cuit)) respuesta += "Ingrese CUIT <br>";
    if (!objDatos.nombre) respuesta += "Ingrese Nombre <br>";
    if (!objDatos.apellido) respuesta += "Ingrese Apellido <br>";
    if (isNaN(objDatos.inmueble)) respuesta += "Ingrese Nº de Inmueble <br>";
    if (isNaN(objDatos.valor)) respuesta += "Ingrese Valor del Inmueble <br>";

    if (respuesta !== '') {
        mensaje.innerHTML = respuesta;
        return false;
    }

    mensaje.innerHTML = '';
    return true;
}

function impuesto(){
    let objDatos = datos();
    if (!verificar(objDatos)) return;

    $.ajax({
        type: 'POST',
        url: "/calcular_impuesto",
        data: JSON.stringify(objDatos),
        headers: {
            'Accept':'application/json',
            'Content-Type':'application/json'
        },
        success: function(respuesta){
            alert("Impuesto calculado: " + respuesta.impuesto);
        },
        error: function(){
            alert("Error al comunicarse con el servidor");
        }
    });
}

function promedio(){
    let objDatos = datos();
    if (!verificar(objDatos)) return;

    $.ajax({
        type: 'POST',
        url: "/calcular_promedio_propiedades",
        data: JSON.stringify(objDatos),
        headers: {
            'Accept':'application/json',
            'Content-Type':'application/json'
        },
        success: function(respuesta){
            alert("Promedio: " + respuesta.promedio);
        },
        error: function(){
            alert("Error al comunicarse con el servidor");
        }
    });
}
