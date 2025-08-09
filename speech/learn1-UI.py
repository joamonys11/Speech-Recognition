# import tkinter as tk
# import speech_recognition as sp
# import pyttsx3



# r = sp.Recognizer()
# engine = pyttsx3.init()

# def on_click():
#     name = entry.get()
#     label_output.config(text=f"Hello, {name}!")
#     user_speakout = User_speak(name)
    

# def User_speak(name):
#     engine.say(f" Hello  {name}")
#     changeui = ChangeLabel_GUi()
#     engine.runAndWait()
   
    
# def ChangeLabel_GUi():
#     label_new = tk.Label(root,text="Hi Joe How are You")



# # Create main window
# root = tk.Tk()
# root.title("My First Tkinter App")
# root.geometry("300x200")

# # Widgets
# label = tk.Label(root, text="What's your name?")
# label.pack(pady=10)

# entry = tk.Entry(root)
# entry.pack(pady=5)

# button = tk.Button(root, text="Say Hello", command=on_click)
# button.pack(pady=5)

# label_output = tk.Label(root, text="")
# label_output.pack(pady=10)

# # Run the app
# root.mainloop()
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import webbrowser
import threading

# Setup recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Variables for UI text
user_text = None
assistant_text = None

# Setup speaking function
def speak(text):
    assistant_text.set(text)
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

# The function that does the listening and responding, runs in a thread
def listen_and_respond_thread():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            voice_input = recognizer.recognize_google(audio)
            user_text.set(f"You said: {voice_input}")

            if "name" in voice_input:
                response = "My name is Alexa."

            elif "how are you" in voice_input:
                response = "I'm doing great!"

            elif "search" in voice_input:
                query = voice_input.replace("search", "").strip()
                if query:
                    response = f"Searching for {query}"
                    speak(response)
                    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
                    return
                else:
                    response = "What do you want me to search for?"

            else:
                response = "I heard you, but I don't understand yet."

            speak(response)

    except sr.UnknownValueError:
        user_text.set("Sorry, I didn't catch that.")
        assistant_text.set("Please try again.")
    except Exception as e:
        user_text.set("Error occurred.")
        assistant_text.set(str(e))

# Button callback to start the listening thread
def on_speak_click():
    user_text.set("Listening...")
    assistant_text.set("")
    threading.Thread(target=listen_and_respond_thread, daemon=True).start()

# Change frame (page)
def show_frame(frame):
    frame.tkraise()

# GUI Setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x300")

# Create two frames (like pages)
page1 = tk.Frame(root)
page2 = tk.Frame(root)

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky='nsew')

# Initialize StringVars after root created
user_text = tk.StringVar()
assistant_text = tk.StringVar()

# ====== PAGE 1: Welcome ======
tk.Label(page1, text="Welcome to Voice Assistant", font=("Arial", 16)).pack(pady=30)
tk.Button(page1, text="Start", font=("Arial", 12), command=lambda: show_frame(page2)).pack()

# ====== PAGE 2: Assistant ======
tk.Label(page2, text="Voice Assistant", font=("Arial", 16)).pack(pady=10)
tk.Label(page2, textvariable=user_text, fg="blue").pack(pady=5)
tk.Label(page2, textvariable=assistant_text, fg="green").pack(pady=5)
ttk.Button(page2, text="🎤 Speak", command=on_speak_click).pack(pady=20)
ttk.Button(page2, text="Back", command=lambda: show_frame(page1)).pack()

# Show welcome page first
show_frame(page1)

# Start the app
root.mainloop()
