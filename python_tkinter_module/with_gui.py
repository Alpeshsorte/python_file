# import tkinter as tk

# root=tk.Tk()
# root.title("----MY GUI---")
# root.geometry("500x500")

# label1=tk.Label(root,text="Form",font=("Arial",20,"bold"))
# label1.grid(row=0,column=0)

# label2=tk.Label(root,text="Name",font=("Arial",15,"bold"))
# label2.grid(row=1,column=0)

# label3=tk.Label(root,text="Gender",font=("Arial",16))
# label3.grid(row=2,column=0)


# label=tk.Radiobutton(root,text="male",font=("Arial",15))
# label.grid(row=3,column=1)


# label=tk.Radiobutton(root,text="female",font=("Arial",15))
# label.grid(row=2,column=1)

# label4=tk.Label(root,text="Subject",font=("Arial",16))
# label4.grid(row=4,column=0)

# label=tk.Radiobutton(root,text="python",font=("Arial",15))
# label.grid(row=4,column=1)


# label=tk.Radiobutton(root,text="java",font=("Arial",15))
# label.grid(row=4,column=1)

# label=tk.Radiobutton(root,text="C++",font=("Arial",15))
# label.grid(row=4,column=1)

# entry1=tk.Entry(root,font=("Arial",16))
# entry1.grid(row=1,column=1)



# button1=tk.Button(root,text="submit",font=("Arial",16))
# button1.grid(row=5,column=0)

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Student Form")
root.geometry("500x400")

# Title
title = tk.Label(root, text="Student Form", font=("Arial",20,"bold"))
title.grid(row=0, column=1, pady=10)

# Name
label_name = tk.Label(root, text="Name", font=("Arial",14))
label_name.grid(row=1, column=0, padx=10, pady=10)

entry_name = tk.Entry(root, font=("Arial",14))
entry_name.grid(row=1, column=1)

# Gender
label_gender = tk.Label(root, text="Gender", font=("Arial",14))
label_gender.grid(row=2, column=0)

gender = tk.StringVar()

male = tk.Radiobutton(root, text="Male", variable=gender, value="Male", font=("Arial",12))
male.grid(row=2, column=1, sticky="w")

female = tk.Radiobutton(root, text="Female", variable=gender, value="Female", font=("Arial",12))
female.grid(row=3, column=1, sticky="w")

# Subject
label_subject = tk.Label(root, text="Subject", font=("Arial",14))
label_subject.grid(row=4, column=0)

subject = tk.StringVar()

python_rb = tk.Radiobutton(root, text="Python", variable=subject, value="Python", font=("Arial",12))
python_rb.grid(row=4, column=1, sticky="w")

java_rb = tk.Radiobutton(root, text="Java", variable=subject, value="Java", font=("Arial",12))
java_rb.grid(row=5, column=1, sticky="w")

cpp_rb = tk.Radiobutton(root, text="C++", variable=subject, value="C++", font=("Arial",12))
cpp_rb.grid(row=6, column=1, sticky="w")

# Submit Function
def submit():
    name = entry_name.get()
    g = gender.get()
    sub = subject.get()

    print("Name:", name)
    print("Gender:", g)
    print("Subject:", sub)

# Button
button = tk.Button(root, text="Submit", command=submit, font=("Arial",14))
button.grid(row=7, column=1, pady=20)

root.mainloop()