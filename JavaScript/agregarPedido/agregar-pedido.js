// ----VARIABLES Y CONSTANTES-----
const limit=5;


// ------ FUNCIONES ---------
const isChecked = () => { 
    if (radio_fruta.checked){
        esconder_fruta.style.display="block";
        esconder_error_verdura.style.display="none"
        esconder_verdura.style.display="none";
    }
    else if (radio_verdura.checked){
        esconder_fruta.style.display="none";
        esconder_error_fruta.style.display="none"
        esconder_verdura.style.display="block";
    }
}

const validateRadioButton= (valor) => {
    if (!valor){
        return false
    }
    else{
        return true
    }
}
const validateCheckbox = (valor) => {
    if(valor){
        if (valor.value=="FRUTA"){
            let num = 0;
            for(let i = 0; i<producto_fruta.length;i++){
                if(producto_fruta[i].checked){
                    num++;
                }
            }
            if(num>=1 && num<=limit){
                return true
            }
            return false
        }
        else if (valor.value=="VERDURA"){
            let num = 0;
            for(let i = 0; i<producto_verdura.length;i++){
                if(producto_verdura[i].checked){
                    num++;
                }
            }
            if(num>=1 && num<=limit){
                return true
            }
            return false
        }       
    }  
    else {
        return false;
    } 
}
const validateDescripcion = (descripcion) =>{
    return descripcion && descripcion.value.length<=500
} 
const validateFotos = (fotos) => {
    if(fotos.length>=1 && fotos.length<=3){
        return true;
    }
    else{
        return false;
    }
}
const validateLenght = (descripcion) => descripcion && descripcion.length>=3 && descripcion.length<=80;

const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };
const validateTelefono = (numero) => {
    const telefonoRegex = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;
    return telefonoRegex.test(numero);  
}


const validate = () => {
    // los errores mostrados en html 
    const error_tipo = document.getElementById("error-tipo");
    const error_email = document.getElementById("error-email");
    const error_nombre = document.getElementById("error-nombre");
    const error_checkbox_fruta = document.getElementById("error-checkbox-fruta");
    const error_checkbox_verdura = document.getElementById("error-checkbox-verdura");
    const error_fotos = document.getElementById("error-foto");
    const error_telefono = document.getElementById("error-telefono");
    const error_descripcion = document.getElementById("error-descripcion");

    // Recuperar lo que va a ser testeado :)
    const valor = document.querySelector('input[name="Tipo-fruta-o-verdura"]:checked');
    const descTextArea = document.getElementById("desc-producto");
    const fotos = document.getElementById("foto").files;
    const nombreProductor = document.getElementById("nombre");
    const email  = document.getElementById("user-email"); 
    const telefono = document.getElementById("telefono");

    const radioISValid = validateRadioButton(valor);
    const checkboxIsValid = validateCheckbox(valor);
    const descIsValid = validateDescripcion(descTextArea);
    const fotosIsValid = validateFotos(fotos);
    const nombreIsValid = validateLenght(nombreProductor.value);
    const emailIsValid = validateEmail(email.value);
    const telefonoIsValid = validateTelefono(telefono.value)
    if (!radioISValid){     
        error_tipo.style.display="block";
    }
    else{
        error_tipo.style.display="none";
    }
    if (radioISValid && !checkboxIsValid){
        if(valor.value == "FRUTA"){
            error_checkbox_fruta.style.display="block";
        }
        if(valor.value == "VERDURA"){
            error_checkbox_verdura.style.display="block";
        }
    } else {
        error_checkbox_fruta.style.display="none";
        error_checkbox_verdura.style.display="none";
    }
    console.log(descIsValid)
    if (!descIsValid){
        error_descripcion.style.display = "block";
    } else {
        error_descripcion.style.display = "none";
    }
    if (!fotosIsValid){
        error_fotos.style.display="block";
    }else{
        error_fotos.style.display="none";
    }
    if (!nombreIsValid){
        error_nombre.style.display="block";
    } else{
        error_nombre.style.display="none";
    }
    if(!emailIsValid){
        error_email.style.display= "block";
    } else{
        error_email.style.display="none";
    }
    if(!telefonoIsValid){
        error_telefono.style.display ="block";
    } else {
        error_telefono.style.display = "none";
    }

}




// ----- RECUPERAR INFO DE HTML ----------
const radio_fruta = document.getElementById("fruta");
const radio_verdura = document.getElementById("verdura");
const fruta_o_verdura = document.querySelector("#Tipo-fruta-o-verdura");
const esconder_fruta = document.getElementById("esconder-fruta")
const esconder_verdura = document.getElementById("esconder-verdura")
const esconder_error_fruta=  document.getElementById("error-checkbox-fruta");
const esconder_error_verdura=  document.getElementById("error-checkbox-verdura");
//---checkboxex---
const producto_fruta = document.getElementById("checkbox-producto-fruta").getElementsByTagName("input");
const producto_verdura = document.getElementById("checkbox-producto-verdura").getElementsByTagName("input");



const button = document.getElementById("submit-button");

//------ Esconde los productos -------
//producto_fruta.style.display="none";
//producto_verdura.style.display="none";


// ------- EVENTOS ----------
fruta_o_verdura.addEventListener("change",isChecked);

button.addEventListener("click",validate);


// ----- LIMITAR CHECKBOXES --------



for (let i = 0; i < producto_fruta.length; i++) {
    producto_fruta[i].onclick = function() {
        let checkedcount = 0;
            for (let i = 0; i < producto_fruta.length; i++) {
            checkedcount += (producto_fruta[i].checked) ? 1 : 0;
        }
        if (checkedcount > limit) {
            this.checked = false;
        }
    }
}
for (let i = 0; i < producto_verdura.length; i++) {
    producto_verdura[i].onclick = function() {
        let checkedcount = 0;
            for (let i = 0; i < producto_verdura.length; i++) {
            checkedcount += (producto_verdura[i].checked) ? 1 : 0;
        }
        if (checkedcount > limit) {
            this.checked = false;
        }
    }
}
