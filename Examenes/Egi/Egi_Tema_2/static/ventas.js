function iniciar_sesion() {
    const data = {
        user: $("#user").val().trim(),
        pasw: $("#pasw").val().trim()
    };

    $.ajax({
        type: "POST",
        url: "/login",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function (res) {
            if (res.success) {
                window.location.href = "/ventas";
            } else {
                $("#mensaje").html(res.message);
            }
        }
    });
}

function registrarVenta() {
    const data = {
        cantidad: $("#cantidad").val(),
        precio: $("#precio").val()
    };

    $.ajax({
        type: "POST",
        url: "/registrar",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function (res) {
            if (!res.success){
                alert("No a inisiado secion")
                window.location.href = "/";
            }
            $("#resultado").html(res.mensaje);
        }
    });
}

function obtenerPromedio() {
    $.ajax({
        type: "GET",
        url: "/promedio",
        success: function (res) {
            $("#resultado").html(
                "Usuario: " + res.usuario + "<br>" +
                "Precio promedio: $" + res.promedio.toFixed(2)
            );
        },
        error: function (err) {
            $("#resultado").html("No hay ventas registradas.");
        }
    });
}
