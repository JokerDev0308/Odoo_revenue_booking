document.addEventListener('DOMContentLoaded', function() {
    var ctxRevenue = document.getElementById('revenueChart').getContext('2d');
    var revenueChart = new Chart(ctxRevenue, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April'],
            datasets: [{
                label: 'Revenue',
                data: [1200, 1900, 3000, 5000],
                borderColor: '#28a745',
                fill: false
            }]
        }
    });

    var ctxBooking = document.getElementById('bookingChart').getContext('2d');
    var bookingChart = new Chart(ctxBooking, {
        type: 'pie',
        data: {
            labels: ['Cricket', 'Badminton', 'Football'],
            datasets: [{
                label: 'Bookings',
                data: [10, 20, 30],
                backgroundColor: ['#ff6384', '#36a2eb', '#ffce56']
            }]
        }
    });
});
