function rangos_numeros(){

	edad = parseInt(document.getElementById('edad').value)
	anio_nacimiento = (2025-edad)
	mi_arreglo = new Array(edad);
	indice=0
	for(i = anio_nacimiento; i <= 2025; i++){
		indice++
		mi_arreglo[indice] = i;
	}
	//alert(mi_arreglo.join(' // '))
	document.getElementById('mensaje').innerHTML = mi_arreglo.join(' // ')
}

function CalcularNacimiento(){
	var edad = document.getElementById('edad').value
	if (edad<18){
		//alert("ES MENOR")
		document.getElementById('mensaje').innerHTML = "ES MENOR"
	}else{
		//alert("ES MAYOR")
		document.getElementById('mensaje').innerHTML = "ES MAYOR"
	}
}
function CalcularNacimiento_2(){
	var edad = parseInt(document.getElementById('edad').value)
	alert("Año de nacimiento: " + (2025-edad))
}

function cargar_imagen_provincia(provincia){
	switch (provincia){
		case "codigo_mendoza":
			document.getElementById('titulo_imagen').innerHTML = "Imagen de la Provincia de MENDOZA"
			document.getElementById('imagen_provincia').src = "imagenes/mendoza.jpg"
			break
		case "codigo_sanjuan":
			document.getElementById('titulo_imagen').innerHTML = "Imagen de la Provincia de SAN JUAN"
			document.getElementById('imagen_provincia').src = "imagenes/san_juan.jpg"
			break
		case "codigo_sanluis":
			document.getElementById('titulo_imagen').innerHTML = "Imagen de la Provincia de SAN LUIS"
			document.getElementById('imagen_provincia').src = "imagenes/san_luis.jpg"
			break
		case "codigo_buenosaires":
			document.getElementById('titulo_imagen').innerHTML = "Imagen de la Provincia de BS.AS."
			document.getElementById('imagen_provincia').src = "imagenes/bsas.jpg"
			break
		case "codigo_cordoba":
			document.getElementById('titulo_imagen').innerHTML = "Imagen de la Provincia de CORDOBA"
			document.getElementById('imagen_provincia').src = "imagenes/cordoba.jpg"
			break		
		default:
			document.getElementById('imagen_provincia').src = ""
	}
	
}
function funcion_js() {
	
	alert("ESTO ES JAVASCRIPT")

}
function HolaMundo() {
    
	alert("Hola Mundo!!!!")
}

function ArregloSimple() {
    
	miArray = new Array();
	minimo = 1
	maximo = 100
	for(i=0;i<10;i++){

		miArray[i] = Math.floor(Math.random() * (maximo - minimo + 1) + minimo)
	}
	alert(miArray.join(', '))

}

function ArregloBiDimensional() {
    
	miArray = new Array()
	minimo = 1
	maximo = 100
	for(i=0;i<3;i++){
		miArray[i] = new Array()
		for(j=0;j<2;j++){

			miArray[i][j] = Math.floor(Math.random() * (maximo - minimo + 1) + minimo)

		}
	}
	texto_a_imprimir = ""
	for(i=0;i<3;i++){
		for(j=0;j<2;j++){

			texto_a_imprimir += "Fila: "+i+" Columna: "+j+" -> "+miArray[i][j] + "\n"

		}
	}
	alert(texto_a_imprimir)
	
}



  /*
  function OtraFuncion() {
	alert("UN MENSAJE DE LA FUNCION NUEVA")
  }

  function MostrarProvincia() {
	alert(document.getElementById('id_provincia').value)
  }
  */
 function CargarDptos(){
	id_provincia = parseInt(document.getElementById('provincias').value)
	switch (id_provincia){
		case 1:{

			borrarDptos()
			dptos = document.getElementById('dptos')
			dptos.options[1] = new Option('Godoy Cruz', 'Godoy Cruz', false, false);
			dptos.options[2] = new Option('Guaymallen', 'Guaymallen', false, false);
			dptos.options[3] = new Option('Maipu', 'Maipu', false, false);
			dptos.options[4] = new Option('Lujan', 'Lujan', false, false);
			dptos.options[5] = new Option('Capital', 'Capital', false, false);
			break;
		}
		case 2:{

			borrarDptos()
			dptos = document.getElementById('dptos')
			dptos.options[1] = new Option('Rivadavia', 'Rivadavia', false, false);
			dptos.options[2] = new Option('Caucete', 'Caucete', false, false);
			dptos.options[3] = new Option('Capital', 'Capital', false, false);
			dptos.options[4] = new Option('Pocito', 'Pocito', false, false);
			dptos.options[5] = new Option('Chimbas', 'Chimbas', false, false);
			break;
		}
		case 3:{

			borrarDptos()
			break;
		}
		case 4:{

			borrarDptos()
			break;
		}
		case 5:{

			borrarDptos()
			break;
		}
	}
 }
 function borrarDptos(){
	dptos = document.getElementById('dptos')
	for( indice = dptos.options.length; indice > 0  ;indice --) 
		{
			dptos.options[indice]=null;
		}
 }