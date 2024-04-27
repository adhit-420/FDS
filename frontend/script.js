async function fetchData() {
    const res=await fetch ("");
    const record=await res.json();
    document.getElementById("Suspicion").innerHTML=record.data[0].suspicionScore;
    document.getElementById("Rag").innerHTML=record.data[0].rag;
fetchData();
}

document.addEventListener('DOMContentLoaded', function() {
    var reportButton = document.getElementById('reportButton');
    reportButton.addEventListener('click', function() {
        chrome.tabs.create({ url: 'https://www.cybercrime.gov.in/Webform/Accept.aspx' });
    });
})