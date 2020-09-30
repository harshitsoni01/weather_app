from flask import Flask, render_template, request
# from weather_backend import weather_city, clothes

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dress", methods= ['GET', 'POST'])
def dress():
    cityname = request.args.get("city_name")
    from weather_backend import weather_city, clothes

    # result = weather_city(cityname)
    wind=weather_city(cityname)["wind_speed"]
    temp =weather_city(cityname)["temperature"]
    message = str(clothes())
    feels = weather_city(cityname)["feels_temperature"]
    description= weather_city(cityname)["weather_description"]
    return render_template("dress.html",wind= wind,cityname=cityname, message=message, temp=temp, feels_temperature=feels, weather_description=description )

if __name__ == "__main__":
    app.run(debug=True)