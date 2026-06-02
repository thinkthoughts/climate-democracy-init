document.addEventListener("DOMContentLoaded", () => {
  const target = document.getElementById("qr-container");

  if (!target) return;

  new QRCode(target, {
    text: window.location.href,
    width: 140,
    height: 140,
    correctLevel: QRCode.CorrectLevel.M
  });
});
