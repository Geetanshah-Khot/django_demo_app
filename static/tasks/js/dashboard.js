async function loadData(){
const resp = await fetch('/api/tasks/stats/');
const data = await resp.json();
const labels = data.map(d => d.status);
const counts = data.map(d => d.count);


const ctx = document.getElementById('statusChart').getContext('2d');
new Chart(ctx, {
type: 'bar',
data: {
labels: labels,
datasets: [{
label: 'Tasks',
data: counts,
}]
},
});
}


loadData();