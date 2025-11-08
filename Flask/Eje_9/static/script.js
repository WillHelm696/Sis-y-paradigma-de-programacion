function ordenar(){
    let datos={
        'nombre1': document.getElementById('nombre1').value,
        'nombre2': document.getElementById('nombre2').value,
        'nombre3': document.getElementById('nombre3').value,
        'nombre4': document.getElementById('nombre4').value,
        'nombre5': document.getElementById('nombre5').value,        
    }
    let menssaje = document.getElementById("mensaje")
    let tabla = document.getElementById("lista")

    if (datos.nombre1==="" || datos.nombre2==="" || datos.nombre3==="" || datos.nombre4==="" || datos.nombre5===""){
        tabla.innerHTML = ""
        menssaje.innerHTML = "Todos los campos son obligatorios";
        return
    }
    menssaje.innerHTML = "";
    $.ajax({
        type:'POST',
        url:'http://127.0.0.1:5000/ordenar',
        data:JSON.stringify(datos),
        headers:{
            'Accept':'application/json',
            'Content-Type':'application/json'
        },
        success: function(respuesta){
            let html=
            `
            <tr><th>${respuesta.nombre1}</th></tr>
            <tr><th>${respuesta.nombre2}</th></tr>
            <tr><th>${respuesta.nombre3}</th></tr>
            <tr><th>${respuesta.nombre4}</th></tr>
            <tr><th>${respuesta.nombre5}</th></tr>
            `;
            tabla.innerHTML = html
        },
        error: function(){
            alert("Error al comunicarse con el servidor");
        }
    })
}