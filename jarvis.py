import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import pyautogui

# --- Voice Engine Setup ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# 1 aksar Female voice hola (Agar mard ke awaaz aaye ta 0 ya 2 try kar sakela)
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 150) # Thoda dheere bolai ta Bhojpuri me maza aayi
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"Ganga: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        # Shor kam kare khatir
        listener.adjust_for_ambient_noise(source, duration=0.8)
        print("\nSuni taani... Boliye... (Listening...)")
        voice = listener.listen(source)

    try:
        # Google Hindi (hi-IN) Bhojpuri badhiya se samjhela
        command = listener.recognize_google(voice, language='hi-IN')
        command = command.lower()
        print(f"Aapne kaha: {command}")
        return command
    except:
        return ""

def run_assistant():
    command = take_command()
    
    if not command:
        return True

    # --- Gaana Bajaye khatir ---
    if 'बजाओ' in command or 'baja' in command or 'play' in command:
        song = command.replace('play', '').replace('baja', '').replace('बजाओ', '')
        speak(f'Theek ba Diwakar ji, abhi YouTube par {song} bajawat tani, maza liji.')
        pywhatkit.playonyt(song)

    # --- App Khole khatir ---
    elif 'खोल' in command or 'open' in command or 'kholo' in command:
        if 'notepad' in command:
            speak('Theek ba, Notepad khul gail ba.')
            os.system('notepad')
        elif 'calculator' in command or 'hisab' in command:
            speak('Hisab-kitab khatir calculator khul gail.')
            os.system('calc')
        elif 'chrome' in command or 'browser' in command:
            speak('Internet wala browser khul gail ba.')
            os.system('start chrome')

    # --- Window Controls ---
    elif 'छोटा' in command or 'minimize' in command:
        speak('Theek ba, sab window niche kar tani.')
        pyautogui.hotkey('win', 'd')

    elif 'बंद' in command or 'close' in command:
        speak('Theek ba, window band ho gail.')
        pyautogui.hotkey('alt', 'f4')

    # --- Time (Samay) ---
    elif 'समय' in command or 'time' in command or 'ka baje' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Abhi ke samay ho rahal ba {time}')

    # --- Exit ---
    elif 'बंद हो' in command or 'ruk jao' in command or 'exit' in command:
        speak('Theek ba, ab hum jaat tani. Pranam Diwakar ji!')
        return False
    
    else:
        # Kuch na samajh me aila par
        speak('Ka kahila? Humra samajh me nahi aayil, fir se boli na.')
    
    return True

# --- Main Start ---
if __name__ == "__main__":
    # Assistant ke desi swagat
    speak("Pranam Diwakar ji! Hum Ganga bani, batai ka sahayata kari?")
    while True:
        if not run_assistant():
            break