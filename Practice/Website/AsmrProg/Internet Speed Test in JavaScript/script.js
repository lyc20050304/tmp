const imageApi = "https://source.unsplash.com/random?topic=nature";

const info = document.getElementById("info");
const mbSpeed = document.getElementById("mbs");
const kbSpeed = document.getElementById("kbs");
const bitSpeed = document.getElementById("bits");

let startTime, endTime;
let image = new Image();
let imageSize = "";

let totalBitSpeed = 0;
let totalKbSpeed = 0;
let totalMbSpeed = 0;
let testCompleted = 0;
let numTests = 5;

async function init() {
  info.innerHTML = "Testing...";
  startTime = new Date().getTime();
  image.src = imageApi;
}
function calculateSpeed() {
  const loadedBits = imageSize * 8;
  const timeDuration = (endTime - startTime) / 1000;
  const speedInBts = loadedBits / timeDuration;
  const speedInKbs = speedInBts / 1024;
  const speedInMbs = speedInKbs / 1024;

  totalBitSpeed += speedInBts;
  totalKbSpeed += speedInKbs;
  totalMbSpeed += speedInMbs;

  testCompleted++;

  if (testCompleted === numTests) {
    const averageSpeedInBps = (totalBitSpeed / numTests).toFixed(2);
    const averageSpeedInKbps = (totalKbSpeed / numTests).toFixed(2);
    const averageSppedInMbps = (totalMbSpeed / numTests).toFixed(2);

    bitSpeed.innerHTML += `${averageSpeedInBps}`;
    kbSpeed.innerHTML += `${averageSpeedInKbps}`;
    mbSpeed.innerHTML += `${averageSppedInMbps}`;
    info.innerHTML = "Test Completed!";
  } else {
    startTime = new Date().getTime();
    image.src = imageApi;
  }
}
window.addEventListener("load", () => {
  for (let i = 0; i < numTests; i++) {
    init();
  }
});
image.addEventListener("load", async () => {
  endTime = new Date().getTime();

  await fetch(imageApi).then((response) => {
    imageSize = response.headers.get("content-length");
    calculateSpeed();
  });
});
