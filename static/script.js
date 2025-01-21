document.addEventListener("DOMContentLoaded", function () {
    // effect to inputs
    const inputs = document.querySelectorAll("input");
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.boxShadow = "0 0 15px rgba(138, 43, 226, 0.4)";
        });
        input.addEventListener("blur", () => {
            input.style.boxShadow = "none";
        });
    });

    // success message 
    const form = document.getElementById("geneticForm");
    form.addEventListener("submit", function (e) {
        alert("Processing your genetic simulation...");
    });
});
