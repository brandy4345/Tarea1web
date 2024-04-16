for (let i = 1; i <= 5; i++) {
    const row = document.getElementById('fila'+i);
    row.addEventListener("click", () => {
        const link = row.querySelector("a").href
        window.location.href = link;
    });
  }