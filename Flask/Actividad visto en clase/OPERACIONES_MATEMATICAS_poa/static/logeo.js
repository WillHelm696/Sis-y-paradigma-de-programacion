		function logueo(){
		
			var nombre = document.getElementById("nombreUser").value;
			var clave = document.getElementById("contraseña").value;
			if(nombre.length<=0 || clave.length<=0){
				alert("**DEBE INGRESAR EL USUARIO Y LA CONTRASEÑA**");
				return
			}	

			// Los parametrosa  enviar
			datos = {"p_nombre": nombre,"p_clave": clave}
			$.ajax({
				
					type: 'POST',
					url: '/logueo',
					data: JSON.stringify(datos),
					headers: {
							'Accept': 'application/json',
							'Content-Type': 'application/json'
					},
					success: function (response) {

						//alert("Respuesta: "+response.mensaje_devuelto); //CUANDO DEVUELVO UN TEXTO
						//return
						if(response.mensaje_devuelto == 'OK'){
							window.location.replace("/carga_operaciones_poa")
						}else{
							document.getElementById('label_mensaje').innerHTML = response.mensaje_devuelto
						}

					},
					error: function (response) {
						alert("HUBO UN ERROR");
					}
				});
		}