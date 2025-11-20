function iniciar_sesion(){
    data={
        user: document.getElementById("user").value,
        pasw: document.getElementById("pasw").value
    }
    let msj = document.getElementById("mensaje")
    let rta = ""

    if(data.user.length <= 0 ){
        rta += "Complte el campo de username <br>"
    }if (data.pasw.length <= 0){
        rta += "Complte el campo de password <br>"
    }if (rta.length <= 0 ){
        msj.innerHTML= rta
        return
    }
    alert(data.user,data.pasw)

    $.ajax=({
        type: 'POST',
        url: '/login',
        data: JSON.stringify(datos),
        headers: {
            'Accept': 'application/json',
            'Content-Type':'application/json'
        },
        success : function(respuesta){

        },
        error: function(){
            alert("HUBO UN ERROR");
        }
        
    })
}