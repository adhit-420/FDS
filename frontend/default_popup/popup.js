// popup.js

// This function runs when the popup HTML has loaded
document.addEventListener('DOMContentLoaded', function() {
    // Add your code here to interact with elements in the popup HTML
});// popup.js

// This function runs when the popup HTML has loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get references to elements in the popup HTML
    const greetingElement = document.getElementById('greeting');
    const inputElement = document.getElementById('input');
    const buttonElement = document.getElementById('button');

    // Add event listener to the button
    buttonElement.addEventListener('click', function() {
        // Get the input value
        const inputValue = inputElement.value;

        // Perform some action based on the input value
        if (inputValue === 'hello') {
            greetingElement.textContent = 'Hello, world!';
        } else {
            greetingElement.textContent = 'Invalid input';
        }
    });
});