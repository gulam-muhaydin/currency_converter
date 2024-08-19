function fetchRate() {
    fetch('/get_rate')
        .then(response => response.json())
        .then(data => {
            document.getElementById('rate').innerText = `1 OMR = ${data.rate} PKR`;
        })
        .catch(error => {
            console.error('Error fetching the rate:', error);
            document.getElementById('rate').innerText = 'Failed to load rate';
        });
}

// Fetch the rate when the page loads
fetchRate();
