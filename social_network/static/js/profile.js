function toggleEmail() {
    var emailBlock = document.getElementById("emailBlock");
    var hiddenEmail = document.getElementById("hiddenEmail");
    var showEmailBtn = document.getElementById("showEmailBtn");

    if (hiddenEmail.style.display === "none") {
        hiddenEmail.style.display = "inline";
        showEmailBtn.innerText = "Скрыть";
    }

    else {
        hiddenEmail.style.display = "none";
        showEmailBtn.innerHTML = "Показать";
    }
}