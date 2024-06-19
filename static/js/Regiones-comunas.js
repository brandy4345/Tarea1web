let comunasObj = null;

const selectorRegion = document.getElementById("regiones");
const selectorComuna = document.getElementById("comunas");

const predeterminado1 = document.createElement("option");
const predeterminado2 = document.createElement("option");


predeterminado1.value = "-1";
predeterminado1.innerText = "Seleccione su región";
predeterminado2.value = "-1";
predeterminado2.innerText = "Seleccione su comuna";
selectorRegion.append(predeterminado1);
selectorComuna.append(predeterminado2);

const actualizaRegion = () =>{  
    for (const regionId in comunasObj){
        const region = comunasObj[regionId];
        const opcion = document.createElement("option");
        opcion.value = regionId;
        opcion.innerText = region.nombre;
        selectorRegion.append(opcion);
    }
}

const actualizaComunas = () => {
    const a = selectorRegion.value;
    const region = comunasObj[a];

    if (selectorComuna.innerHTML.trim()!=''){
        const cantComunasBorrar = selectorComuna.children.length;
        for(let j = 0; j<cantComunasBorrar; j++){
            selectorComuna.lastChild.remove();
        }
    }
    selectorComuna.append(predeterminado2);
    if (region){
        for (const comuna of region.comunas){
            const opcion = document.createElement("option");
            opcion.value = comuna.id;
            opcion.innerText = comuna.nombre;
            selectorComuna.append(opcion);
        }
    }
}

let fetchAJAX = (url) => {
    fetch(url)
        .then((response) =>{
            if(!response.ok){
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((ajaxResponse) => {
            comunasObj = ajaxResponse;
            actualizaRegion();
        })
        .catch((error) => {
            console.error(
                "There has been a problem with your fetch operation",
                error
            );
        });
}

fetchAJAX('http://localhost:5000/region-comunas');



selectorRegion.addEventListener("change",actualizaComunas);