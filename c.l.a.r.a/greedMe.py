import datetime
from sayAndListen import speak

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Please tell me, how can I help you today?")

if __name__ == "__main__":
    wishMe()

