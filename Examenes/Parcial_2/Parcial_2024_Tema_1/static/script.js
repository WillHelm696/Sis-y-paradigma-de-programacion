function obtenerDatos() {
    return {
        dni: document.getElementById("dni").value.trim(),
        nombre: document.getElementById("nombre").value.trim(),
        apellido: document.getElementById("apellido").value.trim(),
        ingresos: parseFloat(document.getElementById("ingresos").value),
        valor_auto: parseFloat(document.getElementById("valor_auto").value)
    };
}

function validarDatos(datos) {
    let mensaje = "";

    if (!datos.dni) mensaje += "Ingrese DNI.<br>";
    if (!datos.nombre) mensaje += "Ingrese Nombre.<br>";
    if (!datos.apellido) mensaje += "Ingrese Apellido.<br>";
    if (isNaN(datos.ingresos) || datos.ingresos <= 0) mensaje += "Ingrese un valor válido de ingresos.<br>";
    if (isNaN(datos.valor_auto) || datos.valor_auto <= 0) mensaje += "Ingrese un valor válido de auto.<br>";

    if (mensaje !== "") {
        document.getElementById("resultado").innerHTML = mensaje;
        return false;
    }
    document.getElementById("resultado").innerHTML = "";
    return true;
}

function calcularCredito() {
    let datos = obtenerDatos();
    if (!validarDatos(datos)) return;

    $.ajax({
        type: "POST",
        url: "/calcular_credito",
        data: JSON.stringify(datos),
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        success: function(respuesta) {
            document.getElementById("resultado").innerHTML = respuesta.mensaje;
        },
        error: function() {
            document.getElementById("resultado").innerHTML = "Error al comunicarse con el servidor.";
        }
    });
}

function calcularPromedio() {
    let datos = obtenerDatos();
    if (!validarDatos(datos)) return;

    $.ajax({
        type: "POST",
        url: "/calcular_promedio",
        data: JSON.stringify(datos),
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        success: function(respuesta) {
            document.getElementById("resultado").innerHTML = 
                "Promedio de ingresos: $" + respuesta.promedio.toFixed(2);
        },
        error: function() {
            document.getElementById("resultado").innerHTML = "Error al comunicarse con el servidor.";
        }
    });
}


/* 
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
 */