function initCountdown(selector, targetDate) {
  window.addEventListener("load", () => {
    const el = document.querySelector(selector);
    el.classList.add("countdown");

    const update = () => {
      const totalSeconds = (targetDate - new Date()) / 1000;
      if (totalSeconds <= 0) {
        el.innerHTML = "";
        return;
      }

      const days = Math.floor(totalSeconds / 3600 / 24)
        .toString()
        .padStart(2, "0");

      const hours = Math.floor((totalSeconds - days * 24 * 3600) / 3600)
        .toString()
        .padStart(2, "0");

      const minutes = Math.floor(
        (totalSeconds - days * 24 * 3600 - hours * 3600) / 60,
      )
        .toString()
        .padStart(2, "0");

      const seconds = Math.floor(
        totalSeconds - days * 24 * 3600 - hours * 3600 - minutes * 60,
      )
        .toString()
        .padStart(2, "0");

      el.innerHTML = `
<span class="component">
  <span class="number">${days}</span>
  <span class="text">ngày</span>
</span>
<span class="component">
  <span class="number">${hours}</span>
  <span class="text">giờ</span>
</span>
<span class="component">
  <span class="number">${minutes}</span>
  <span class="text">phút</span>
</span>
<span class="component">
  <span class="number">${seconds}</span>
  <span class="text">giây</span>
</span>
`;
    };

    update();
    setInterval(update, 1000);
  });
}
