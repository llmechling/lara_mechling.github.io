# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:56:03 2022

@author: Lara Home
"""
import time
import requests
import json

def welcomeMessage():
    """Welcome the user to the program"""
    print("Welcome to your weather forcast!\n")
    time.sleep(2)
    print("Please use a zip code to select your location.\n")
    time.sleep(2)
    print("Once your zip code is entered you will be able to view the weather for that area.")
    time.sleep(3)

def getZipCode():
    """Prompt user for their zip code"""
    active = True
    while active:
        zip_code = str(input("Please enter a 5-didgit zip code: "))
        if len(zip_code) == 5:
            return zip_code
            break
        else:
            print("\nPlease enter 5 didgits.\n")
            continue
        
def openWeathermap():
    """Open http://openweathermap.org"""
    #store local variables
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = 'fde9ba41d22c50ffd0ac18bae09dd05f'
    full_url = url + 'q=' + zip_code + "&appid=" + api_key
    r = requests.get(full_url)
    return r

def verifyConnection():
    '''verify conntecion to API'''
    print("\nLets check your connection.\n")
    time.sleep(2)
    
    try:
        r.raise_for_status()
    except requests.HTTPError as http_exception:
        print(f"Status: {http_exception}. An HTTP error has occured.\n")
    except Exception as other_exception:
        print(f"Status: {other_exception}. A non-HTTP error has occured\n")
    else:
        print("Your connection was successful.\n")  
    
def displayWeather():
    """Obtain the weather data from http://openweathermap.org"""
    r_dict = r.json()
    
    main = r_dict['main']
    temperature = main['temp']
    humidity = main['humidity']
    feels_like = main['feels_like']
    
    wind = r_dict['wind']
    wind_speed = wind['speed']

    print(f"The temperature is {temperature} degrees, but ")
    print(f"with a humidity of {humidity}% and a wind speed")
    print(f"of {wind_speed}, it feels like {feels_like} degrees.\n")
    
    print(zip_code)
    print(f"\tTemperature: {temperature}")
    print(f"\tHumidity: {humidity}")
    print(f"\tWind Speed: {wind_speed}")
    print(f"\tFeels Like: {feels_like}")

def continueProgram():
    while True:
        continue_program = str(input("Please enter 'y' to restart the program or 'n' to end: ")).lower()
        
        if continue_program == 'y':
            zip_code = getZipCode()
            r = openWeathermap()
            verifyConnection()
            displayWeather()
            continueProgram()
        elif continue_program == 'n':
            break
        else:
            print("Please enter a 'y' or an 'n'.")
            
welcomeMessage()
zip_code = getZipCode()
r = openWeathermap()
verifyConnection()
displayWeather()
continueProgram()


