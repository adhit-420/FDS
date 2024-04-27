// async function to fetch data from the API endpoint and update HTML elements
async function fetchData() {
    try {
        // Get the current URL of the page
        const currentURL = window.location.href;
        
        // Make a GET request to your FastAPI endpoint with the current URL as input
       const res = await fetch(`http://localhost:8000/phish_model?url=${encodeURIComponent(currentURL)}`);
       //const youtubeURL = 'https://www.youtube.com'; // URL of YouTube
       //const res = await fetch(`http://localhost:8000/phish_model?url=${encodeURIComponent(youtubeURL)}`);
        if (!res.ok) {
            throw new Error('Network response was not ok');
        }

        const record = await res.json();
        // Update HTML elements with fetched data
        document.getElementById("Suspicion").innerHTML = record.proba;
        document.getElementById("Rag").innerHTML = record.pred;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Call fetchData function when the page loads
window.onload = function () {
    fetchData();
};


// Call fetchData function when the page loads
window.onload = function () {
    fetchData();
};
document.addEventListener('DOMContentLoaded', function() {
    var reportButton = document.getElementById('reportButton');
    reportButton.addEventListener('click', function() {
        chrome.tabs.create({ url: 'https://www.cybercrime.gov.in/Webform/Accept.aspx' });
    });
})