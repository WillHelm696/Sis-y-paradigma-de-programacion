function datos(){
    return {
        cuit: parseInt(document.getElementById('cuit').value.trim()),
        nombre: document.getElementById('nombre').value,
        apellido: document.getElementById('apellido').value,
        inmuebles: parseInt(document.getElementById('inmuebles').value),
        valor: parseFloat(document.getElementById('valor').value)
    }
    
}

function verificar_datos(Obj_dato){

    let msj= document.getElementById('msj')
    let rta=''


/*     if (isNaN(objDatos.cuit)) respuesta += "Ingrese CUIT <br>";
    if (!objDatos.nombre) respuesta += "Ingrese Nombre <br>";
    if (!objDatos.apellido) respuesta += "Ingrese Apellido <br>";
    if (isNaN(objDatos.inmueble)) respuesta += "Ingrese Nº de Inmueble <br>";
    if (isNaN(objDatos.valor)) respuesta += "Ingrese Valor del Inmueble <br>"; */

    if (isNaN(Obj_dato.cuit)){
        rta +="Falta Ingresar Cuit <br>"
    }/* else(Obj_dato){
        rta +="Cuit debe contener solo Numeros <br>"
    } */
    
    
    if (!Obj_dato.nombre){
        rta +="Falta Ingresar Nombre <br>"
    }if (!Obj_dato.apellido){
        rta +="Falta Ingresar Apellido <br>"
    }if (isNaN(Obj_dato.inmuebles)){
        rta +="Falta Ingresar nº Inmuebles <br>"
    }if (isNaN(Obj_dato.valor)){
        rta +="Falta Ingresar Valor Total <br>"
    }

    if (rta !== ''){
        msj.innerHTML = rta
        return true
    }
    msj.innerHTML = ''
}

function calcular_impuesto(){
    let Obj_dato=datos()
    if (verificar_datos(Obj_dato)){
        return
    }
    let msj= document.getElementById('msj')

    console.log(Obj_dato)
    $.ajax({
            type: 'POST',
            url: "/calcular_promedio_impuesto",
            data: JSON.stringify(Obj_dato),
            headers: {
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            success: function(respuesta){
                msj.innerHTML = 
                "Debe abonar " + respuesta.abono+ "% <br>" +

                "Promedio: " +  respuesta.impuesto + "+" + Obj_dato.valor;
            },
            error: function(){
                alert("Error al comunicarse con el servidor");
            }
        });
}

function calcular_promedio(){
    let Obj_dato=datos()
    if (verificar_datos(Obj_dato)){
        return
    }

    $.ajax({
            type: 'POST',
            url: "/calcular_promedio_propiedades",
            data: JSON.stringify(Obj_dato),
            headers: {
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            success: function(respuesta){
                msj.innerHTML = "Promedio: " + respuesta.promedio; 
            },
            error: function(){
                alert("Error al comunicarse con el servidor");
            }
        });
}
