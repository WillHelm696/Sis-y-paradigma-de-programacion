const COLESTEROL_LIMITE = 200;

function validar_datos(datos, mensajeElement) {
    // 2. Determinar la URL del servidor según el colesterol
    const colesterolValor = parseFloat(datos.colesterol);
    let url;
    if (colesterolValor > COLESTEROL_LIMITE) {
        // Colesterol Alto: Analizar Glóbulos
        url = '/analisis_globulos';
    } else {
        // Colesterol Normal/Bajo: Analizar Triglicéridos
        url = '/analisis_trigliceridos';
    }

    // 3. Llamada AJAX con jQuery
    mensajeElement.className = 'enviando';
    mensajeElement.innerHTML = 'Enviando datos al servidor para análisis...';

    $.ajax({
        type: 'POST',
        url: url,
        data: JSON.stringify(datos),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success: function(respuesta) {
            let html = `
                <h2>${respuesta.titulo}</h2>
                <p><strong>Datos Recibidos:</strong> ${respuesta.datos_recibidos}</p>
                <hr>
                <p><strong>Conclusión del Servidor:</strong></p>
                <ul>
                    ${respuesta.conclusion.map(item => `<li>${item}</li>`).join('')}
                </ul>
            `;
            mensajeElement.className = respuesta.tipo; // Usa la clase de estilo definida por Flask
            mensajeElement.innerHTML = html;
        },
        error: function(xhr, status, error) {
            console.error('Error al comunicarse con el servidor:', error);
            mensajeElement.className = 'error';
            mensajeElement.innerHTML = '**Error de Conexión:** No se pudo contactar al servidor Flask.';
        }
    });
}


function verificacion(){
    datos ={

        nombre: document.getElementById('nombre').value.trim(),
        apellido: document.getElementById('apellido').value.trim(),
        tipo: document.getElementById('tipo').value,    
        
        colesterol: parseFloat(document.getElementById('colesterol').value),
        globulosRojos: parseFloat(document.getElementById('globulos_rojos').value),
        globulosBlancos: parseFloat(document.getElementById('globulos_blancos').value),
        glucemina: parseFloat(document.getElementById('glucemia').value),
        trigliceridos: parseFloat(document.getElementById('trigliceridos').value)
        
    }
    
    let mensaje = document.getElementById('mensaje')
    let contexto=""

    if (datos.nombre === ""){
        contexto += "Complete campo **Nombre** <br>"
    }if (datos.apellido === ""){
        contexto += "Complete campo **Apellido** <br>"
    }if(datos.tipo === "selecione"){
        contexto +="**Selecione** El tipo de documento <br>"
    }
    
    if(isNaN(datos.colesterol)){
        contexto += "Complete campo colesterol<br> "
    }if(isNaN(datos.globulosRojos)){
        contexto += "Complete campo Globulo Rojo<br>"
    }if(isNaN(datos.globulosBlancos)){
        contexto += "Complete campo Globulo Blanco<br>"
    }if(isNaN(datos.glucemina)){
        contexto += "Complete campo glucemina<br>"
    }if(isNaN(datos.trigliceridos)){
        contexto += "Complete campo trigliceridos <br>"
    }

    if (contexto != ""){
    //Vericficar Errores
        mensaje.innerHTML = contexto
        return
    }
/*     mensaje.innerHTML = "Todods los campos Fueron completado<br>" + */
    
    return validar_datos(datos,mensaje)
    
}

