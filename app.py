from flask import Flask, render_template, request
from weather_backend import temperature_condition,clothes,feels_temperature,weather_description,weather_city

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dress", methods= ['GET', 'POST'])
def dress():
    cityname = request.form.get("city_name")
    result = weather_city(cityname)
    wind=result["wind_speed"]
    temp = str(temperature_condition())
    message = str(clothes())
    feels = feels_temperature
    description= weather_description
    return render_template("dress.html",wind= wind,cityname=cityname, message=message, temp=temp, feels_temperature=feels, weather_description=description )

if __name__ == "__main__":
    app.run(debug=True)