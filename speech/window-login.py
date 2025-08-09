import tkinter as tk 


root = tk.Tk()
root.title("Test Dialog")
root.geometry("400x500")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)



#page1 
page1 = tk.Frame(root)
page2 = tk.Frame(root)


for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky='nsew')


user_input = tk.StringVar()
pass_input = tk.StringVar()
user_Default = "admin"
pass_Default = "1234"

result_label = tk.Label(page1,text ="")
result_label.pack()


def on_login():
    username = user_input.get()
    password = pass_input.get()
    print(f"User name : {username} and Password : {pass_input}" )

    if username == user_Default and password == pass_Default:
        result_label.config(text = "Login Success",fg="green" )
        root.after(10,lambda : slide_in(page1,page2))
    else:
        result_label.config(text = "Fail Login",fg="red" )




tk.Label(page1,text = "Login Form",font=("Arial",16 )).pack(pady=10)
tk.Label(page1,text = "User Name",font=("Arial",16)).pack(pady=10)
tk.Entry(page1,textvariable = user_input).pack(pady=10,padx=10)
tk.Label(page1,text = "Password",font=("Arial",16)).pack(pady=10)
tk.Entry(page1,textvariable=pass_input,show = "*").pack(padx=10,pady=10)
tk.Button(page1,text = "Login",command=on_login).pack(padx=10,pady=10)


#page2
tk.Label(page2,text= "Welcome",font=("Arial",16)).pack(padx=10)





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

def show_frame(frame):
    frame.tkraise()



show_frame(page1)
root.mainloop()

# import tkinter as tk 

# root = tk.Tk()
# root.title("Test Dialog")
# root.geometry("400x500")
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# # Pages
# page1 = tk.Frame(root)
# page2 = tk.Frame(root)

# for frame in (page1, page2):
#     frame.grid(row=0, column=0, sticky='nsew')

# # Variables
# user_input = tk.StringVar()
# pass_input = tk.StringVar()

# user_Default = "admin"
# pass_Default = "1234"  # Use string for simplicity

# # Result label (declared early so it's visible in on_login)
# result_label = tk.Label(page1, text="", font=("Arial", 12))
# result_label.pack()

# # Login function
# def on_login():
#     username = user_input.get()
#     password = pass_input.get()

#     if username == user_Default and password == pass_Default:
#         result_label.config(text="Login Success", fg="green")
#         root.after(10, lambda: slide_in(page1, page2))
#     else:
#         result_label.config(text="Login Failed", fg="red")

# # UI for page1
# tk.Label(page1, text="Login Form", font=("Arial", 16)).pack(pady=10)
# tk.Label(page1, text="User Name", font=("Arial", 12)).pack()
# tk.Entry(page1, textvariable=user_input).pack(pady=5)
# tk.Label(page1, text="Password", font=("Arial", 12)).pack()
# tk.Entry(page1, textvariable=pass_input, show="*").pack(pady=5)
# tk.Button(page1, text="Login", command=on_login).pack(pady=10)

# # Dummy page2 content
# tk.Label(page2, text="Welcome!", font=("Arial", 20)).pack(pady=100)

# # Slide animation
# def slide_in(from_frame, to_frame, x=None):
#     if x is None:
#         x = root.winfo_width()
#     to_frame.place(x=x, y=0, relwidth=1, relheight=1)
#     to_frame.lift()
#     if x > 0:
#         x -= 20
#         root.after(10, lambda: slide_in(from_frame, to_frame, x))
#     else:
#         from_frame.place_forget()
#         to_frame.place(x=0, y=0, relwidth=1, relheight=1)

# # Start
# page1.tkraise()
# root.mainloop()


