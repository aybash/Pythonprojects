from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_openweathermap_api_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    data = request.json
    city = data.get('city')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    elif latitude and longitude:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    else:
        return jsonify({'error': 'City or coordinates are required!'}), 400

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        forecast_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={weather_data['coord']['lat']}&lon={weather_data['coord']['lon']}&exclude=minutely,hourly&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)

        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            return jsonify({
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'forecast': forecast_data['daily'][:5]  # 5-day forecast
            })
        else:
            return jsonify({'error': 'Failed to fetch forecast data!'}), 500
    else:
        return jsonify({'error': 'City or location not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
