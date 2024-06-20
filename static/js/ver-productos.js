num = 0
let hola; 
for (let i = 1; i <= 5; i++) {
    const row = document.getElementById('fila'+i);
    row.addEventListener("click", () => {
        const link = row.querySelector("a").href
        window.location.href = link;
    });
  }
const table = document.getElementById("tabla")
const createRow= (info) => {
    const tipo = info[0]
    const producto = info[1]
    const region = info[2]
    const comuna = info[3]
    const foto = info[4]
    console.log(info)

    const row = document.createElement("tr");

    const td1 = document.createElement("td");
    const p1 = document.createElement("p")
    p1.innerText = tipo
    td1.appendChild(p1)

    const td2 = document.createElement("td");
    const p2 = document.createElement("p")
    p2.innerText = producto
    td2.appendChild(p2)

    const td3 = document.createElement("td");
    const p3 = document.createElement("p")
    p3.innerText = region
    td3.appendChild(p3)

    const td4 = document.createElement("td");
    const p4 = document.createElement("p")
    p4.innerText = comuna
    td4.appendChild(p4)

    const td5 = document.createElement("td");
    const img =  document.createElement("img");
    img.src = foto;
    img.alt = "foto_producto";

    td5.appendChild(img);
    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    row.appendChild(td5);
    table.append(row);
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
            for (i=0; i< ajaxResponse.length ;i++) {
                hola = ajaxResponse
                createRow(ajaxResponse[i])
            }

        })
        .catch((error) => {
            console.error(
                "There has been a problem with your fetch operation",
                error
            );
        });
}

fetchAJAX('http://localhost:5000/get-productos/'+num);