const eventBox = document.getElementById('event-box');
console.log(eventBox.textContent);
const countdownBox = document.getElementById('countdown-box');

console.log(eventBox.textContent);
const eventDate = Date.parse(eventBox.textContent);
// console.log(eventDate)


const myCountdown = setInterval(() => {
  const now = new Date().getTime();

  const diff = eventDate - now;


  const d = Math.floor(diff / (1000 * 60 * 60 * 24));
  const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  const s = Math.floor((diff % (1000 * 60)) / 1000);

  if (diff > 0) {
    countdownBox.innerHTML = d + " days, " + h + " hours, " + m + " minutes, " + s + " seconds.";
  } else {
    clearInterval(myCountdown);
    countdownBox.innerHTML = "Countdown Completed!";
  }
}, 1000);
