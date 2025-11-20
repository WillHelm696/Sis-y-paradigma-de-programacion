$(document).ready(function() {
    // Función para validar datos
    function validarDatos() {
        const dni = $("#dni").val().trim();
        const nombre = $("#nombre").val().trim();
        const apellido = $("#apellido").val().trim();
        const personas = parseInt($("#personas").val());
        const sueldos = $("#sueldos").val().trim().split(",").map(Number);

        if (!dni || !nombre || !apellido || isNaN(personas) || sueldos.some(isNaN)) {
            alert("Por favor, complete todos los campos correctamente.");
            return false;
        }
        return { dni, nombre, apellido, personas, sueldos };
    }

    // Botón Calcular Crédito
    $("#calcularCredito").click(function() {
        const datos = validarDatos();
        if (!datos) return;

        $.ajax({
            url: "/calcular_credito",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(datos),
            success: function(response) {
                $("#resultado").val(`Monto de crédito otorgado: $${response.monto}`);
            },
            error: function(xhr, status, error) {
                alert("Error al calcular el crédito: " + error);
            }
        });
    });

    // Botón Calcular Promedio
    $("#calcularPromedio").click(function() {
        const datos = validarDatos();
        if (!datos) return;

        $.ajax({
            url: "/calcular_promedio",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(datos),
            success: function(response) {
                $("#resultado").val(`Promedio de sueldos: $${response.promedio}`);
            },
            error: function(xhr, status, error) {
                alert("Error al calcular el promedio: " + error);
            }
        });
    });
});

