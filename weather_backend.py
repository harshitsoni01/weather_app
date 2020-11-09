# Python program to find current weather details of any city using openweathermap api
# 60 calls/min and 1,000,000 calls/month
import requests, json 
import weatherMappingMessage
import keys

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + keys.api_key + "&q=" + city_name + "&units=metric" 
    api_response = (requests.get(complete_url)).json()

    print("api_response", api_response)

    try:
        weather_values = api_response["main"]
        current_temperature = weather_values["temp"]# [] is keys() method to call/add something
        current_pressure = weather_values["pressure"] 
        current_humidity = weather_values["humidity"]
        feels_temperature = weather_values["feels_like"]

        wind = api_response["wind"]
        wind_speed = wind["speed"]

        weather_desc = api_response["weather"] 
        weather_description = weather_desc[0]["description"]
        ids = weather_desc[0]["id"]
        icons = weather_desc[0]["icon"]
        print(f' Temperature (in celsius unit) = {current_temperature} '
            f'Feels like(in celsisu unit) =  {feels_temperature}'
            f'atmospheric pressure (in Pa unit) = {current_pressure}'
            f'humidity (in percentage) = {current_humidity}'
            f'description = {weather_description}'
            f'wind_speed(in meters/sec) = {wind_speed}'
            f'id of des = {ids}'
            f'icon = {icons}')

    except requests.exceptions.HTTPError as e:
        if e.response.cod == 400:
            print(e)
            pass  
    return {
        "wind_speed":wind_speed,
        "ids":ids,
        "temperature":current_temperature,
        "feels_temperature":feels_temperature,
        "pressure":current_pressure,
        "humidity":current_humidity,
        "weather_description":weather_description,
        "icons":icons,
    }


def get_attire(weather_response):
    weather_message_map = weatherMappingMessage.weather_message_dict
    weather_message = ""

    print("weather response", weather_response)
    temp = weather_response["temperature"]
    index = temp//5
    ids = weather_response["ids"]
    if ids in range(200,203) or ids in range(230,233):#thunderstorm1 with rain
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nWear Gum Boots and Carry an umbrella"
            print(weather_message) 
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(210, 212):#thunderstorm2
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(212, 222):#thunderstorm3
        if index in weather_message_map:
            weather_message = "WARNING!Heavy thunderstorm outside.\n You might be more safe inside.\n Stay inside for atleast 30 minutes after the last strike." + weather_message_map[index] + "Carry a Umbrella"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(300, 312):#drizzle decreases visibility more rain 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(312, 322):#heavy drizzle
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella.\nWear Gum Boots" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(500, 502) or ids in range(520,522):#rain 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(502, 505) or ids in range(522,532):#heavy rain and shower 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 511 or ids in range(611, 614):#Freezing rain and sleet
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella and a windcheater.\n Wear Gum Boots" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(600, 602) or ids in range(615, 621):#Snow
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 602 or ids == 622:#Heavy snow 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nCarry a Umbrella" 
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 701:#mist 
        if index in weather_message_map:
            weather_message = weather_message_map[index]
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 741:#fog
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nVisibility of your surrounding is subpar."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 711:#smog 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nProtect your eyes and nose when going out."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 721:#Haze 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nvisibility around your area is sub par"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 731 or ids == 751 or ids == 761:#dust/sand 
        if index in weather_message_map:
            weather_message = weather_message_map[index] + "\nProtect your eyes and nose when going out.\nDust and sand in the atmosphere."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 762:#volanic ash
        if index in weather_message_map:
            weather_message = "WARNING! Don't go out.\n volanic ash in your surrounding."+weather_message_map[index] + "\nvisibility around your area is sub par"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 771:#squall 
        if index in weather_message_map:
            weather_message = "Expect precipitation" + weather_message_map[index] + "\nHigh speed winds.\nWear protective gears."
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids == 781:#tornado 
        if index in weather_message_map:
            weather_message = "WARNING!Don't go out." + weather_message_map[index] + "\nWear neccessary gears"
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(800, 803):#clear/10-40clouds
        if index in weather_message_map:
            weather_message = weather_message_map[index]
            print(weather_message)
        else:
            print("WARNING!! DON'T GO OUT!!"
                    "\n Protect yourself from the extreme temperature.")
    elif ids in range(803,805):
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
