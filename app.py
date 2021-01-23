from flask import Flask, render_template, request, redirect
from weather_backend import get_weather, get_attire
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        emails = request.form.get("emails")
        names = request.form.get("names")
        message = request.form.get("message")
        if message is not None:
            with open('user_data/feedback_form.csv', mode='a') as file_:
                file_.write("Email: {}, Names: {}, Message: {}".format(emails,names,message))
                file_.write("\n")

        Email = request.form.get("Email")
        if Email is not None:
            with open('user_data/sub_email.csv', mode='a') as file_:
                file_.write("Email:{}".format(Email))
                file_.write("\n")

        return redirect(request.url)

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
    wind_speed = result["wind_speed"]
    wind_direction = result["wind_direction"]
    temp = int(result["temperature"])
    feels = result["feels_temperature"]
    description = result["weather_description"]
    icon = result["icons"]
    message = str(get_attire(result))
    email = request.form.get("email")
    if email is not None:
        with open('user_data/sub_email.csv', mode='a') as file_:
                file_.write("Email:{}".format(email))
                file_.write("\n")

    return render_template("landing_page.html", wind_speed=wind_speed, wind_direction=wind_direction, cityname=city_name, message=message, temp=temp, humid=humid,feels=feels, weather_description=description, icon = icon)


if __name__ == "__main__":
    app.run(debug=True)
