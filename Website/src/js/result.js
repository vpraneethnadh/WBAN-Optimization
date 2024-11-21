document.addEventListener("DOMContentLoaded", function () {
  const sensorPositions = JSON.parse(localStorage.getItem("sensorPositions"));

  if (!sensorPositions) {
    document.getElementById("nonGeneticContainer").innerHTML = "<p>No sensor data found.</p>";
    document.getElementById("gaContainer").innerHTML = "<p>No sensor data found.</p>";
    return;
  }

  fetch("http://127.0.0.1:5000/optimize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ sensor_positions: sensorPositions }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const formatScientificNotation = (value) =>
        value.replace(/x 10\^(-?\d+)/, "x 10<sup>$1</sup>");

      const nonGeneticContainer = document.getElementById("nonGeneticContainer");
      nonGeneticContainer.innerHTML = `
        <h2>Non-Genetic Optimization</h2>
        <p><strong>Route:</strong> ${data.non_genetic.route.join(" -> ")}</p>
        <p><strong>Total Distance:</strong> ${data.non_genetic.distance.toFixed(2)} units</p>
        <p><strong>Total Energy:</strong> ${formatScientificNotation(data.non_genetic.energy)} Joules</p>
      `;

      const gaContainer = document.getElementById("gaContainer");
      gaContainer.innerHTML = `
        <h2>Genetic Algorithm Optimization</h2>
        <p><strong>Route:</strong> ${data.ga.route.join(" -> ")}</p>
        <p><strong>Total Distance:</strong> ${data.ga.distance.toFixed(2)} units</p>
        <p><strong>Total Energy:</strong> ${formatScientificNotation(data.ga.energy)} Joules</p>
      `;
    })
    .catch((error) => {
      console.error("An error occurred while fetching results:", error);
      document.getElementById("nonGeneticContainer").innerHTML =
        "<p>Error loading Non-Genetic results.</p>";
      document.getElementById("gaContainer").innerHTML =
        "<p>Error loading Genetic Algorithm results.</p>";
    });
});
