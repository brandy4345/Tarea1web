let num  = 0;
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
    const nombre = info[4]

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
    const p5 = document.createElement("p")
    p5.innerText = nombre
    td5.appendChild(p5)

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

fetchAJAX('http://localhost:5000/get-pedidos/'+0);


const anterior = document.getElementById("anterior");
const siguiente =  document.getElementById("siguiente");

const restarUno =() =>{
    if (num<=0){
        num = 0
    }
    else {
        num--;
        fetchAJAX('http://localhost:5000/get-pedidos/'+num);
    }
}
const sumarUno =() =>{
    if (num<0){
        num = 0
    }
    else {
        num++;
        fetchAJAX('http://localhost:5000/get-pedidos/'+num);
    }
}

anterior.addEventListener("click",restarUno)
siguiente.addEventListener("click",sumarUno)