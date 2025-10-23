function tirarDado() {
    const imagen = document.getElementById('imagen_dado')
    const numero = document.getElementById('numero')
    const resultado= Math.floor(Math.random()*6)+1

    switch (resultado) {
        case 1:
            imagen.src = "img/pngwing.com(1).png";
            break;
        case 2:
            imagen.src = "img/pngwing.com(2).png";
            break;
        case 3:
            imagen.src = "img/pngwing.com(3).png";
            break;
        case 4:
            imagen.src = "img/pngwing.com(4).png";
            break;
        case 5:
            imagen.src = "img/pngwing.com(5).png";
            break;
        case 6:
            imagen.src = "img/pngwing.com(6).png";
            break;
        default:
            imagen.src = "";
    }
    numero.innerHTML= "Numero que salio " + resultado
}
