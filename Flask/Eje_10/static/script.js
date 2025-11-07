function enviarAnalisis() {
    // Validaciones básicas
    if ($("#nombre").val().trim() === "") { alert("Debe ingresar nombre y apellido"); return; }
    if ($("#tipo_doc").val() === "") { alert("Debe seleccionar un tipo de documento"); return; }
    if ($("#colesterol").val() === "") { alert("Debe ingresar el colesterol"); return; }

    // Capturar valores
    var datos = {
        nombre: $("#nombre").val(),
        tipo_doc: $("#tipo_doc").val(),
        colesterol: parseFloat($("#colesterol").val()),
        rojos: parseFloat($("#rojos").val()),
        blancos: parseFloat($("#blancos").val()),
        glucemia: parseFloat($("#glucemia").val()),
        trigliceridos: parseFloat($("#trigliceridos").val())
    };

    // Si colesterol es alto → analizar glóbulos
    if (datos.colesterol > 200) {
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/analizar_globulos",
            data: JSON.stringify(datos),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            success: function(respuesta) {
                $("#mensaje").html(respuesta.mensaje);
            },
            error: function() { alert("Error al comunicarse con el servidor"); }
        });
    }
    // Si colesterol bajo → analizar triglicéridos
    else {
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/analizar_trigliceridos",
            data: JSON.stringify(datos),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            success: function(respuesta) {
                $("#mensaje").html(respuesta.mensaje);
            },
            error: function() { alert("Error al comunicarse con el servidor"); }
        });
    }
}
