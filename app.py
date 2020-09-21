from flask import Flask, render_template, request
from weather_backend import temperature_condition,clothes,feels_temperature,weather_description

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"

@app.route("/", methods = ['GET', 'POST'])
# def search():
#     city = name_city()
#     return city
def index():
    #temp = str(temperature_condition())
    #return f"[temperature]: {temp}"
    #return render_template("index.html", temp=temp)
    location = ""
    if request.method == "POST":
        location = request.form["city_name"]
        return location
    return render_template("index.html", location=location)

@app.route("/dress")
def dress():
    temp = str(temperature_condition())
    message = str(clothes())
    feels = feels_temperature
    description= weather_description
    return render_template("dress.html", message=message, temp=temp, feels_temperature=feels, weather_description=description )

if __name__ == "__main__":
    app.run(debug=True)