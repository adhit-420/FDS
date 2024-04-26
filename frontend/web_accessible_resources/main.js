// main.js

// Function to perform backend action and update displays
function performBackendAction() {
    fetch('http://localhost:8000/perform_action')
        .then(response => response.text())
        .then(result => {
            // Display result in both displays
            document.getElementById('display1').textContent = result;
            document.getElementById('display2').textContent = result;
        })
        .catch(error => console.error('Error:', error));
}

// Function to handle button click event
function handleButtonClick() {
    document.getElementById('actionButton').addEventListener('click', function () {
        performBackendAction();
    });
}

// Initialize the extension
function initializeExtension() {
    handleButtonClick();
}

// Call initializeExtension when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function () {
    initializeExtension();
});
