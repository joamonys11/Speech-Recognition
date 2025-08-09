import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import webbrowser
import threading
import time

# Setup recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) 
engine.setProperty('rate', 150)  # 120–180 is natural range
# engine.setProperty('volume', 1.0)  # Full volume

welcome_Text = "My name is Alexa"
Open_Text = "Welcome to Alexa What i can assit u"
listening_Text = "Listening...."

width = 500
hieght = 400

#page3 menu 
Credit_text = "Joe"
EndSpeak_text = "Ending Program"

# Speaking function
def speak(text):
    assistant_text.set(text)
    print("Alexa:", text)
    engine.say(text)
    engine.runAndWait()

# Function to listen and respond (threaded)
def listen_and_respond_thread():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            voice_input = recognizer.recognize_google(audio)
            user_text.set(f"You said: {voice_input}")
            voice_inputspeak = (f"You said {voice_input}")
            speak(voice_inputspeak)
            time.sleep(2)

            if "name" in voice_input:
                response = welcome_Text

            elif "how are you" in voice_input:
                response = "I'm doing great!"

            elif "Stop" in voice_input:
                exit

            elif "search" in voice_input:
                query = voice_input.replace("search", "").strip()
                if query:
                    response = f"Searching for {query}"
                    speak(response)
                    time.sleep(1)
                    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
                    return
                else:
                    response = "What do you want me to search for?"

            else:
                response = "I heard you, but I don't understand yet."

            speak(response)
            return voice_input

    except sr.UnknownValueError:
        user_text.set("Sorry, I didn't catch that.")
        assistant_text.set("Please try again.")
    except Exception as e:
        user_text.set("Error occurred.")
        assistant_text.set(str(e))

# Button callback to trigger threaded listening
def on_speak_click():
    user_text.set("Listening...")
    speak(listening_Text)
    assistant_text.set("Waiting")
    threading.Thread(target=listen_and_respond_thread, daemon=True).start()


def on_Stop():
    page3.after(10,lambda : speak(EndSpeak_text))
    terminate_p = Terminate_window(500) #delay 


def Terminate_window(time):
    root.after(time,root.destroy)

def slide_in(from_frame, to_frame , x=None):
    #print(f"Test X : {width}")
    if x is None:
        x = root.winfo_width()
        print(f"Test X : {x}")


    to_frame.place(x=x,y=0,relwidth = 1,relheight = 1)
    to_frame.lift()



    if x > 0:
        x -= 10
        to_frame.place(x=x, y=0)
        root.after(10, lambda: slide_in(from_frame, to_frame, x))

    else:
        from_frame.place_forget()
        to_frame.place(x=0,y=0,relwidth = 1,relheight = 1)




# Frame switcher
def show_frame(frame):
    frame.tkraise()



# GUI Setup
root = tk.Tk()
root.title("Voice Assistant")
root.geometry(f"{width}x{hieght}")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Pages setup
page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')


# Tkinter text variables (after root)
user_text = tk.StringVar() #auto uwpdate text 
assistant_text = tk.StringVar()

# ====== PAGE 1: Welcome ======
tk.Label(page1, text="Welcome to Voice Assistant", font=("Arial", 16)).pack(pady=30)
tk.Button(page1, text="Start", font=("Arial", 12), command=lambda: show_frame(page2)).pack(pady=10)
tk.Button(page1, text="Start_Test", font=("Arial", 12), command=lambda: slide_in(page1,page2)).pack(pady=10)
tk.Label(page1, text=Open_Text, font=("Arial", 14)).pack(pady=20)

# Speak welcome text once GUI starts
root.after(500, lambda: speak(Open_Text))

# ====== PAGE 2: Assistant ======
tk.Label(page2, text="Voice Assistant", font=("Arial", 16)).pack(pady=10)
tk.Label(page2, textvariable=user_text, fg="blue", wraplength=400).pack(pady=5)
tk.Label(page2, textvariable=assistant_text, fg="green", wraplength=400).pack(pady=5)
ttk.Button(page2, text="🎤 Speak", command=on_speak_click).pack(pady=20)
ttk.Button(page2, text="Back", command=lambda: show_frame(page1)).pack(pady=10)
ttk.Button(page2, text="Next Page ", command=lambda: show_frame(page3)).pack(pady=10)


tk.Label(page3, text="Voice Assistant", font=("Arial", 16)).pack(pady=10)
tk.Label(page3,text = Credit_text, font=("Arial",16) ).pack(pady=10)
tk.Button(page3,text = "Stop Assitance",font=("Arial",16),command=on_Stop).pack(pady=10,padx=10)


# Show the first page
show_frame(page1)

# Run app
root.mainloop()
