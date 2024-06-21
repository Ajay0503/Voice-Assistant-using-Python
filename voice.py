import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import requests

# Text-to-Speech function
def speechtxt(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 140)
    engine.say(text)
    engine.runAndWait()

# Speech-to-Text function
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print("Heard:", data)
            return data
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Request error: {e}")
            return ""

# Weather function
def get_weather(location):
    api_key = "YOUR_WEATHER_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + location + "&appid=" + api_key

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        temp_celsius = temperature - 273.15
        return f"The weather in {location} is {weather_description}, with a temperature of {temp_celsius:.2f}°C."
    else:
        return "Weather data not found."

# Main script
if __name__ == "__main__":
    while True:
        data1 = sptext().lower()

        if "your name" in data1:
            speechtxt("My name is Pan")
        
        elif "old are you" in data1:
            speechtxt("I am 12 years old")
            
        elif 'time now' in data1:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Current time:", current_time)
            speechtxt(f"The current time is {current_time}")
        
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
            
        elif 'open linkedin' in data1:
            webbrowser.open("https://www.linkedin.com/feed/")
            
        elif 'my linkedin' in data1:
            webbrowser.open("https://www.linkedin.com/in/ajay-shanker-ab5032221/")
        
        elif 'my github' in data1:
            webbrowser.open("https://github.com/Ajay0503")
            
        elif 'chatgpt' in data1:
            webbrowser.open("https://chat.openai.com/")
        
        elif 'joke' in data1:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print("Joke:", joke)  # Debugging output
            speechtxt(joke)
            
        
        
        elif "search" in data1:
            query = data1.replace("search", "").strip()  # Extract search query
            webbrowser.open(f"https://www.google.com/search?q={query}")
        
        elif "exit" in data1:
            speechtxt("Thanks, goodbye")
            break
        
        time.sleep(5)  # Pause to prevent tight loop
