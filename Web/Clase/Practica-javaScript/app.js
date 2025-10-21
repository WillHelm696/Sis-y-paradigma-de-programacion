function datos(){
    let a = new Array(3);
    nombre=parseInt(document.getElementById(nombre).value);
    a[0]=nombre;
    contraseña=parseInt(document.getElementById(contraseña).value);
    a[1]=contraseña;
    gmail=parseInt(document.getElementById(gmail).value);
    a[2]=gmail;

    console.log(a);

    alert(a);
    
}


function save(){
    var edad = document.getElementById("edad".value)
    document.getElementById('mesaje').innerHTML = ""
}

console.log('Hola Mundo');

/* Variable 

UpperCamelCase, camelCalse, snake_case */
let nombre="Hola Mundo"; /*let para asignar variables*/
let apellido;
apellido='Schurmann'


console.log(nombre);

let animal, raza

animal='Perro'
raza='Canino'
console.log(animal,raza)

/* Tipos de datos 
Primitivos:Number, String,Boolean, Undefined, Null
DeReferencia: Array, Object, Function, Clases
*/


/* ------------------------------------------------------------------------- */
/*Primitivo*/
console.log("---------------------------------------------------------------------------------------");
let numero=1;
let texo="Hola mundo";
let verdedadero=true;
let noDefinido;
let undef = undefined;
let nulo=null;


/* -------------------------------------------------------------------------------------- */
console.log("---------------------------------------------------------------------------------------");
const nombre2="CHanchito feliz";
console.log(nombre2);
/* ------------------------------------------------------------------------------------------------- */

let numero4 = 42;
let nombre4 = "Hola mundo";
let verdedadero4= true;
let undef4;
let nula4=null;

console.log("la variable numero4 es",numero4 ,"y es de tipo", typeof numero);
console.log("la variable nombre4 es",nombre4,"y es de tipo", typeof nombre4);
console.log("la variable verdedadero4 es",verdedadero4,"y es de tipo", typeof verdedadero4);
console.log("la variable undef4 es",undef4,"y es de tipo", typeof undef4);
console.log("la variable nula4 es",nula4,"y es de tipo", typeof nula4);

/* ------------------------------------------------------------------------------------------------- */
