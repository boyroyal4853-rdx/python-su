import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import os

pygame.mixer.init()

def speak(text):
    print(f"Ganga: {text}")
    
    # 👉 Text ko clean Hindi me convert karo
    clean_text = text.replace("ba", "है").replace("ka", "क्या")

    tts = gTTS(text=clean_text, lang='hi', tld='co.in')
    filename = "voice.mp3"
    
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    pygame.mixer.music.unload()
    pygame.mixer.quit()

    time.sleep(0.5)
    os.remove(filename)

# --- Voice Input ---
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=0.8)
        print("\nListening...")
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice, language='hi-IN')
        command = command.lower()
        print(f"You said: {command}")
        return command
    except:
        return ""

# --- Weather ---
def get_weather(city="Varanasi"):
    try:
        api_key = "YOUR_API_KEY"   # 👉 apna API key daalo
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        data = requests.get(url).json()

        temp = data['main']['temp']
        desc = data['weather'][0]['description']

        return f"{city} me abhi temperature {temp} degree hai aur mausam {desc} hai."
    except:
        return "Weather check nahi ho paaya."

# --- Indian Assistant ---
def indian_assistant(command):

    if "namaste" in command or "hello" in command:
        return "Namaste! Ka haal ba?"

    elif "time" in command or "samay" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return f"Abhi ka samay hai {time}"

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        return f"Aaj ki tareekh hai {date}"

    elif "weather" in command or "mausam" in command:
        return get_weather()

    elif "kaun hai" in command or "who is" in command:
        try:
            person = command.replace("kaun hai", "").replace("who is", "")
            info = wikipedia.summary(person, sentences=2)
            return info
        except:
            return "Iske baare me jankari nahi mili."

    elif "news" in command:
        return "Aaj ke news ke liye Google News check kariye."

    elif "thank you" in command:
        return "Aapka swagat hai!"

    return None

# --- Confirmation System ---
def ask_continue():
    speak("Kya aap aur koi kaam karwana chahte hain? Yes ya No boliye.")
    
    answer = take_command()

    if answer == "":
        speak("Samajh nahi aaya, main band ho raha hoon.")
        return False

    if 'yes' in answer or 'haan' in answer:
        return True
    else:
        speak("Theek hai, phir milte hain. Namaste!")
        return False

# --- Main Logic ---
def run_assistant():
    command = take_command()

    if not command:
        speak("Kuch suna nahi, dobara boliye.")
        return True

    # --- Song ---
    if 'play' in command or 'baja' in command:
        song = command.replace('play', '').replace('baja', '')
        speak(f"{song} bajaya ja raha hai")
        pywhatkit.playonyt(song)

    # --- Open Apps ---
    elif 'open' in command or 'kholo' in command:
        if 'notepad' in command:
            os.system('notepad')
            speak("Notepad khul gaya")

        elif 'calculator' in command:
            os.system('calc')
            speak("Calculator khul gaya")

        elif 'chrome' in command:
            os.system('start chrome')
            speak("Chrome khul gaya")

    # --- Window Control ---
    elif 'close' in command:
        pyautogui.hotkey('alt', 'f4')
        speak("Window band kar diya")

    elif 'minimize' in command:
        pyautogui.hotkey('win', 'd')
        speak("Sab minimize kar diya")

    # --- Search ---
    elif 'search' in command:
        query = command.replace('search', '')
        pywhatkit.search(query)
        speak(f"{query} search kar rahe hain")

    # --- Indian Assistant ---
    else:
        response = indian_assistant(command)
        if response:
            speak(response)
        else:
            speak("Thoda aur clearly boliye, samajh nahi aaya.")

    return True

# --- Main ---
if __name__ == "__main__":
    speak("radhe- radhe , boli   ham   kya sewa  kree")
    
    while True:
        if not run_assistant():
            break

        if not ask_continue():
            break