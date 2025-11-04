const COLESTEROL_LIMITE = 200;

async function validar_datos(datos,mensaje){
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
    // 3. Llamada AJAX (fetch) al servidor
    mensaje.className = 'enviando';
    mensaje.innerHTML = 'Enviando datos al servidor para análisis...';
    try {
        const respuesta = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datos)
        });
        const resultadoFlask = await respuesta.json();
        // 4. Mostrar la respuesta del servidor
        let html = `
            <h2>${resultado.titulo}</h2>
            <p><strong>Datos Recibidos:</strong> ${resultado.datos_recibidos}</p>
            <hr>
            <p><strong>Conclusión del Servidor:</strong></p>
            <ul>
                ${resultado.conclusion.map(item => `<li>${item}</li>`).join('')}
            </ul>
        `;
        mensaje.className = resultado.tipo; // Usa la clase de estilo definida por Flask
        mensaje.innerHTML = html;
    } catch (error) {
        console.error('Error al comunicarse con el servidor:', error);
        mensaje.className = 'error';
        mensaje.innerHTML = '**Error de Conexión:** No se pudo contactar al servidor Flask.';
    }
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

