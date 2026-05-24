# import tkinter as tk

# root=tk.Tk()
# root.title("student form")
# root.geometry("500x400")

# #Title
# title=tk.Label(root,text="student form", font=("Arial",20,"bold"))
# title.grid(row=0, column=5)

# # name 
# label_name=tk.Label(root,text="name",font=("Arial",20,"bold"))
# label_name.grid(row=1, column=0)

# entry_name=tk.Entry(root,font=("Arial",15))
# entry_name.grid(row=1,column=1)

# #Gender
# label_gender=tk.Label(root, text="Gender:-", font=("Arial",20,"bold"))
# label_gender.grid(row=2,column=0)

# gender=tk.StringVar()

# male=tk.Radiobutton(root, text="Male", variable=gender, value="Male", font=("Arial",15))
# male.grid(row=2,column=1)

# female=tk.Radiobutton(root, text="Female", variable=gender, value="Female",font=("Arial",15))
# female.grid(row=3,column=1)

# #subject
# label_subject=tk.Label(root, text="Subject:-", font=("Arial",20,"bold"))
# label_subject.grid(row=4,column=0)

# subject=tk.StringVar()

# python_but=tk.Radiobutton(root, text="Python", variable=subject, value="python", font=("Arial",15))
# python_but.grid(row=4,column=1)

# java_but=tk.Radiobutton(root, text="java", variable=subject,  value="java", font=("Arial",15))
# java_but.grid(row=5,column=1)

# C_but=tk.Radiobutton(root, text="C++", variable=subject,  value="C", font=("Arial",15))
# C_but.grid(row=6,column=1)


# #submit function
# def submit():
#     name=entry_name.get()
#     g=gender.get()
#     sub=subject.get()

#     print(f"---- information of student -----")
#     print("name:",name)
#     print("gender:",g)
#     print("subject:",sub)

# submit_but=tk.Button(root, text="Submit", command=submit, font=("Arial",15))
# submit_but.grid(row=7,column=2)
    

# root.mainloop()

import tkinter as tk 
def login(): 
    if entry_username.get() == "admin" and entry_password.get() == "password": 
        label_status.config(text="Login Successful", fg="green") 
    else: 
        label_status.config(text="Login Failed", fg="red") 
root = tk.Tk() 
root.geometry("400x400")
tk.Label(root, text="Username:").pack() 
entry_username = tk.Entry(root) 
entry_username.pack() 
tk.Label(root, text="Password:").pack() 
entry_password = tk.Entry(root, show="*") 
entry_password.pack() 
tk.Button(root, text="Login", command=login).pack() 
label_status = tk.Label(root, text="") 
label_status.pack() 
root.mainloop()