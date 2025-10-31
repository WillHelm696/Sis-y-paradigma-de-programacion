function     selecionar_provicia(opcion){
    const Imagen = document.getElementById('imag')
    switch(opcion){
        case "Buenos Aires":
            Imagen.src="img/Map_of_Buenos_Aires_Province.svg.png"
            break

        case "Catamarca":
            Imagen.src="img/Map_of_Catamarca_Province.svg"
            break
        case "Chaco":
            Imagen.src="img/Map_of_Chaco_Province.svg"
            break

        case "Chubut":
            Imagen.src="img/Map_of_Chubut_Province.svg"
            break

        case "Córdoba":
            Imagen.src="img/Map_of_Cordoba_Province,_Argentina.png"
            break

        case "Corrientes":
            Imagen.src="img/Map_of_Corrientes_Province.svg"
            break

        case "Entre Ríos":
            Imagen.src="img/Map_of_Entre_Rios_Province.svg"
            break

        case "Formosa":
            Imagen.src="img/Map_of_Formosa_Province.svg"
            break

        case "Jujuy":
            Imagen.src="img/Map_of_Jujuy_Province.svg"
            break

        case "La Pampa":
            Imagen.src="img/Map_of_La_Pampa_Province.svg"
            break

        case "La Rioja":
            Imagen.src="img/Map_of_La_Rioja_Province_(Argentina).svg"
            break

        case "Mendoza":
            Imagen.src="img/Map_of_Mendoza_Province.svg"
            break

        case "Misiones":
            Imagen.src="img/Map_of_Misiones_Province.svg.png"
            break

        case "Neuquén":
            Imagen.src="img/Map_of_Neuquén_Province.svg"
            break

        case "Río Negro":
            Imagen.src="img/Map_of_Río_Negro_Province.svg"
            break

        case "Salta":
            Imagen.src="img/Map_of_Salta_Province.svg"
            break

        case "San Juan":
            Imagen.src="img/Map_of_San_Juan_Province.svg"
            break

        case "San Luis":
            Imagen.src="img/Map_of_San_Luis_Province.svg.png"
            break

        case "Santa Cruz":
            Imagen.src="img/Mapa_Santa_Cruz_2.svg.png"
            break

        case "Santa Fe":
            Imagen.src="img/Map_of_Santa_Fe_Province.svg"
            break

        case "Santiago del Estero":
            Imagen.src="img/Map_of_Santiago_del_Estero.svg.png"
            break

        case "Tierra del Fuego":
            Imagen.src="img/Tierra_del_Fuego_(Argentina)_and_Isla_de_los_Estados.svg.png"
            break

        case "Tucumán":
            Imagen.src="img/Map_of_Tucuman_Province.svg"
            break

        default:
            Imagen.src=""

    }
}

function guardarDatos() {
    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const edad = parseInt(document.getElementById('edad').value);
    const direccion = document.getElementById('direccion').value.trim();
    const genero = document.querySelector('input[name="seleccion"]:checked')?.value || '';
    const provincia = document.getElementById('provincia').value;
    const validar = document.getElementById('datos');

    if (!nombre || !apellido || isNaN(edad) || !direccion || !genero || !provincia) {
        validar.innerHTML = "⚠️ Por favor, complete todos los campos correctamente.";
    } else {
        validar.innerHTML = `✅ Datos guardados:<br>Nombre: ${nombre}<br>Apellido: ${apellido}<br>Edad: ${edad}<br>Dirección: ${direccion}<br>Género: ${genero}<br>Provincia: ${provincia}`;
    }
}
 


function Validar_Form() {
    const form = document.getElementById('tiketForm');
    const nombre = form.nombre.value.trim();
    const apellido = form.apellido.value.trim();
    let valid = true;

    if (!nombre) {
        alert("⚠️ Complete el campo Nombre");
        valid = false;
    }
    if (!apellido) {
        alert("⚠️ Complete el campo Apellido");
        valid = false;
    }

    return valid;
}

