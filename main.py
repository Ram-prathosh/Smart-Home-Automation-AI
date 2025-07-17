import speech_recognition as sr
import pyttsx3
import datetime

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # speed

# Device simulation
devices = {
    "lights": False,
    "fan": False,
    "ac": False
}

# Speak function
def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# Listen to user
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

# Time-based suggestion
def suggest_automation():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 18 and not devices["lights"]:
        speak("It's daytime. Turning off the lights to save energy.")
        devices["lights"] = False
    elif hour >= 18 and not devices["lights"]:
        speak("It's evening. Turning on the lights.")
        devices["lights"] = True

# Control devices
def control_device(command):
    if "turn on lights" in command:
        devices["lights"] = True
        speak("Lights turned on.")
    elif "turn off lights" in command:
        devices["lights"] = False
        speak("Lights turned off.")
    elif "turn on fan" in command:
        devices["fan"] = True
        speak("Fan is on.")
    elif "turn off fan" in command:
        devices["fan"] = False
        speak("Fan is off.")
    elif "turn on ac" in command:
        devices["ac"] = True
        speak("AC turned on.")
    elif "turn off ac" in command:
        devices["ac"] = False
        speak("AC turned off.")
    elif "status" in command:
        status = ", ".join([f"{k}: {'on' if v else 'off'}" for k, v in devices.items()])
        speak("Current device status: " + status)
    else:
        speak("Sorry, I don't understand that command.")

# Main loop
def main():
    speak("Welcome to Smart Home Automation System.")
    suggest_automation()
    while True:
        command = listen()