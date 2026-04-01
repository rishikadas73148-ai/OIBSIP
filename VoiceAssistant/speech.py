import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text, output_area=None):
    if output_area:
        output_area.insert("end", "Assistant: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

def take_command(output_area=None):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        if output_area:
            output_area.insert("end", "Listening...\n")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        if output_area:
            output_area.insert("end", "You: " + command + "\n")
    except:
        return ""

    return command
