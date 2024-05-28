from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather_data(city):
     API_KEY = '4a30f12a18c4d06bbe8dfc186a44cb85'
     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
     r = requests.get(url).json()
     return r
@app.route("/")
def index():
    print(get_weather_data('Guayaquil'))
    return render_template('index.html')

if __name__ ==  "__main__":
     app.run(debug=True)
