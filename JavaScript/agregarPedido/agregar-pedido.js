// ------ FUNCIONES ---------
const isChecked = () => { 
    if (radio_fruta.checked){
        producto_fruta.style.display="block";
        producto_verdura.style.display="none";
    }
    else if (radio_verdura.checked){
        producto_fruta.style.display="none";
        producto_verdura.style.display="block";
        console.log("verdura esta checked");
    }
}


// ----- RECUPERAR INFO DE HTML ----------
const radio_fruta = document.getElementById("fruta");
const radio_verdura = document.getElementById("verdura");
const fruta_o_verdura = document.querySelector("#Tipo-fruta-o-verdura");

const producto_fruta = document.getElementById("checkbox-producto-fruta");
const producto_verdura = document.getElementById("checkbox-producto-verdura");

//------ Esconde los productos -------
//producto_fruta.style.display="none";
//producto_verdura.style.display="none";


// ------- EVENTOS ----------
fruta_o_verdura.addEventListener("change",isChecked);

