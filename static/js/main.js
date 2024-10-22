function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.prediction) {
            document.getElementById('result').innerText = `Predicted Fish: ${data.prediction}`;
        } else {
            document.getElementById('result').innerText = 'Error: No prediction available';
        }
    })
    .catch(error => console.error('Error:', error));
}
