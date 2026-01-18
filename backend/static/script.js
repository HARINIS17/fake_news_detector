function checkNews() {
  const newsText = document.getElementById("news").value;

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ news: newsText })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("result").innerText =
      "Prediction: " + data.prediction;
  })
  .catch(error => {
    console.error("Error:", error);
    document.getElementById("result").innerText =
      "Error connecting to backend";
  });
}
