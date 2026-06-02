document.addEventListener("DOMContentLoaded", () => {
  const target = document.getElementById("qr-container");

  if (!target || typeof QRCode === "undefined") return;

  target.innerHTML = "";

  new QRCode(target, {
    text: window.location.href,
    width: 220,
    height: 220,
    colorDark: "#000000",
    colorLight: "#ffffff",
    correctLevel: QRCode.CorrectLevel.H
  });
});
