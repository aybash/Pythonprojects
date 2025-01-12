document.getElementById('search-btn').addEventListener('click', () => {
    const city = document.getElementById('city-input').value;
    fetchWeather({ city });
});

document.getElementById('location-btn').addEventListener('click', () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                fetchWeather({ latitude, longitude });
            },
            () => {
                showError("Unable to access location!");
            }
        );
    } else {
        showError("Geolocation is not supported by this browser!");
    }
});

function fetchWeather(data) {
    const errorMessage = document.getElementById('error-message');
    const weatherResult = document.getElementById('weather-result');
    const forecastDiv = document.getElementById('forecast');

    errorMessage.classList.add('hidden');
    weatherResult.classList.add('hidden');
    forecastDiv.innerHTML = "";

    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showError(data.error);
        } else {
            document.getElementById('city-name').textContent = data.city;
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature}°C`;
            document.getElementById('description').textContent = data.description;
            document.getElementById('weather-icon').src = `http://openweathermap.org/img/wn/${data.icon}.png`;
            weatherResult.classList.remove('hidden');

            data.forecast.forEach(day => {
                const date = new Date(day.dt * 1000).toLocaleDateString('en-US', { weekday: 'short' });
                const forecastItem = `
                    <div class="forecast-day">
                        <p>${date}</p>
                        <img src="http://openweathermap.org/img/wn/${day.weather[0].icon}.png" alt="${day.weather[0].description}">
                        <p>${day.temp.day}°C</p>
                    </div>
                `;
                forecastDiv.innerHTML += forecastItem;
            });
        }
    })
    .catch(() => {
        showError("An error occurred while fetching the weather data!");
    });
}

function showError(message) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
}
