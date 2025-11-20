function inisiar_secision(){
    data={
        user: document.getElementById("user").value,
        pasw: document.getElementById("pasw").value
    }

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