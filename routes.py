from app import app
#from flask import render_template
from weather_backend import temperature_condition,clothes


@app.route("/")
@app.route("/index")
def index():
    
    temp = str(temperature_condition())
    return f"[temperature]: {temp}"

@app.route("/dress")
@app.route("/index/dress")
def dress():
    message = str(clothes())
    return f"[message]:{message}"
