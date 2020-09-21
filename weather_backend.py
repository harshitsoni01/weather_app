# Python program to find current weather details of any city using openweathermap api
# 60 calls/min and 1,000,000 calls/month
import requests, json 
import weatherMappingMessage
from keys import *

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

index = temp//5
weather_message_map = weatherMappingMessage.weather_message_dict
weather_message = ""


def clothes():
    if query in range(200,203) or query in range(230,233):#thunderstorm1 with rain
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nWear Gum Boots and Carry an umbrella"
            print(weather_message) 
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(210, 212):#thunderstorm2
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(212, 222):#thunderstorm3
        if index in weather_message_map:
            weather_message = "WARNING!Heavy thunderstorm outside.\n You might be more safe inside.\n Stay inside for atleast 30 minutes after the last strike." + weather_message_map[index] + "Carry a Umbrella"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(300, 312):#drizzle decreases visibility more rain 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(312, 322):#heavy drizzle
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella.\nWear Gum Boots" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(500, 502) or query in range(520,522):#rain 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(502, 505) or query in range(522,532):#heavy rain and shower 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 511 or query in range(611, 614):#Freezing rain and sleet
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella and a windcheater.\n Wear Gum Boots" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(600, 602) or query in range(615, 621):#Snow
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 602 or query == 622:#Heavy snow 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 701:#mist 
        if index in weather_message_map:
            weather_message = weather_message_map[index]
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 741:#fog
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nVisibility of your surrounding is subpar."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 711:#smog 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nProtect your eyes and nose when going out."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 721:#Haze 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nvisibility around your area is sub par"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 731 or query == 751 or query == 761:#dust/sand 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nProtect your eyes and nose when going out.\nDust and sand in the atmosphere."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 762:#volanic ash
        if index in weather_message_map:
            weather_message = "WARNING! Don't go out.\n volanic ash in your surrounding."+weather_message_map[index] + "\nvisibility around your area is sub par"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 771:#squall 
        if index in weather_message_map:
            weather_message = "Expect precipitation" + weather_message_map[index] + "\nHigh speed winds.\nWear protective gears."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query == 781:#tornado 
        if index in weather_message_map:
            weather_message = "WARNING!Don't go out." + weather_message_map[index] + "\nWear neccessary gears"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(800, 803):#clear/10-40clouds
        if index in weather_message_map:
            weather_message = weather_message_map[index]
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif query in range(803,805):
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCloud surrounding."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    return weather_message

# # gender = input("Enter your Gender:\n")
# # #this can be made into select a gender or genders can be showed side by side
# # gender = gender.lower()

# # if gender == "man" or gender == "male" or gender == "m" or gender == "men":
# #     men_clothes()

clothes()
