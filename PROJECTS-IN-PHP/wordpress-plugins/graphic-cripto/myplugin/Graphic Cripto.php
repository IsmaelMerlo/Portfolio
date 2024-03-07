<?php
/**
* Plugin Name: Graphic Cripto
* Plugin URI: https://www.myplugin.com/
* Description: Graphic Cripto is a plugin for show the criptocoins in real time.
* Version: 1.0
* Author: Ismael Merlo
* Author URI: https://ismaelmerlo.netlify.app
**/


function graphiccripto_shortcode_function(){
    ob_start();
    ?>
    <!DOCTYPE html>
<html>
<head>
	<title>Criptomonedas</title>
	<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
	<style>
		.container {
			display: flex;
			justify-content: space-between;
			align-items: flex-start;
			flex-wrap: wrap;
			max-width: 1000px;
			margin: 0 auto;
			padding: 20px;
			box-sizing: border-box;
		}

		.chart-container {
			display: flex;
			flex-direction: column;
			width: 400px;
			padding-right: 5px;
			box-sizing: border-box;
		}

		.chart-container canvas {
			width: 100%;
			height: 300px;
		}

		.table-container {
			width: 5%;
			box-sizing: border-box;
		}

		table {
			border-collapse: collapse;
			width: 80%;
			font-family: Arial, Helvetica, sans-serif;
			font-size: 12px;
			text-align: center;
			background-color: #f2f2f2;
			border: 1px solid #ddd;
		}

		th, td {
			padding: 5px;
			border: 1px solid #ddd;
		}

		th {
			background-color: #d9d9d9;
			font-weight: bold;
		}

		tbody tr:nth-child(even) {
			background-color: #e6e6e6;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="chart-container">
			<canvas id="myChart"></canvas>
		</div>
		<div class="table-container">
			<table>
				<thead>
					<tr>
						<th>Moneda</th>
						<th>Precio</th>
						<th>Volumen (24h)</th>
						<th>Cambio</th>
					</tr>
				</thead>
				<tbody id="table-body">
				</tbody>
			</table>
		</div>
		<div class="data-column">
			<div id="data"></div>
		</div>
	</div>
    <script>
    // Hacemos la solicitud a la API de Coingecko
    fetch("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cbitcoin-cash%2Cdogecoin%2Clitecoin%2Clitecoin%2Cdash%2Cethereum-classic%2Czcash%2Cravencoin%2Cnamecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en")
    .then(response => response.json())
    .then(data => {
	// Creamos un objeto con los datos que necesitamos de cada moneda
	const coins = data.map(coin => ({
		name: coin.name,
		price: coin.current_price,
		volume: coin.total_volume,
		change: coin.price_change_percentage_24h,
		icon: coin.image
	}));

	// Creamos un objeto con los colores de cada moneda
	const colors = {
		"Bitcoin": "#F7931A",
		"Dash": "#627EEA",
		"Namecoin": "#008DE4",
		"Bitcoincash": "#90EE90",
		"Ethereum Classic": "darkgreen",
		"Dogecoin": "#4BA2F2",
        "Litecoin": "grey",
        "Zcash": "yellow",
        "Raven": "black"
	};

	// Creamos un array con los datos de la gráfica donut
	const chartData = coins.map(coin => ({
		label: coin.name,
		value: coin.price,
		color: colors[coin.name]
	}));

	// Creamos la gráfica donut con Chart.js
	const ctx = document.getElementById("myChart").getContext("2d");
	const myChart = new Chart(ctx, {
	    type: 'doughnut',
	    data: {
	        labels: chartData.map(data => data.label),
	        datasets: [{
	            data: chartData.map(data => data.value),
	            backgroundColor: chartData.map(data => data.color)
	        }]
	    },
	    options: {
	        responsive: true
	    }
	});

	// Mostramos los datos de cada moneda en la tabla
    const tableBody = document.getElementById("table-body");
        coins.forEach(coin => {
    const row = document.createElement("tr");
        row.innerHTML = `
    <td><img src="${coin.icon}" alt="${coin.name}" width="28" height="28"> ${coin.name}</td>
    <td>${coin.price}</td>
    <td>${coin.volume}</td>
    <td>${coin.change}%</td>
    `;
    tableBody.appendChild(row);
    });
  })
.catch(error => {
	console.error(error);
});
    </script>
</body>
</html>
    <?php
    return ob_get_clean();
}
add_shortcode('graphiccripto_shortcode', 'graphiccripto_shortcode_function');
// Shortcode: [graphiccripto_shortcode]
?>