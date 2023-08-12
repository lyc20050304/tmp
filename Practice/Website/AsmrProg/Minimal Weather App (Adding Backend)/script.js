const apiKey = "5783b40b84fce9e72a46ac821007db16";

const weatherIconMap = {
  "01d": "sun",
  "01n": "moon",
  "02d": "sun",
  "02n": "moon",
  "03d": "cloud",
  "03n": "cloud",
  "04d": "cloud",
  "04n": "cloud",
  "09d": "cloud-rain",
  "09n": "cloud-rain",
  "10d": "cloud-rain",
  "10n": "cloud-rain",
  "11d": "cloud-lightning",
  "11n": "cloud-lightning",
  "13d": "cloud-snow",
  "13n": "cloud-snow",
  "50d": "water",
  "50n": "water",
};

function fetchWeatherData(location) {
  const apiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${location}&appid=${apiKey}&units=metric`;
  fetch(apiUrl).then(response => response.json()).then(data => {
    const todayInfo = document.querySelector(".today-info");
    todayInfo.querySelector('h2').textContent = new Date().toLocaleDateString('en', { weekday: 'long' });
    todayInfo.querySelector('span').textContent = new Date().toLocaleDateString('en', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    });

    const locationElement = document.querySelector('.today-info > div > span');
    locationElement.textContent = `${data.city.name}, ${data.city.country}`;

    const todayWeatherIcon = document.querySelector(".today-weather i");
    const todayWeatherIconCode = data.list[0].weather[0].icon;
    todayWeatherIcon.className = `bx bx-${weatherIconMap[todayWeatherIconCode]}`;

    const todayTemp = document.querySelector(".weather-temp");
    const todayTemperature = `${Math.round(data.list[0].main.temp)}°C`;
    todayTemp.textContent = todayTemperature;

    const weatherDescriptionElement = document.querySelector('.today-weather h3');
    const todayWeather = data.list[0].weather[0].description;
    weatherDescriptionElement.textContent = todayWeather;

    const dayInfoContainer = document.querySelector('.day-info');
    const todayPrecipitation = `${data.list[0].pop}%`;
    const todayHumidity = `${data.list[0].main.humidity}%`;
    const todayWindSpeed = `${data.list[0].wind.speed} km/h`;
    dayInfoContainer.innerHTML = `
      <div>
        <span class="title">PRECIPITATION</span>
        <span class="value">${todayPrecipitation}</span>
      </div>

      <div>
        <span class="title">HUMIDITY</span>
        <span class="value">${todayHumidity}</span>
      </div>

      <div>
        <span class="title">WIND SPEED</span>
        <span class="value">${todayWindSpeed}</span>
      </div>
    `;

    const daysList = document.querySelector(".days-list");
    const nextDaysData = data.list.slice(1);
    const uniqueDays = new Set();
    const today = new Date();
    let count = 0;
    daysList.innerHTML = '';
    for (const dayData of nextDaysData) {
      const forecastDate = new Date(dayData.dt_txt);
      const dayAbbreviation = forecastDate.toLocaleDateString('en', { weekday: 'short' });
      const iconCode = dayData.weather[0].icon;
      const dayTemp = `${Math.round(dayData.main.temp)}°C`;
      if (!uniqueDays.has(dayAbbreviation) && forecastDate.getDate() !== today.getDate()) {
        uniqueDays.add(dayAbbreviation);
        daysList.innerHTML += `
          <li>
            <i class="bx bx-${weatherIconMap[iconCode]}"></i>
            <span>${dayAbbreviation}</span>
            <span class="day-temp">${dayTemp}</span>
          </li>
        `;
        count++;
      }
      if(count === 4) break;
    }
  }).catch(error => {
    alert(`Error fetching weather data: ${error} (Api Error)`);
  })
}
document.addEventListener('DOMContentLoaded', () => {
  const defaultLocation = 'Germany';
  fetchWeatherData(defaultLocation);
})
const locButton = document.querySelector(".loc-button");
locButton.addEventListener('click', () => {
  const location = prompt('Enter a location :');
  if (!location) return;
  fetchWeatherData(location);
})