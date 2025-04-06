console.log("Form submitted");

document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    console.log("Sending video to backend...");

    const videoInput = document.getElementById("videoInput");
    const videoFile = videoInput.files[0];

    if (!videoFile) {
        alert("Please select a video first.");
        return;
    }

    const formData = new FormData();
    formData.append("video", videoFile);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        console.log("📦 Response received:", result);

        if (result.error) {
            alert("Upload failed: " + result.error);
            return;
        }

        const outputVideo = document.getElementById("outputVideo");
        const plateList = document.getElementById("plateList");

        outputVideo.src = result.output;
        outputVideo.style.display = "block";

        plateList.innerHTML = "";
        result.plates.forEach(plate => {
            const li = document.createElement("li");
            li.textContent = plate;
            plateList.appendChild(li);
        });
    } catch (err) {
        console.error("❌ Fetch failed:", err);
    }
});
