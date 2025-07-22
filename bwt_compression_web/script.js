document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const dna = document.getElementById('dnaInput').value;
    fetch('/compress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ dna })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('resultText').textContent = data.compressed || 'Error occurred';
    })
    .catch(err => console.error('Error:', err));
});