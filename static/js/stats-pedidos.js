Highcharts.chart("container2",{
    chart: {
        type: "pie"
    },
    title: {
        text: "Tipos de fruta o verduras"
    },
    series: [
        {
          name: "Cantidad",
          data: [
          ],
        },
      ]
});

let fetchAJAX = (url) => {
    fetch(url)
        .then((response) =>{
            if(!response.ok){
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then((ajaxResponse) => {
            // Get the chart by ID
            const chart = Highcharts.charts.find(
                (chart) => chart && chart.renderTo.id === "container2"
            );
        
            // Update the chart with new data
            chart.update({
                series: [
                {
                    data: ajaxResponse,
                },
                ],
            });
            })
        .catch((error) => {
            console.error(
                "There has been a problem with your fetch operation",
                error
            );
        });
}
fetchAJAX('http://localhost:5000/get-pedido-data');