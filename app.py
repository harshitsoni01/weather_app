from flask import Flask, render_template, request, redirect
from weather_backend import weather_city, clothes

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"


@app.route("/")
def index():
    return render_template("index1.html")


@app.route("/dress", methods=['POST'])
def dress():
    city_name = request.form.get("city_name")
    app.logger.info(f'city name={city_name}')
    result = weather_city(city_name)
    wind = result["wind_speed"]
    temp = result["temperature"]
    feels = result["feels_temperature"]
    description = result["weather_description"]
    message = str(clothes(city_name))
    return render_template("dress.html", wind=wind, cityname=city_name, message=message, temp=temp, feels_temperature=feels, weather_description=description)


if __name__ == "__main__":
    app.run(debug=True)
