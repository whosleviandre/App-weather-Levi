from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

def get_weather_data(city):
    API_KEY = '4a30f12a18c4d06bbe8dfc186a44cb85'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    r = requests.get(url).json()
    return r

def get_unsplash_image(city, api_key):
    url = f'https://api.unsplash.com/search/photos?query={city}&client_id={api_key}'
    r = requests.get(url).json()
    if r['results']:
        return r['results'][0]['urls']['full']
    return None

def get_default_image():
    hour = datetime.now().hour
    if 6 <= hour < 8:
        return 'https://github.com/whosleviandre/App-weather-Levi/blob/main/static/vecteezy_sunrise-from-the-sea_45637165.JPG?raw=true'
    elif 8 <= hour < 17:
        return 'https://github.com/whosleviandre/App-weather-Levi/blob/main/static/vecteezy_cloudy-and-bluesky-in-the-morning-background-soft-focus_6835788.JPG?raw=true'
    elif 17 <= hour < 19:
        return 'https://github.com/whosleviandre/App-weather-Levi/blob/main/static/vecteezy_sunset-over-tranquil-seascape-blurred-motion-waves_25484887.jpg?raw=true'
    else:
        return 'https://github.com/whosleviandre/App-weather-Levi/blob/main/static/noche.jpg?raw=true'

@app.route("/", methods=['POST', 'GET'])
def index():
    default_image = get_default_image()
    city_image_url = default_image
    if request.method == 'POST':
        ciudad = request.form.get('txtciudad')
        if ciudad:
            data = get_weather_data(ciudad)
            if data['cod'] != 200:
                return render_template('index.html', error="City not found.", default_image=default_image)
            UNSPLASH_API_KEY = 'bqd2VY0lqhfOgh7UJlc1VeUx4lAky53jkeYmbJcRJ5c'
            city_image_url = get_unsplash_image(ciudad, UNSPLASH_API_KEY) or default_image
            return render_template('index.html', context=data, city_image_url=city_image_url, default_image=default_image)
    return render_template('index.html', city_image_url=city_image_url, default_image=default_image)

@app.route("/cv", methods=['GET'])
def cv():
    return render_template('cv.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        USUARIO = "ADMIN@ADMIN.COM"
        PASSWORD = "ADMIN"
        user = request.form.get("txtemail")
        password = request.form.get("txtpassword")
        if USUARIO == user and PASSWORD == password:
            return render_template('index.html')
        else:
            return render_template('login.html', error=True)
    else:
        return render_template("login.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
