from flask import Flask, render_template, request, redirect
from weather_backend import get_weather, get_attire

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")

@app.route("/single")
def single():
    return render_template("single.html")

@app.route("/", methods=['GET','POST'])
@app.route("/landing_page", methods=['GET','POST'])
def dress():
    city_name = request.form.get("city_name")
    app.logger.info(f'city name={city_name}')
    result = get_weather(city_name)
    humid = result["humidity"]
    wind = result["wind_speed"]
    temp = result["temperature"]
    feels = result["feels_temperature"]
    description = result["weather_description"]
    icon = result["icons"]
    message = str(get_attire(result))
    return render_template("landing_page.html", wind=wind, cityname=city_name, message=message, temp=temp, humid=humid,feels_temperature=feels, weather_description=description, icon = icon)


if __name__ == "__main__":
    app.run(debug=True)
