from flask import Flask, render_template
from weather_backend import temperature_condition,clothes,name_city

app = Flask(__name__)
app.config["SECRET_KEY"] = "Secret-key"

@app.route("/")
def search():
    city = name_city()
    return city
# def index():
#     temp = str(temperature_condition())
#     #return f"[temperature]: {temp}"
#     return render_template("index.html", temp=temp)

@app.route("/dress")
def dress():
    message = str(clothes())
    return f"[message]:{message}"

if __name__ == "__main__":
    app.run(debug=True)