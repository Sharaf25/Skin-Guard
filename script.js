// Event listener for the file input
document.getElementById("imageUpload").addEventListener("change", function (event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const uploadBox = document.querySelector(".upload-box");
            uploadBox.style.backgroundImage = `url(${e.target.result})`;
            uploadBox.style.backgroundSize = "cover";
            uploadBox.style.backgroundPosition = "center";
            uploadBox.innerHTML = "";

            // Show the reset button
            document.getElementById("reset-button").style.display = "block";
        };
        reader.readAsDataURL(file);

        // Upload the image to the backend
        uploadImage(file);
    }
});

// Function to upload the image to the backend
function uploadImage(file) {
    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.result) {
                document.getElementById("result-text").innerText = `Analysis: ${data.result}`;
                document.getElementById("info-text").innerText = data.info || "No additional information available.";
            } else {
                document.getElementById("result-text").innerText = "Error processing image.";
                document.getElementById("info-text").innerText = "No additional information available.";
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            document.getElementById("result-text").innerText = "Error connecting to server.";
            document.getElementById("info-text").innerText = "No additional information available.";
        });
}

// Reset button functionality
document.getElementById("reset-button").addEventListener("click", function () {
    const uploadBox = document.querySelector(".upload-box");
    const fileInput = document.getElementById("imageUpload");
    const resultText = document.getElementById("result-text");
    const infoText = document.getElementById("info-text");

    // Reset the upload box
    uploadBox.style.backgroundImage = "none"; // Clear the background image
    uploadBox.innerHTML = "<p>Upload The Image Here</p>"; // Restore placeholder text

    // Clear the file input
    fileInput.value = ""; 

    // Reset the result text
    resultText.innerText = "Waiting for image..."; 

    // Reset the additional information text
    infoText.innerText = "No additional information available.";
});