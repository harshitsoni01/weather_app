# Python program to find current weather details of any city using openweathermap api
# 60 calls/min and 1,000,000 calls/month
import requests, json 
api_key = "b03aae2dd0d2c016e48d6fc50ec429f2"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ") 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" 
response = requests.get(complete_url) 

x = response.json()

if x["cod"] != "404": 
    y = x["main"]
    b = x["wind"]
    
    wind_speed = b["speed"]
    feels_temperature = y["feels_like"]
    current_temperature = y["temp"]# [] is keys() method to call/add something
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 

    z = x["weather"] 
    weather_description = z[0]["description"]
    ids = z[0]["id"] 

    print(" Temperature (in celsius unit) = " +
                    str(current_temperature) +
        "\n Feels like(in celsisu unit) = " +
                    str(feels_temperature) +
        "\n atmospheric pressure (in Pa unit) = " +
                    str(current_pressure) +
        "\n humidity (in percentage) = " +
                    str(current_humidiy) +
        "\n description = " +
                    str(weather_description)+
        "\n wind_speed(in meters/sec) = " +
                    str(wind_speed) +
        "\n id of des = "+
                    str(ids)  )
else:
    print(" City Not Found ")

def weather_condition():
    query = ids
    print(f"[weather_id]: {query}")
    return query

def temperature_condition():
    temp = current_temperature
    print(f"[temperature]: {temp}")
    return temp

temp = int(temperature_condition())
query = int(weather_condition())

def clothes():
    if query in range(200,203) or query in range(230,233):#thunderstorm1 with rain
        if temp in range(-20,-10):
            print("WARNING!! DON'T GO OUT!"
                    "\n Expect Snow"
                    "\n Wear atleast 4 layers of clothing."
                    "\n And atleast 3 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(-10,0):
            print("WARNING!! TEMPERATURE LESS THAN ZERO!"
                    "\n Expect Snow"
                    "\n Wear atleast 3 layers of clothing."
                    "\n And atleast 2 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(0,5):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(5,10):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(10,15):
            print("Wear atleast 2 layers of clothing."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(15,20):
            print("Wear a coat or sweater."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(20,25):
            print("Wear some light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(25,30):
            print("Wear light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(30,35):
            print("Wear lightweight clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(35,40):
            print("Wear Lightweight running pants or capris with a long sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(40,45):
            print("Wear Lightweight capris or shorts with a long-sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Carry a umbrella or wind-cheater."
                    "\n Protect yourself from the heat.")
    elif query in range(210,212):#thunderstorm2
        print("Expect Rain.")
        if temp in range(-20,-10):
            print("WARNING!! DON'T GO OUT!"
                    "\n Wear atleast 4 layers of clothing."
                    "\n And atleast 3 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(-10,0):
            print("WARNING!! TEMPERATURE LESS THAN ZERO!"
                    "\n Wear atleast 3 layers of clothing."
                    "\n And atleast 2 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(0,5):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(5,10):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(10,15):
            print("Wear atleast 2 layers of clothing."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(15,20):
            print("Wear a coat or sweater."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(20,25):
            print("Wear some light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(25,30):
            print("Wear light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(30,35):
            print("Wear lightweight clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(35,40):
            print("Wear Lightweight running pants or capris with a long sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(40,45):
            print("Wear Lightweight capris or shorts with a long-sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Carry a umbrella or wind-cheater."
                    "\n Protect yourself from the heat.")
    elif query in range(212,222):#thunderstorm3
        print("WARNING!Heavy thunderstorm outside."
                "\n You might be more safe inside."
                "\n Stay inside for atleast 30 minutes after the last strike.")
        if temp in range(-20,-10):
            print("WARNING!! DON'T GO OUT!"
                    "\n Wear atleast 4 layers of clothing."
                    "\n And atleast 3 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(-10,0):
            print("WARNING!! TEMPERATURE LESS THAN ZERO!"
                    "\n Wear atleast 3 layers of clothing."
                    "\n And atleast 2 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(0,5):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(5,10):
            print("Wear atleast 2 layers of clothing."
                    "\n And atleast 1 layers on your head."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(10,15):
            print("Wear atleast 2 layers of clothing."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(15,20):
            print("Wear a coat or sweater."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(20,25):
            print("Wear some light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(25,30):
            print("Wear light clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(30,35):
            print("Wear lightweight clothes."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(35,40):
            print("Wear Lightweight running pants or capris with a long sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        elif temp in range(40,45):
            print("Wear Lightweight capris or shorts with a long-sleeve shirt or t-shirt."
                    "\n Carry a umbrella or wind-cheater."
                    "\n Wear Gum Boots.")
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Carry a umbrella or wind-cheater."
                    "\n Protect yourself from the Extreme temperature.")        
    
# gender = input("Enter your Gender:\n")
# #this can be made into select a gender or genders can be showed side by side
# gender = gender.lower()

# if gender == "man" or gender == "male" or gender == "m" or gender == "men":
#     men_clothes()