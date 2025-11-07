function enviar_datos(){

	if(document.getElementById('id_dni').value.length<=0){
		alert("DEBE CARGAR UN DNI")
		return
	}
	if(document.getElementById('id_nombre').value.length<=0){
		alert("DEBE CARGAR UN NOMBRE 111111")
		return
	}
	var dni = document.getElementById('id_dni').value;
	var nombre = document.getElementById('id_nombre').value;

	// Los parametros a  enviar
    datos = {"pp_dni": dni,"pp_nombre": nombre}
	 $.ajax({
        
	        type: 'POST',
	        url: 'http://127.0.0.1:5000/servidor',
            data: JSON.stringify(datos),
            headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
            },
	        success: function (respuesta) {

				// alert("Respuesta: "+respuesta.mensaje); //CUANDO DEVUELVO UN TEXTO
				document.getElementById("mensaje").innerHTML = respuesta.mensaje

	        },
	        error: function (respuesta) {
                alert("HUBO UN ERROR");

	        }
	    });

}

function enviar_datos_bis(){

	if(document.getElementById('id_dni').value.length<=0){
		alert("DEBE CARGAR UN DNI")
		return
	}
	if(document.getElementById('id_nombre').value.length<=0){
		alert("DEBE CARGAR UN NOMBRE")
		return
	}
	var dni = document.getElementById('id_dni').value;
	var nombre = document.getElementById('id_nombre').value;

	// Los parametrosa  enviar
	datos = {"p_dni": dni,"p_nombre": nombre}
	$.ajax({
		
			type: 'POST',
			url: 'http://127.0.0.1:5000/servidor_estructura',
			data: JSON.stringify(datos),
			headers: {
					'Accept': 'application/json',
					'Content-Type': 'application/json'
			},
			success: function (respuesta) {

				mensaje = ""
				claves = Object.keys(respuesta)
				if(claves.length>0){
					for(i=0;i<claves.length;i++){
						// console.log(claves[i]+ " --- "+respuesta[claves[i]]);
						mensaje += claves[i]+ ": "+respuesta[claves[i]] + "<br>"
					}
					
				}else{
					mensaje = "NO HAY DATOS"
				}

				document.getElementById("mensaje").innerHTML = mensaje

			},
			error: function (respuesta) {
				alert("HUBO UN ERROR");
			}
		});

}