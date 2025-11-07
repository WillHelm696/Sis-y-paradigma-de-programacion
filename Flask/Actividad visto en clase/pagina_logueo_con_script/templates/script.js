		function enviar_informacion_get(){
		
			var nombre = document.getElementById("formulario_get").nombreUser.value;
			var clave = document.getElementById("formulario_get").contraseña.value;
			if(nombre.length<=0 || clave.length<=0){
				alert("**DEBE INGRESAR EL USUARIO Y LA CONTRASEÑA**");
			}else{

				//document.getElementById("formulario_get").action = "";
				document.getElementById("formulario_get").submit();
			}		
		}
		
		function enviar_informacion_post(){
		
			var nombre = document.getElementById("formulario_post").nombreUser.value;
			var clave = document.getElementById("formulario_post").contraseña.value;
			if(nombre.length<=0 || clave.length<=0){
				alert("**DEBE INGRESAR EL USUARIO Y LA CONTRASEÑA**");
			}else{
				document.getElementById("formulario_post").submit();
			}		
		}