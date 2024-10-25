import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import requests

print('Loading your AI personal assistant - A V M')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good Morning"
    elif hour < 18:
        greet = "Good Afternoon"
    else:
        greet = "Good Evening"

    speak(f"Hello, {greet}")
    print(f"Hello, {greet}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")
            return statement.lower()
        except Exception:
            speak("Pardon me, please say that again.")
            return "None"


speak("Hey, I am your AI personal assistant AVM.")
wishMe()
speak("Tell me how I can help you now.")

while True:
    statement = takeCommand()

    if "good bye" in statement or "ok bye" in statement or "stop" in statement:
        speak('Your personal assistant AVM is shutting down. Goodbye.')
        print('Your personal assistant AVM is shutting down. Goodbye.')
        break

    if 'wikipedia' in statement:
        speak('Searching Wikipedia...')
        statement = statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("YouTube is open now.")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google is open now.")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("https://gmail.com")
        speak("Google Mail is open now.")
        time.sleep(5)

    elif "weather" in statement:
        api_key = "YOUR_API_KEY"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("What's the city name?")
        city_name = takeCommand()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273.15  # Convert from Kelvin to Celsius
            current_humidity = y["humidity"]
            weather_description = x["weather"][0]["description"]
            speak(
                f"Temperature in Celsius is {current_temperature:.2f} degrees. Humidity is {current_humidity}% and the weather is described as {weather_description}.")
            print(
                f"Temperature: {current_temperature:.2f}°C, Humidity: {current_humidity}%, Description: {weather_description}")
        else:
            speak("City Not Found.")
    elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {strTime}")

    elif 'who are you' in statement or 'what can you do' in statement:
        speak(
            'I am AVM version 1.0, your personal assistant. I can perform tasks like opening YouTube, Google, Gmail, checking the weather, searching Wikipedia, and more.')

    elif 'who made you' in statement:
        speak("I was built by Vishnu Prakash.")
        print("I was built by Vishnu Prakash.")

    elif 'how are you' in statement:
        speak("I am doing good. How are you?")
        print("I am doing good. How are you?")

    elif 'joke' in statement:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)

    elif "open stackoverflow" in statement:
        webbrowser.open_new_tab("https://stackoverflow.com")
        speak("Here is Stack Overflow.")

    elif "play" in statement:
        song = statement.replace('play', '')
        speak('Playing ' + song)
        pywhatkit.playonyt(song)
        time.sleep(6)

    elif 'news' in statement:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India. Happy reading!')
        time.sleep(6)

    elif "camera" in statement:
        ec.capture(0, "robo camera", "img.jpg")

    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    elif 'ask' in statement:
        speak('I can answer computational and geographical questions. What do you want to ask?')
        question = takeCommand()
        app_id = "YOUR_APP_ID"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)

    elif "log off" in statement:
        speak("Okay, your PC will log off in 10 seconds. Please save your work.")
        subprocess.call(["shutdown", "/l"])

