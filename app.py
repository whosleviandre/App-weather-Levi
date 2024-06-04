from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = '4a30f12a18c4d06bbe8dfc186a44cb85'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ciudad = str(request.form.get('txtciudad'))
        if ciudad:
            data = get_weather_data(ciudad)
        return render_template('index.html', context=data)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)