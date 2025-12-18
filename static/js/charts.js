document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('expenseChart');
    if (!canvas) return;

    // CATEGORY_LABELS and CATEGORY_VALUES come from dashboard.html
    if (typeof CATEGORY_LABELS === 'undefined' || typeof CATEGORY_VALUES === 'undefined') {
        return;
    }

    const ctx = canvas.getContext('2d');

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: CATEGORY_LABELS,
            datasets: [{
                data: CATEGORY_VALUES,
                backgroundColor: [
                    '#ff6384', '#36a2eb', '#ffcd56',
                    '#4caf50', '#9c27b0', '#ff9800'
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
});
