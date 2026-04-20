const api_url = "http://127.0.0.1:5000";

// Load locations on page load
window.onload = function () {
    fetch(api_url + "/get_location_names")
        .then(response => response.json())
        .then(data => {
            const locations = data.locations;
            const locationSelect = document.getElementById("location");

            locations.forEach(loc => {
                let option = document.createElement("option");
                option.value = loc;
                option.text = loc;
                locationSelect.appendChild(option);
            });
        });
};

function predictPrice() {
    const sqft = document.getElementById("sqft").value;
    const bhk = document.getElementById("bhk").value;
    const bath = document.getElementById("bath").value;
    const location = document.getElementById("location").value;

    const formData = new FormData();
    formData.append("total_sqft", sqft);
    formData.append("bhk", bhk);
    formData.append("bath", bath);
    formData.append("location", location);

    fetch(api_url + "/predict_home_price", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "Estimated Price: ₹ " + data.estimated_price + " Lakhs";
    })
    .catch(err => {
        console.error(err);
        alert("Error connecting to server");
    });
}
