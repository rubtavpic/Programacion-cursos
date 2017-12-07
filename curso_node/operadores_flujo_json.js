// definimos un objeto de forma literal
var empleado = {
    nombre: "Smith",
    profesion: "Agente",
    edad: 42,
    armas: ["pistola", "rifle", "kungfu"]
};

console.log(empleado);

// serializar el objeto
var serializado = JSON.stringify(empleado);

console.log(serializado);

// des-serializar el objeto
var leido = JSON.parse(serializado);
console.log(leido);

//Para hacer que falle el try :
// serializado = serializado + '}';
var leido2;

try {
    leido2 = JSON.parse(serializado);
} catch (err) {
    console.log('No se pudo leer "serializado"');
}

if (typeof leido2 !='undefined') {
    console.log('Hay algo leido');
} else {
    console.log('No hay nada leido');
}

for (var i = 0; i < empleado.armas.length; i++) {
    var arma = empleado.armas[i];
    console.log(empleado.nombre + (arma == 'kungfu' ? ' sabe ' : ' tiene ') + arma);
}