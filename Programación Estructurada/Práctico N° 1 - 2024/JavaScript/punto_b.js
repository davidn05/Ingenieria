var edad = parseInt(prompt("Indique su edad"));

alert("Indique su sexo");
alert("Hombre = 1");
alert("Mujer = 2");
var sexo = parseInt(prompt());

if (edad >= 16) {
    if (sexo === 1) {
        alert("Usted es hombre y puede votar.");
    } else if (sexo === 2) {
        alert("Usted es mujer y puede votar.");
    }
} else {
    if (sexo === 1) {
        alert("Usted es hombre y no puede votar.");
    } else if (sexo === 2) {
        alert("Usted es mujer y no puede votar.");
    }
}
