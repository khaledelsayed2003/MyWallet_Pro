document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("expenseChart");
  if (!canvas) return;

  const dataEl = document.getElementById("chartData");
  if (!dataEl) return;

  const labelsRaw = dataEl.getAttribute("data-labels");
  const valuesRaw = dataEl.getAttribute("data-values");

  if (!labelsRaw || !valuesRaw) return;

  const labels = JSON.parse(labelsRaw);
  const values = JSON.parse(valuesRaw);

  const ctx = canvas.getContext("2d");

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: labels,
      datasets: [
        {
          data: values,
          backgroundColor: [
            "#ff6384",
            "#36a2eb",
            "#ffcd56",
            "#4caf50",
            "#9c27b0",
            "#ff9800",
          ],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "bottom" },
      },
    },
  });
});
