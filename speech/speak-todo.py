# # import tkinter as tk 


# # root = tk.Tk()
# # root.title("Todo List App")
# # root.geometry("400x500")
# # root.columnconfigure(0,weight=1)
# # root.rowconfigure(0,weight=1)


# # task_frame = tk.Frame(root)
# # task_frame.pack(pady=10,fill="both")

# # task_input_label = tk.Label(root,text = "Input Task ",width=30).pack(padx=10)
# # task_input = tk.Entry(root,width=30)
# # task_input.pack(padx=10)
# # task_des_label = tk.Label(root,text= "Input Description ",width=30).pack(padx=10)
# # task_description = tk.Entry(root,width=30)
# # task_description.pack(padx=10)
# # task_date_label = tk.Label(root,text=" Input Date ",width=30).pack(padx=10)
# # task_date_input = tk.Entry(root,width=30)
# # task_date_input.pack(padx=10)





# # def Add_Task():
# #     task = task_input.get()
# #     taskdes = task_description.get()
# #     taskdate = task_date_input.get()

# #     if task.strip() != "":
# #         task_container = tk.Frame(task_frame,bg="#f0f0f0",bd=1,relief="solid")
# #         task_container.pack(fill="x",padx=5,pady=(2,0))
# #         task_label = tk.Label(task_container,text=f"Your Task : {task}",anchor="w",bg="lightgray",width=30)
# #         task_label.pack(padx=5,pady=5,anchor="w")
# #         task_descrip = tk.Label(task_container,text=f"Description: {taskdes}",anchor="w",bg="lightgray",width=30)
# #         task_descrip.pack(padx=5,pady=5,anchor="w")
# #         taskdate = tk.Label(task_container,text=f"Description: {taskdes}",anchor="w",bg="lightgray",width=30)
# #         taskdate.pack(padx=5,pady=5,anchor="w")
# #         task_input.delete(0,tk.END)
# #         task_description.delete(0,tk.END)
# #         task_date_input.delete(0,tk.END)

# #         delete_button = tk.Button(task_container,text="Delete",fg="red",command=task_container.destroy)
# #         delete_button.pack(padx=5,pady=5,anchor="e")

# # tk.Button(root,text="Add Task",command=Add_Task).pack(padx=10)



# # root.mainloop()

# import tkinter as tk
# import speech_recognition as sr
# import pyttsx3
# import time


# root = tk.Tk()
# root.title("Todo List App")
# root.geometry("400x500")
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('rate', 150) 



# open_text = "Welcome to the Todo List App. You can add tasks and descriptions using voice commands or text input."



# # Frame to hold the list of tasks; this will expand/shrink as tasks change
# task_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
# task_frame.pack(fill="both", expand=True, padx=10, pady=(10,1))

# # Frame to hold input fields & buttons; stays at bottom
# input_frame = tk.Frame(root,bg="white",bd=2,relief="ridge")
# input_frame.pack(fill="both", padx=10, pady=10)

# # Inside input_frame: labels and entries
# tk.Label(input_frame, text="Input Task").grid(row=0, column=0, sticky="w")
# task_input = tk.Entry(input_frame,state="normal")
# task_input.grid(row=0, column=1, sticky="ew", padx=5)

# tk.Label(input_frame, text="Input Description").grid(row=1, column=0, sticky="w")
# task_description = tk.Entry(input_frame)
# task_description.grid(row=1, column=1, sticky="ew", padx=5)

# # Make the input_frame columns expand horizontally
# input_frame.columnconfigure(1, weight=1)

# def Speak(voice):
#     engine.say(voice)
#     engine.runAndWait()

# def Speech_Recognition():
#     try:
#         with sr.Microphone() as source:
#             audio = recognizer.listen(source)
#             voice_input = recognizer.recognize_google(audio)
#             voice_inputspeak = (f"You said {voice_input}")
#             Speak(voice_inputspeak)
#             print(voice_inputspeak)
#             return voice_input
#     except sr.UnknownValueError:
#         Speak("Sorry, I did not understand that.")
#         return None



