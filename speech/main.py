# import webbrowser
# import speech_recognition as sp 
# import time
# import pyttsx3

# r = sp.Recognizer()
# engine = pyttsx3.init()
# start = False


# def speak(text):
#     print(f"Alexa: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def record_Audio(prompt=None):
#     if prompt:
#         speak(prompt)
#     with sp.Microphone() as source:
#         speak("Listening...")
#         audio = r.listen(source)

#     if start is not True:
#         try:
#             voice_data = r.recognize_google(audio)
#             speak(f"You said: {voice_data}")
#             time.sleep(1)
#             return voice_data.lower()
#         except sp.UnknownValueError:
#             speak("Sorry, I did not get that")
#             time.sleep(1)
#             return ""
#         except sp.RequestError:
#             speak("Sorry, my speech service is down")
#             time.sleep(1)
#             return ""
#         except Exception as e:
#             speak(f"An unexpected error occurred: {e}")
#             time.sleep(1)
#             return ""
#     elif start is True:
#         voice_data = r.recognize_google(audio)
#         speak(f"You said: {voice_data}")
#         time.sleep(1)
#         return voice_data.lower()



    





# def respond(voice_data):
#     if 'what is your name' in voice_data:
#         speak('My name is Alexa')
#     elif 'search' in voice_data:
#         search = record_Audio('What do you want to search for?')
#         if search:
#             url = 'https://google.com/search?q=' + search.replace(' ', '+')
#             webbrowser.open(url)
#             speak('Here is what I found for: ' + search)
#             time.sleep(1)
#     elif 'search for' in voice_data or 'image' in voice_data:
#         search = record_Audio('What do you want to search for?')
#         if search:
#             url = 'https://www.google.com/search?q=' + search.replace(' ', '+')
#             webbrowser.open(url)
#             speak('Showing results for: ' + search)
#             time.sleep(1)

#     elif sp.UnknownValueError:
#              speak('Try Again What can i assist you ')
#              time.sleep(2)



# def HiAlexa(alexa_start):
    
#     if 'start' in alexa_start or 'star' in alexa_start or start is not True:
#         speak('What can I assist you with?')
#         time.sleep(1)
#         listen = record_Audio()
#         time.sleep(1)
#         respond(listen)
#         start = True
#         if start is True:
#             listen_start = record_Audio()
#             responstart = respond(listen_start)
            

#     elif 'stop' in alexa_start:
#         speak('Ok, Goodbye!')
#         return False

#     else:
#         return True  # Keep running if input doesn't match 'start' or 'stop'

# while True:
#     start_listen = record_Audio('Say "start" to begin or "stop" to exit.')
#     if not HiAlexa(start_listen):
#         break

import tkinter as tk
from tkinter import messagebox
import speech_recognition as sp
import pyttsx3
import webbrowser
import threading

r = sp.Recognizer()
engine = pyttsx3.init()

def speak(text):
    output_text.set(f"Alexa: {text}")
    engine.say(text)
    engine.runAndWait()

def record_audio(prompt=None):
    if prompt:
        speak(prompt)

    with sp.Microphone() as source:
        output_text.set("Listening...")
        speak('Listening')
        try:
            audio = r.listen(source, timeout=5)
            voice_data = r.recognize_google(audio)
            output_text.set(f"You said: {voice_data}")
            voice_datasaid = (f"You said {voice_data}")
            return voice_data.lower()
        except sp.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sp.RequestError:
            speak("Sorry, the speech service is down.")
        except Exception as e:
            speak(f"Error: {e}")
    return ""

def respond(voice_data):
    if "your name" in voice_data:
        speak("My name is Alexa.")
    elif "search" in voice_data:
        query = record_audio("What do you want to search for?")
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Here is what I found for {query}.")
    elif "stop" in voice_data:
        speak("Goodbye.")
        root.quit()

def start_assistant():
    def run():
        voice_data = record_audio("Say something.")
        if voice_data:
            respond(voice_data)
    threading.Thread(target=run).start()

# ---- GUI Setup ----
root = tk.Tk()
root.title("Alexa Voice Assistant")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

output_text = tk.StringVar()
output_text.set("Welcome to Alexa GUI")

output_label = tk.Label(root, textvariable=output_text, wraplength=300, bg="#f0f0f0", font=("Helvetica", 12))
output_label.pack(pady=30)

listen_button = tk.Button(root, text="🎤 Start Listening", font=("Helvetica", 14), command=start_assistant)
listen_button.pack(pady=10)

exit_button = tk.Button(root, text="❌ Exit", font=("Helvetica", 12), command=root.quit)
exit_button.pack(pady=5)

root.mainloop()

