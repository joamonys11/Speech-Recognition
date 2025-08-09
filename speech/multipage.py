import tkinter as tk 


root = tk.Tk()


width = 400
hieght = 300

root.title ("Multi_Page App")
root.geometry(f"{width}x{hieght}")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

page1= tk.Frame(root,bg= "lightblue")
page2= tk.Frame(root,bg= "lightgreen")
page3= tk.Frame(root,bg= "black")


for frame in (page1,page2,page3):
    frame.grid(row=0,column=0,sticky="nsew")


def show_frame(frame):
    frame.tkraise()


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



tk.Label(page1,text ="Page 1 ",font=("Arial",18)).pack(padx=10)
tk.Label(page1,text="Click button to go page 2",font=("Arial",16)).pack(padx=10)
tk.Button(page1,text = "CLick Here",command=lambda:slide_in(page1,page2),font=("Arial",16)).pack( side="left",padx=10)



show_frame(page1)
root.mainloop()