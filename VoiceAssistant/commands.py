import datetime
import wikipedia
import pywhatkit
import pyjokes
import os
from speech import speak

def execute_command(command, output_area=None):

    if 'hello' in command:
        speak("Hello! How can I help you?", output_area)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        speak("Current time is " + time, output_area)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today's date is " + date, output_area)

    elif 'search' in command:
        query = command.replace("search", "")
        speak("Searching " + query, output_area)
        pywhatkit.search(query)

    elif 'wikipedia' in command:
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result, output_area)

    elif 'play' in command:
        song = command.replace("play", "")
        speak("Playing " + song, output_area)
        pywhatkit.playonyt(song)

    elif 'joke' in command:
        speak(pyjokes.get_joke(), output_area)

    elif 'open chrome' in command:
        os.system("start chrome")

    elif 'exit' in command:
        speak("Goodbye!", output_area)
        exit()

    else:
        speak("I didn't understand that", output_area)
