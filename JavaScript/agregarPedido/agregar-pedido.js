// ------ FUNCIONES ---------
const isChecked = () => { 
    if (radio_fruta.checked){
        producto_fruta.style.display="flex";
        producto_verdura.style.display="none";
    }
    else if (radio_verdura.checked){
        producto_fruta.style.display="none";
        producto_verdura.style.display="flex";
        console.log("verdura esta checked");
    }
}

const validateLenght = (descripcion) => descripcion && descripcion.length>=3 && descripcion.length<=300;

const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

const validate = () => {
    // Recuperar lo que va a ser testeado :)
    const descTextArea = document.getElementById("desc-producto");
    const nombreProductor = document.getElementById("nombre");
    const email  = document.getElementById("user-email"); 

    const nombreIsValid = validateLenght(nombreProductor.value);
    const emailIsValid = validateEmail(email.value);

    if (emailIsValid){
        console.log("hola");
    }
    else {
        console.log("elpepe");
    }
}




// ----- RECUPERAR INFO DE HTML ----------
const radio_fruta = document.getElementById("fruta");
const radio_verdura = document.getElementById("verdura");
const fruta_o_verdura = document.querySelector("#Tipo-fruta-o-verdura");

const producto_fruta = document.getElementById("checkbox-producto-fruta");
const producto_verdura = document.getElementById("checkbox-producto-verdura");

const button = document.getElementById("prueba-button");

//------ Esconde los productos -------
//producto_fruta.style.display="none";
//producto_verdura.style.display="none";


// ------- EVENTOS ----------
fruta_o_verdura.addEventListener("change",isChecked);

button.addEventListener("click",validate);

