document.addEventListener("DOMContentLoaded", function () {
    const numeros = document.querySelectorAll(".num");

    numeros.forEach(el => {
      if (el.textContent.includes(".")) {
        el.textContent = el.textContent.replace(".", ",");
      }
    });
  });