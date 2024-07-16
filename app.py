from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '40d1ad355b8e2bf6a0ea86ab4653911e'


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    temperature = None
    city_name = None
    if request.method == 'POST':
        city_name = request.form['city']
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key}"
        )
        if weather_data.json()['cod'] == '404':
            weather = "No City Found"
        else:
            weather = weather_data.json()['weather'][0]['main']
            temperature = round(weather_data.json()['main']['temp'])
    return render_template('index.html', weather=weather, temperature=temperature, city_name=city_name)


if __name__ == '__main__':
    app.run(debug=True)
