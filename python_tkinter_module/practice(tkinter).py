import tkinter as tk

root=tk.Tk()
root.geometry("400x400")
root.title("my first GUI window")

#label
# label=tk.Label(root,text="hello.Alpesh",font=("Arial",20,"bold"))
# label.pack()

# label1=tk.Label(root,text="Name:")
# label1.grid(row=0,column=0)

# label2=tk.Label(root,text="Gender:")
# label2.grid(row=1,column=0)

#Entry
# entry=tk.Entry(root)
# entry.pack()

# entry1 = tk.Entry(root) 
# entry1.grid(row=0, column=1) 

#BUTTON
# button=tk.Button(root,text="Submit",command=lambda:print("Button Clicked"))
# button.pack()

# button = tk.Button(root, text="Submit", command=lambda:print("submit successfuly-")) 
# button.grid(row=2, column=1) 


''' 4 .Event handling & commands'''
# def on_click():
#     label.config(text="Button Clicked!")

# label=tk.Label(root,text="Click the button")
# label.grid(row=2,column=1)

# button=tk.Button(root,text="click,Me",command=on_click)
# button.grid(row=3,column=1)


''' 5 Tkinter widgets (Advanced)
    5.1 Checkboxes and radio button '''
# but=tk.StringVar(value="option1")

# rb1=tk.Radiobutton(root,text="option1",variable=but,value="option1")
# rb2=tk.Radiobutton(root,text="option2",variable=but,value="option2")

# rb1.pack()
# rb2.pack()

''' 5.2 listbox and scrollbar '''
# listbox=tk.Listbox(root)
# listbox.pack()

# for i in range(100):
#     listbox.insert(tk.END, f"Item {i}")


'''  5.3 Canvas for Drawing '''
# canvas=tk.Canvas(root,width=200,height=200)
# canvas.pack()

# canvas.create_line(0,0,200,200)
# canvas.create_rectangle(50,50,150,150,fill="pink")


'''  6. Tkinter Menus 
    6.1 Creating a simple menu '''
# menu=tk.Menu(root)
# root.config(menu=menu)

# file_menu=tk.Menu(menu)
# menu.add_cascade(label="file",menu=file_menu)
# file_menu.add_command(label="open")
# file_menu.add_command(label="Exit",command=root.quit)


from tkinter import messagebox 
def show_message(): 
    messagebox.showinfo("Info", "This is a message box!")
button = tk.Button(root, text="Show Message", command=show_message) 
button.pack()
root.mainloop()

