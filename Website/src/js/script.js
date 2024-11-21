// Handle index.html - Form submission
if (document.getElementById("nodeForm")) {
  document.getElementById("nodeForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const numNodes = document.getElementById("numNodes").value;
    if (!numNodes || numNodes < 1) {
      alert("Please enter a valid number of sensors.");
      return;
    }
    localStorage.setItem("numNodes", numNodes);
    window.location.href = "page2.html";
  });
}

// Handle page2.html - Dynamic 3D input generation and CSV download
if (document.getElementById("pointsForm")) {
  const numNodes = localStorage.getItem("numNodes");
  const pointsContainer = document.getElementById("pointsContainer");

  // Create input fields for each node
  for (let i = 1; i <= numNodes; i++) {
    const row = document.createElement("div");
    row.innerHTML = `
      <label for="node${i}">Cord${i}:</label>
      <input type="number" class="d1" placeholder="D1" step="any" required>
      <input type="number" class="d2" placeholder="D2" step="any" required>
      <input type="number" class="d3" placeholder="D3" step="any" required>
    `;
    pointsContainer.appendChild(row);
  }

  // Handle CSV download
  document.getElementById("downloadBtn").addEventListener("click", function () {
    const rows = [];
    const d1Fields = document.querySelectorAll(".d1");
    const d2Fields = document.querySelectorAll(".d2");
    const d3Fields = document.querySelectorAll(".d3");

    // Collect data from input fields
    for (let i = 0; i < numNodes; i++) {
      const d1 = d1Fields[i].value || 0;
      const d2 = d2Fields[i].value || 0;
      const d3 = d3Fields[i].value || 0;
      rows.push([`Cord${i + 1}`, d1, d2, d3]);
    }

    // Create CSV content
    const csvContent = "data:text/csv;charset=utf-8," + 
      "Node,D1,D2,D3\n" + 
      rows.map(row => row.join(",")).join("\n");

    // Create a link to download the CSV file
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "Data_Config.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  });

  // Handle Get Results button logic (open results in a new tab)
  document.getElementById("calculateBtn").addEventListener("click", function () {
    const sensorPositions = [];
    const d1Fields = document.querySelectorAll(".d1");
    const d2Fields = document.querySelectorAll(".d2");
    const d3Fields = document.querySelectorAll(".d3");

    // Collect the sensor positions from the input fields
    for (let i = 0; i < numNodes; i++) {
      const d1 = parseFloat(d1Fields[i].value) || 0;
      const d2 = parseFloat(d2Fields[i].value) || 0;
      const d3 = parseFloat(d3Fields[i].value) || 0;

      sensorPositions.push([d1, d2, d3]);
    }

    // Save data to local storage
    localStorage.setItem("sensorPositions", JSON.stringify(sensorPositions));

    // Open result.html in a new tab
    const resultWindow = window.open("result.html", "_blank");

    // Wait for the new tab to load and then fetch the results
    resultWindow.onload = function () {
      resultWindow.fetchResults();
    };
  });
}
