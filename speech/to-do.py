# import tkinter as tk 


# root = tk.Tk()
# root.title("Todo List App")
# root.geometry("400x500")
# root.columnconfigure(0,weight=1)
# root.rowconfigure(0,weight=1)


# task_frame = tk.Frame(root)
# task_frame.pack(pady=10,fill="both")

# task_input_label = tk.Label(root,text = "Input Task ",width=30).pack(padx=10)
# task_input = tk.Entry(root,width=30)
# task_input.pack(padx=10)
# task_des_label = tk.Label(root,text= "Input Description ",width=30).pack(padx=10)
# task_description = tk.Entry(root,width=30)
# task_description.pack(padx=10)
# task_date_label = tk.Label(root,text=" Input Date ",width=30).pack(padx=10)
# task_date_input = tk.Entry(root,width=30)
# task_date_input.pack(padx=10)





# def Add_Task():
#     task = task_input.get()
#     taskdes = task_description.get()
#     taskdate = task_date_input.get()

#     if task.strip() != "":
#         task_container = tk.Frame(task_frame,bg="#f0f0f0",bd=1,relief="solid")
#         task_container.pack(fill="x",padx=5,pady=(2,0))
#         task_label = tk.Label(task_container,text=f"Your Task : {task}",anchor="w",bg="lightgray",width=30)
#         task_label.pack(padx=5,pady=5,anchor="w")
#         task_descrip = tk.Label(task_container,text=f"Description: {taskdes}",anchor="w",bg="lightgray",width=30)
#         task_descrip.pack(padx=5,pady=5,anchor="w")
#         taskdate = tk.Label(task_container,text=f"Description: {taskdes}",anchor="w",bg="lightgray",width=30)
#         taskdate.pack(padx=5,pady=5,anchor="w")
#         task_input.delete(0,tk.END)
#         task_description.delete(0,tk.END)
#         task_date_input.delete(0,tk.END)

#         delete_button = tk.Button(task_container,text="Delete",fg="red",command=task_container.destroy)
#         delete_button.pack(padx=5,pady=5,anchor="e")

# tk.Button(root,text="Add Task",command=Add_Task).pack(padx=10)



# root.mainloop()

import tkinter as tk
import speech_recognition as sr
import pyttsx3

root = tk.Tk()
root.title("Todo List App")
root.geometry("400x500")
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150) 

# Frame to hold the list of tasks; this will expand/shrink as tasks change
task_frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
task_frame.pack(fill="both", expand=True, padx=10, pady=(10,1))

# Frame to hold input fields & buttons; stays at bottom
input_frame = tk.Frame(root,bg="white",bd=2,relief="ridge")
input_frame.pack(fill="both", padx=10, pady=10)

# Inside input_frame: labels and entries
tk.Label(input_frame, text="Input Task").grid(row=0, column=0, sticky="w")
task_input = tk.Entry(input_frame,state="normal")
task_input.grid(row=0, column=1, sticky="ew", padx=5)

tk.Label(input_frame, text="Input Description").grid(row=1, column=0, sticky="w")
task_description = tk.Entry(input_frame)
task_description.grid(row=1, column=1, sticky="ew", padx=5)

# Make the input_frame columns expand horizontally
input_frame.columnconfigure(1, weight=1)


def Speak(voice):
    engine.say(voice)
    engine.runAndWait()

def add_task():
    task = task_input.get()
    taskdes = task_description.get()
    Speak(f"Task added: {task} with description {taskdes}")
    if task.strip() != "":
        task_container = tk.Frame(task_frame, bg="#f0f0f0", bd=1, relief="solid")
        task_container.pack(fill="x", pady=5)

        tk.Label(task_container, text=f"Task: {task}", bg="lightgray").pack(anchor="w", padx=5)
        tk.Label(task_container, text=f"Description: {taskdes}", bg="lightgray").pack(anchor="w", padx=5)

        def delete_task():
            task_container.destroy()
            Speak(f"Task deleted: {task}")

        tk.Button(task_container, text="Delete", fg="red", command=delete_task).pack(anchor="e", padx=5, pady=5)

        # Clear inputs
        task_input.delete(0, tk.END)
        task_description.delete(0, tk.END)

tk.Button(input_frame, text="Add Task",command=add_task).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
