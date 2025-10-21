function calcular_impar(){
    min = document.getElementById(('min').value)
    max = document.getElementById(('max').value)
    if( min <= max){
        document.getElementById('mensaje').innerHTML ="Los valore ingresados no incorrectos"
    }
}