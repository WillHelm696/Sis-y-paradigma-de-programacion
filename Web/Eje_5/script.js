
function controles_logicos(){
    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const direccion = document.getElementById('direccion').value.trim();
    const dniStr = document.getElementById('dni').value.trim();
    const fecha = document.getElementById('nacimiento').value;

    const errores = [];

    // Campos obligatorios
    if (!nombre) errores.push('Falta el nombre');
    if (!apellido) errores.push('Falta el apellido');
    if (!direccion) errores.push('Falta la dirección');
    if (!dniStr) errores.push('Falta el DNI');

    // Validaciones de formato
    if (nombre && hasNumber(nombre)) errores.push('El nombre no debe contener números');
    if (apellido && hasNumber(apellido)) errores.push('El apellido no debe contener números');

    const dni = parseInt(dniStr, 10);
    if (dniStr && (isNaN(dni) || dni < 1)) errores.push('DNI inválido');

    // Fecha de nacimiento lógica
    if (!fecha) {
        errores.push('Falta la fecha de nacimiento');
    } else {
        const nacimiento = new Date(fecha);
        const hoy = new Date();
        if (nacimiento > hoy) {
            errores.push('La fecha de nacimiento no puede ser futura');
        } else {
            const edad = calcularEdad(nacimiento, hoy);
            if (edad < 10) errores.push('Edad inválida: el alumno debe tener al menos 10 años');
            if (edad > 120) errores.push('Edad inválida');
        }
    }

    // Materias y notas
    const campo = document.getElementById('campo');
    const filas = campo ? campo.querySelectorAll('.campo-complejo') : [];
    let materiasCargadas = 0;
    let notasSum = 0;
    let notasContadas = 0;
    const problemasMaterias = [];

    filas.forEach(function(div, index){
        const nombreMateria = div.querySelector('input[name="campo[]"]').value.trim();
        const notaStr = div.querySelector('.nota').value.trim();

        if (nombreMateria !== '' || notaStr !== ''){
            if (nombreMateria !== '') materiasCargadas++;

            if (notaStr === ''){
                problemasMaterias.push(`Falta la nota para "${nombreMateria || 'Materia ' + (index+1)}"`);
            } else {
                const nota = parseFloat(notaStr.replace(',','.'));
                if (isNaN(nota) || nota < 0 || nota > 10) {
                    problemasMaterias.push(`Nota inválida (${notaStr}) para "${nombreMateria || 'Materia ' + (index+1)}"`);
                } else {
                    notasSum += nota;
                    notasContadas++;
                }
            }
        }
    });

    if (materiasCargadas < 5) errores.push('El alumno debe haber cursado al menos 5 materias');
    if (problemasMaterias.length) errores.push.apply(errores, problemasMaterias);

    // Promedio
    let promedio = null;
    if (notasContadas > 0) promedio = notasSum / notasContadas;
    if (promedio !== null && promedio <= 7) errores.push(`El promedio (${promedio.toFixed(2)}) debe ser superior a 7`);

    mostrarResultado(errores, promedio);
}

function hasNumber(str){
    return /\d/.test(str);
}

function calcularEdad(nacimiento, hoy){
    let edad = hoy.getFullYear() - nacimiento.getFullYear();
    const m = hoy.getMonth() - nacimiento.getMonth();
    if (m < 0 || (m === 0 && hoy.getDate() < nacimiento.getDate())) edad--;
    return edad;
}

function mostrarResultado(errores, promedio){
    const cont = document.getElementById('result');
    if (!cont) {
        if (errores.length) alert('Errores:\n' + errores.join('\n'));
        else alert('Registro correcto. Promedio: ' + (promedio ? promedio.toFixed(2) : 'sin notas'));
        return;
    }

    if (errores.length){
        cont.innerHTML = '<div class="errores"><strong>Se encontraron errores:</strong><ul>' + errores.map(e => '<li>'+e+'</li>').join('') + '</ul></div>';
        cont.scrollIntoView({behavior:'smooth'});
    } else {
        cont.innerHTML = '<div class="exito"><strong>Registro correcto.</strong><p>Promedio: ' + (promedio ? promedio.toFixed(2) : 'sin notas') + '</p></div>';
        cont.scrollIntoView({behavior:'smooth'});
    }
}