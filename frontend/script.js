async function fetchData() {
    const res=await fetch ("");
    const record=await res.json();
    document.getElementById("Suspicion").innerHTML=record.data[0].suspicionScore;
    document.getElementById("Rag").innerHTML=record.data[0].rag;
fetchData();
}