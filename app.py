from flask import Flask, render_template, request, jsonify
from weather_analysis import analyze_time_series
from external_api import fetch_hourly_temperature
from analyzer import analyze_numbers
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    raw_input = request.form.get("numbers")
    if not raw_input:
        return render_template('index.html', error="Please enter numbers.")
    try:
        numbers = [float(x.strip()) for x in raw_input.split(',')]
        result = analyze_numbers(numbers)
        return render_template('results.html', results=result, numbers=numbers)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter valid numbers.")

@app.route("/test-weather")
def test_weather():
    lantitude = 40.7128
    longitude = -74.0060
    times, temperatures = fetch_hourly_temperature(lantitude, longitude)
    analysis = analyze_time_series(times, temperatures)
    return jsonify(analysis)

@app.route("/analyze-weather", methods=['POST'])
def analyze_weather():
    try:
     latitude = float(request.form.get("latitude"))
     longitude = float(request.form.get("longitude"))
    except (TypeError, ValueError):
        return render_template('weather_input.html', error="Invalid latitude or longitude.")
    
    times, temperatures = fetch_hourly_temperature(latitude, longitude)
    analysis = analyze_time_series(times, temperatures)
    return render_template('weather_analysis_results.html', analysis=analysis)

@app.route("/weather-input")
def weather_input():
    return render_template('weather_input.html')

if __name__ == '__main__':
    app.run(debug=True) 