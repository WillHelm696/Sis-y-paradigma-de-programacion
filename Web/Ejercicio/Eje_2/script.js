function calcular_impar() {
    var min = parseInt(document.getElementById('min').value);
    var max = parseInt(document.getElementById('max').value);
    var mensaje = document.getElementById('mensaje');

    if (isNaN(min) || isNaN(max) || min >= max) {
        mensaje.innerHTML = "Los valores ingresados no son correctos";
        return;
    }

    let impares = [];
    for (let i = min; i <= max; i++) {
        if (i % 2 !== 0) {
            impares.push(i);
        }
    }

    mensaje.innerHTML = "Números impares: " + impares.join(', ');
}
