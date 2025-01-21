document.addEventListener("DOMContentLoaded", function () {
    // Add hover effect to inputs
    const inputs = document.querySelectorAll("input");
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.boxShadow = "0 0 15px rgba(138, 43, 226, 0.4)";
        });
        input.addEventListener("blur", () => {
            input.style.boxShadow = "none";
        });
    });

    // Show success message on form submission
    const form = document.getElementById("geneticForm");
    form.addEventListener("submit", function (e) {
        alert("Processing your genetic simulation...");
    });
});
