document.addEventListener("DOMContentLoaded", () => {
    const campos = document.getElementById("campos");
    const agregar = document.getElementById("agregar");

    agregar.onclick = () => {
        const cantidad = campos.querySelectorAll(".campo").length;
        if (cantidad >= 10) {
        alert("Solo se pueden ingresar hasta 10 materias.");
        return;
        }

        campos.insertAdjacentHTML("beforeend", `
        <div class="campo">
            <input type="text" name="materia[]" placeholder="Materia" required>
            <input type="number" name="nota[]" placeholder="Nota" min="0" max="10" required>
            <button type="button" class="eliminar">X</button>
        </div>
        `);
    };

    campos.onclick = e => {
        if (e.target.classList.contains("eliminar")) {
        e.target.parentElement.remove();
        }
    };

    document.getElementById("formulario").onsubmit = e => {
        e.preventDefault();
        alert("Formulario enviado correctamente.");
    };
});

