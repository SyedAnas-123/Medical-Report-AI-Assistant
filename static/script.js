document.addEventListener("DOMContentLoaded", function () {
    const formElements = document.querySelectorAll("input, select");

    // Scale effect on input focus
    formElements.forEach(element => {
        element.addEventListener("focus", () => {
            element.style.transform = "scale(1.05)";
        });

        element.addEventListener("blur", () => {
            element.style.transform = "scale(1)";
        });

        // Live validation to prevent empty input
        element.addEventListener("input", () => {
            if (element.value.trim() === "") {
                element.style.border = "2px solid red";
            } else {
                element.style.border = "2px solid #ccc";
            }
        });
    });

    // Restrict 'ca' field (0-3) to valid values
    const caInput = document.querySelector("input[name='ca']");
    if (caInput) {
        caInput.addEventListener("input", () => {
            let value = parseInt(caInput.value, 10);
            if (value < 0 || value > 3) {
                caInput.value = ""; // Reset invalid input
                alert("Please enter a valid number (0 to 3) for major vessels.");
            }
        });
    }

    // Smooth background animation effect
    let background = document.querySelector(".background");
    document.addEventListener("mousemove", (event) => {
        let moveX = (event.clientX / window.innerWidth) * 50;
        let moveY = (event.clientY / window.innerHeight) * 50;
        background.style.backgroundPosition = `${moveX}px ${moveY}px`;
    });

    // Ensure the form submits correctly
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        let valid = true;

        // Check for empty required fields
        formElements.forEach(element => {
            if (element.value.trim() === "") {
                element.style.border = "2px solid red";
                valid = false;
            }
        });

        if (!valid) {
            event.preventDefault();
            alert("Please fill in all required fields before submitting.");
        }
    });
});
