const view_data = document.getElementById('view_data').innerHTML.split('[')[1].split(']')[0].split(',');
const view_products = document.getElementById('view_products').innerHTML.split('[')[1].split(']')[0].split(',');
const view_products_count = document.getElementById('view_products_count').innerHTML.split('[')[1].split(']')[0].split(',');
const ctx1 = document.getElementById('chartViewPage').getContext('2d');
const chartViewPage = new Chart(ctx1, {
    type: 'line',
    legend: {
        fontFamily: 'dashboard',
    },
    data: {
        labels: ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'],
        datasets: [{
            label: 'بازدید',
            data: view_data,
            backgroundColor: [
                '#FF2626'
            ],
            borderColor: [
                '#FF2626'
            ],
            borderWidth: 5
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    },
});

const ctx2 = document.getElementById('chartViewProducts').getContext('2d');
const chartViewProducts = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: view_products,
        datasets: [{
            label: 'بازدید',
            data: view_products_count,
            backgroundColor: [
                '#FF2626'
            ]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});