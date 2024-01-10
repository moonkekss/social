function toggleEmail() {
    const hiddenEmail = document.getElementById("hiddenEmail");
    const showEmailBtn = document.getElementById("showEmailBtn");

    if (hiddenEmail.style.display === "none") {
        hiddenEmail.style.display = "inline";
        showEmailBtn.textContent = "Скрыть";
    } else {
        hiddenEmail.style.display = "none";
        showEmailBtn.textContent = "Показать";
    }
}