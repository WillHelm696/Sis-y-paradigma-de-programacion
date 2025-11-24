// -----------------------------
// DATOS USUARIO
// -----------------------------
window.onload = function () {

    $.ajax({
        url: "/api/usuario",
        method: "GET",
        success: function (data) {
            if (data.success === false ){
                window.location.href = "/";
            }            
            document.getElementById("current-user").innerText = data.usuario;
            document.getElementById("current-balance").innerText = "$ " + data.saldo.toFixed(2);
        },
        error: function () {
            window.location.href = "/"; 
        }
    });
};
// -----------------------------
// DEPOSITO
// -----------------------------
function realizarDeposito() {
    let monto = parseFloat(document.getElementById("deposito-monto").value);
    let msj = document.getElementById("operation-message");

    if (isNaN(monto) || monto <= 0) {
        msj.innerHTML = "Monto no válido";
        return;
    }

    let data = { monto: monto };

    $.ajax({
        type: 'POST',
        url: '/deposito',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function (respuesta) {
            if (respuesta.success === false ){
                window.location.href = "/";
            }            
            msj.innerHTML = respuesta.mensaje;
            // actualizar saldo en pantalla
            document.getElementById("current-balance").innerText =
                "$ " + respuesta.saldo.toFixed(2);
        },
        error: function (error) {
            msj.innerHTML = "Error al depositar: " + error.responseText;
        }
    });
}
// -----------------------------
// RETIRRO
// -----------------------------
function realizarRetiro() {
    let monto = parseFloat(document.getElementById("retiro-monto").value);
    let msj = document.getElementById("operation-message");

    if (isNaN(monto) || monto <= 0) {
        msj.innerHTML = "Monto no válido";
        return;
    }

    let data = { monto: monto };

    $.ajax({
        type: 'POST',
        url: '/retiro',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function (respuesta) {
            if (respuesta.success === false ){
                window.location.href = "/";
            }
            msj.innerHTML = respuesta.mensaje;
            document.getElementById("current-balance").innerText =
                "$ " + respuesta.saldo.toFixed(2);
        },
        error: function (xhr) {
            let err = JSON.parse(xhr.responseText);
            msj.innerHTML = "Error: " + err.error;
        }
    });
}
// -----------------------------
// TRANSACCION
// -----------------------------
function realizarTransaccion() {
    let monto = parseFloat(document.getElementById("transaccion-monto").value);
    let tipo = document.getElementById("Transacción").value;
    let destino = document.getElementById("transaccion-destino").value.trim();
    let msj = document.getElementById("operation-message");

    if (isNaN(monto) || monto <= 0) {
        msj.innerHTML = "Monto no válido";
        return;
    }
    if (tipo === "seleccione") {
        msj.innerHTML = "Debe seleccionar el tipo de transacción";
        return;
    }
    // Si el usuario eligió 'impuestos', no es necesario ingresar destino
    if (tipo === "impuestos") {
        destino = "impuestos";
    } else {
        if (destino === "") {
            msj.innerHTML = "Debe ingresar una cuenta destino";
            return;
        }
    }
    let data = {
        monto: monto,
        destino: destino,
        tipo: tipo
    };
    $.ajax({
        type: 'POST',
        url: '/transaccion',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function (respuesta) {
            if (respuesta.success === false ){
                window.location.href = "/";
            }
            msj.innerHTML = respuesta.mensaje;
            document.getElementById("current-balance").innerText = "$ " + respuesta.saldo.toFixed(2);
        },
        error: function (xhr) {
            let err = JSON.parse(xhr.responseText);
            msj.innerHTML = "Error: " + err.error;
        }
    });
}
// -----------------------------
// CONSULTAR MOVIMIENTOS
// -----------------------------
function consultarMovimientos() {
    let msj = document.getElementById("operation-message");
    $.ajax({
        url: "/movimientos",
        method: "POST",
        success: function (respuesta) {
            if (success ===false ){
                window.location.href = "/";
            }            
            msj.innerHTML = respuesta.mensaje;
        },
        error: function () {
            document.getElementById("operation-message").innerHTML = "Error al consultar saldo";
        }
    });
}

// -----------------------------
// CERRAR SESIÓN
// -----------------------------
function cerrar_sesion() {

    $.ajax({
        type: 'POST',
        url: '/cerrar',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(respuesta) {
            window.location.href = "/";
        },
        error: function(error) {
            console.log(error);
            const msj = document.getElementById("mensaje");
            if (msj) {
                msj.innerHTML = "Error al cerrar sesión";
            }
        }
    });

}
