function enviar_a_calcular(){

	var var_nro1 = document.getElementById('nro1').value;
	var var_nro2 = document.getElementById('nro2').value;
	var var_operacion = document.getElementById('operacion').value;

	if(var_nro1.length<=0){
		alert("DEBE CARGAR EL NRO 1")
		return
	}
	if(var_nro2.length<=0){
		alert("DEBE CARGAR EL NRO 2")
		return
	}
	if(var_operacion==0){
		alert("DEBE SELECCIONAR UNA OPERACION MATEMATICA")
		return
	}

	// Los parametros a  enviar
    datos = {"p_nro1": var_nro1,"p_nro2": var_nro2,"p_operacion": var_operacion}
	 $.ajax({
        
	        type: 'POST',
	        url: '/calcular',
            data: JSON.stringify(datos),
            headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
            },
	        success: function (response) {
				document.getElementById('label_mensaje').innerHTML = response.mensaje //CUANDO DEVUELVO UN TEXTO

	        },
	        error: function (response) {
                alert("HUBO UN ERROR");
	        }
	    });

}
