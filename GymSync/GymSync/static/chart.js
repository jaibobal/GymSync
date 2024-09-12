function showStats() {
    fetch('/stats')
        .then(response => response.json())
        .then(data => {
            const ctx1 = document.getElementById('benchChart').getContext('2d');
            new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: data.weeks,
                    datasets: [{
                        label: 'Bench Press',
                        data: data.bench,
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {}
            });

            const ctx2 = document.getElementById('squatChart').getContext('2d');
            new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: data.weeks,
                    datasets: [{
                        label: 'Squat',
                        data: data.squat,
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {}
            });

            const ctx3 = document.getElementById('deadliftChart').getContext('2d');
            new Chart(ctx3, {
                type: 'line',
                data: {
                    labels: data.weeks,
                    datasets: [{
                        label: 'Deadlift',
                        data: data.deadlift,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {}
            });

            const ctx4 = document.getElementById('totalChart').getContext('2d');
            new Chart(ctx4, {
                type: 'line',
                data: {
                    labels: data.weeks,
                    datasets: [{
                        label: 'Total',
                        data: data.total,
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {}
            });

            document.getElementById('stats').style.display = 'block';
        });
}