# def add_task():
#     task_voice = Speech_Recognition()
#     if task_voice:
#         Respond(task_voice)




# def Respond(response):
#     print(response)
#     Speak(f"You said: {response}")
#     if response is None:
#         Speak("No input received. Please try again.")
#         return
#     elif "note" in response:
#         Speak("Adding Note")
#         listening = Speech_Recognition()
#         if listening is not None:
#             Speak(f"Note added: {listening}")
#             task_input.insert(0, listening)
#             if task_input.get().strip() != "":
#                 descriptio_Listen = Speech_Recognition()
#                 taskdes = descriptio_Listen if descriptio_Listen else "No description provided"
#                 task_container = tk.Frame(task_frame, bg="#f0f0f0", bd=1, relief="solid")
#                 task_container.pack(fill="x", pady=5)
#                 tk.Label(task_container, text=f"Task: {task_input.get()}", bg="lightgray").pack(anchor="w", padx=5)
#                 tk.Label(task_container, text=f"Description: {taskdes}", bg="lightgray").pack(anchor="w", padx=5)
#                 def delete_task():
#                     task_container.destroy()
#                     Speak(f"Task deleted: {task_input.get()}")
#                 tk.Button(task_container, text="Delete", fg="red", command=delete_task).pack(anchor="e", padx=5, pady=5)
#                 task_input.delete(0, tk.END)
#                 task_description.delete(0, tk.END)
#             else:   
#                 Speak("No input received for task. Waiting to try again.")
#         else:
#             Speak("No input received for note.")

# # Add a button to trigger voice commands
# tk.Button(input_frame, text="Voice Command", command=add_task).grid(row=3, column=0, columnspan=2, pady=5)

# Speak(open_text)
# root.mainloop()


# #main


import tkinter as tk
from tkinter import messagebox, ttk
import speech_recognition as sr
import pyttsx3
import threading
from datetime import datetime

class VoiceTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice-Controlled Todo List")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5f5f5")
        
        # Initialize speech components
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.8)
        
        # Task storage
        self.tasks = []
        self.task_id_counter = 1
        
        self.setup_ui()
        self.speak("Welcome to the Voice-Controlled Todo List App!")
    
    def speak(self, text):
        """Thread-safe text-to-speech"""
        print(f"Speaking: {text}")
        def speak_thread():
            self.engine.say(text)
            self.engine.runAndWait()
        
        # Run speech in separate thread to prevent GUI freezing
        thread = threading.Thread(target=speak_thread, daemon=True)
        thread.start()
    
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Voice Todo List", 
                              font=("Arial", 20, "bold"), 
                              bg="#f5f5f5", fg="#333")
        title_label.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready for voice commands", 
                                    font=("Arial", 10), 
                                    bg="#f5f5f5", fg="#666")
        self.status_label.pack(pady=5)
        
        # Task display frame
        self.task_frame = tk.Frame(self.root, bg="#fff", bd=2, relief="sunken")
        self.task_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Scrollable task area
        self.canvas = tk.Canvas(self.task_frame, bg="#fff")
        self.scrollbar = ttk.Scrollbar(self.task_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#fff")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg="#f5f5f5")
        control_frame.pack(fill="x", padx=20, pady=10)
        
        # Voice command button
        self.voice_btn = tk.Button(control_frame, text="🎤 Voice Command", 
                                  command=self.start_voice_command,
                                  font=("Arial", 12, "bold"),
                                  bg="#4CAF50", fg="white",
                                  padx=20, pady=10)
        self.voice_btn.pack(side="left", padx=5)
        
        # Manual add button
        manual_btn = tk.Button(control_frame, text="✏️ Add Manually", 
                              command=self.show_manual_input,
                              font=("Arial", 12),
                              bg="#2196F3", fg="white",
                              padx=20, pady=10)
        manual_btn.pack(side="left", padx=5)
        
        # Clear all button
        clear_btn = tk.Button(control_frame, text="🗑️ Clear All", 
                             command=self.clear_all_tasks,
                             font=("Arial", 12),
                             bg="#f44336", fg="white",
                             padx=20, pady=10)
        clear_btn.pack(side="right", padx=5)
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)
        self.root.update()
    
    def listen_for_speech(self, prompt="Listening..."):
        """Capture speech input"""
        try:
            self.update_status(prompt)
            self.speak(prompt)
            
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
                
            self.update_status("Processing speech...")
            voice_input = self.recognizer.recognize_google(audio)
            self.speak(f"You said: {voice_input}")
            return voice_input.lower()
            
        except sr.WaitTimeoutError:
            self.speak("No speech detected. Please try again.")
            self.update_status("No speech detected")
            return None
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand that. Please try again.")
            self.update_status("Speech not recognized")
            return None
        except sr.RequestError as e:
            self.speak("Sorry, there was an error with the speech service.")
            self.update_status("Speech service error")
            return None
    
    def start_voice_command(self):
        """Handle voice commands in a separate thread"""
        def voice_thread():
            self.voice_btn.config(state="disabled", text="🎤 Listening...")
            try:
                self.process_voice_command()
            finally:
                self.voice_btn.config(state="normal", text="🎤 Voice Command")
                self.update_status("Ready for voice commands")
        
        thread = threading.Thread(target=voice_thread, daemon=True)
        thread.start()
    
    def process_voice_command(self):
        """Process voice commands"""
        command = self.listen_for_speech("Say 'add task' to create a new task, or 'list tasks' to hear your tasks")
        
        if not command:
            return
        
        if "add" in command and ("task" in command or "todo" in command):
            self.add_task_by_voice()
        elif "list" in command and "task" in command:
            self.list_tasks_by_voice()
        elif "delete" in command or "remove" in command:
            self.delete_task_by_voice()
        elif "clear" in command and "all" in command:
            self.clear_all_tasks()
        else:
            self.speak("I didn't understand that command. Try saying 'add task', 'list tasks', or 'delete task'")
    
    def add_task_by_voice(self):
        """Add task using voice input"""
        self.speak("Let's add a new task!")
        
        # Get task title
        title = None
        attempts = 0
        while not title and attempts < 3:
            title = self.listen_for_speech("Please say the task title")
            attempts += 1
            if not title:
                self.speak("I didn't catch that. Let me try again.")
        
        if not title:
            self.speak("I couldn't get the task title. Please try again later.")
            return
        
        # Get description
        description = self.listen_for_speech("Now say the task description, or say 'skip' for no description")
        if description and "skip" in description:
            description = "No description"
        elif not description:
            description = "No description"
        
        # Get due date
        due_date = self.listen_for_speech("Say the due date, or say 'skip' for no date")
        if due_date and "skip" in due_date:
            due_date = "No due date"
        elif not due_date:
            due_date = "No due date"
        
        # Create the task
        self.create_task(title, description, due_date)
        self.speak(f"Task '{title}' has been added successfully!")
    
    def create_task(self, title, description, due_date):
        """Create a task widget"""
        task_id = self.task_id_counter
        self.task_id_counter += 1
        
        # Task container
        task_container = tk.Frame(self.scrollable_frame, bg="#e8f5e8", 
                                 bd=2, relief="sunken", padx=10, pady=5)
        task_container.pack(fill="both", pady=5, padx=5)
        
        # Task header
        header_frame = tk.Frame(task_container, bg="#e8f5e8")
        header_frame.pack(fill="both", pady=(0, 5))
        
        tk.Label(header_frame, text=f"Task #{task_id}", 
                font=("Arial", 10, "bold"), 
                bg="#e8f5e8", fg="#2e7d32").pack(side="left")
        
        tk.Label(header_frame, text=datetime.now().strftime("%Y-%m-%d %H:%M"), 
                font=("Arial", 8), 
                bg="#e8f5e8", fg="#666").pack(side="right")
        
        # Task content
        tk.Label(task_container, text=f"📝 {title}", 
                font=("Arial", 12, "bold"), 
                bg="#e8f5e8", anchor="w").pack(fill="x", pady=2)
        
        tk.Label(task_container, text=f"📄 {description}", 
                bg="#e8f5e8", anchor="w", 
                wraplength=400).pack(fill="x", pady=2)
        
        tk.Label(task_container, text=f"📅 {due_date}", 
                bg="#e8f5e8", anchor="w").pack(fill="x", pady=2)
        
        # Delete button
        def delete_this_task():
            task_container.destroy()
            self.tasks = [t for t in self.tasks if t['id'] != task_id]
            self.speak(f"Task {task_id} deleted")
        
        tk.Button(task_container, text="❌ Delete", 
                 command=delete_this_task,
                 bg="#f44336", fg="white",
                 font=("Arial", 9)).pack(anchor="e", pady=5)
        
        # Store task data
        task_data = {
            'id': task_id,
            'title': title,
            'description': description,
            'due_date': due_date,
            'created': datetime.now()
        }
        self.tasks.append(task_data)
        
        # Update scroll region
        self.root.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def list_tasks_by_voice(self):
        """Read out all tasks"""
        if not self.tasks:
            self.speak("You have no tasks in your list.")
            return
        
        self.speak(f"You have {len(self.tasks)} tasks:")
        for i, task in enumerate(self.tasks, 1):
            self.speak(f"Task {i}: {task['title']}")
    
    def delete_task_by_voice(self):
        """Delete task by voice command"""
        if not self.tasks:
            self.speak("You have no tasks to delete.")
            return
        
        self.speak(f"You have {len(self.tasks)} tasks. Which task number would you like to delete?")
        
        response = self.listen_for_speech("Say the task number to delete")
        if not response:
            return
        
        # Extract number from response
        import re
        numbers = re.findall(r'\d+', response)
        if numbers:
            task_num = int(numbers[0])
            if 1 <= task_num <= len(self.tasks):
                task_to_delete = self.tasks[task_num - 1]
                # Find and destroy the corresponding widget
                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()
                
                # Remove from tasks list
                self.tasks.pop(task_num - 1)
                
                # Recreate all remaining tasks
                for task in self.tasks:
                    self.create_task(task['title'], task['description'], task['due_date'])
                
                self.speak(f"Deleted task: {task_to_delete['title']}")
            else:
                self.speak("Invalid task number.")
        else:
            self.speak("I couldn't understand the task number.")
    
    def show_manual_input(self):
        """Show manual input dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Task Manually")
        dialog.geometry("400x300")
        dialog.configure(bg="#f5f5f5")
        
        tk.Label(dialog, text="Task Title:", bg="#f5f5f5").pack(pady=5)
        title_entry = tk.Entry(dialog, width=50)
        title_entry.pack(pady=5)
        
        tk.Label(dialog, text="Description:", bg="#f5f5f5").pack(pady=5)
        desc_entry = tk.Text(dialog, width=50, height=5)
        desc_entry.pack(pady=5)
        
        tk.Label(dialog, text="Due Date:", bg="#f5f5f5").pack(pady=5)
        date_entry = tk.Entry(dialog, width=50)
        date_entry.pack(pady=5)
        
        def add_manual_task():
            title = title_entry.get().strip()
            description = desc_entry.get("1.0", tk.END).strip()
            due_date = date_entry.get().strip()
            
            if title:
                self.create_task(
                    title, 
                    description if description else "No description",
                    due_date if due_date else "No due date"
                )
                dialog.destroy()
                self.speak(f"Task '{title}' added manually!")
            else:
                messagebox.showerror("Error", "Task title is required!")
        
        tk.Button(dialog, text="Add Task", command=add_manual_task,
                 bg="#4CAF50", fg="white", pady=5).pack(pady=10)
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if not self.tasks:
            self.speak("No tasks to clear.")
            return
        
        result = messagebox.askyesno("Clear All Tasks", 
                                   "Are you sure you want to delete all tasks?")
        if result:
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            self.tasks.clear()
            self.task_id_counter = 1
            self.speak("All tasks have been cleared.")

def main():
    root = tk.Tk()
    app = VoiceTodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()