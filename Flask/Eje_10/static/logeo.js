// -----------------------------
// INICIAR SESIÓN
// -----------------------------
function iniciar_sesion() {
    const data = {
        user: document.getElementById("user").value.trim(),
        pasw: document.getElementById("pasw").value.trim()
    };

    const msj = document.getElementById("mensaje");
    let errores = "";

    if (data.user === "") {
        errores += "Complete el campo de usuario<br>";
    }
    if (data.pasw === "") {
        errores += "Complete el campo de contraseña<br>";
    }

    if (errores.length > 0) {
        msj.innerHTML = errores;
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(respuesta) {
            if (respuesta.success) {
                window.location.href = "/cargar_banco_xxx";
            } else {
                msj.innerHTML = respuesta.message || "Usuario o contraseña incorrectos";
            }
        },
        error: function(error) {
            msj.innerHTML = "Error al intentar iniciar sesión";
        }
    });
}
