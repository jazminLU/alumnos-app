const API_URL = "/alumnos/";

document.getElementById("alumnoForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const nombre = document.getElementById("nombre").value;

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("mensaje").textContent = data.mensaje || "Alumno agregado.";
      document.getElementById("nombre").value = "";
    })
    .catch(() => {
      document.getElementById("mensaje").textContent = "⚠️ Error al agregar el alumno.";
    });
});

document.getElementById("verAlumnosBtn").addEventListener("click", function() {
  fetch(API_URL)
    .then(res => res.json())
    .then(alumnos => {
      const lista = document.getElementById("listaAlumnos");
      lista.innerHTML = "";

      if (alumnos.length === 0) {
        lista.innerHTML = "<li>No hay alumnos registrados.</li>";
      } else {
        alumnos.forEach(alumno => {
          const item = document.createElement("li");
          item.textContent = `#${alumno.id} - ${alumno.nombre}`;
          lista.appendChild(item);
        });
      }
    })
    .catch(() => {
      console.error("Error al obtener los alumnos");
    });
});
