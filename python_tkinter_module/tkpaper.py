import tkinter as tk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    result_text = f"Name: {name}\nAge: {age}\nEmail: {email}"

    print(f"Form Submitted:\n{result_text}")

root = tk.Tk()
root.title("Test paper")
root.geometry("300x350")

label1=tk.Label(root, text="Enter Name:", font=("Arial",20,"bold"))
label1.grid(row=0, column=0)
name_entry = tk.Entry(root)

tk.Label(root, text="Enter Age:", font=("Arial",20,"bold"))
age_entry = tk.Entry(root)

tk.Label(root, text="Enter Email:",font=("Arial",20,"bold"))
email_entry = tk.Entry(root)

submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.pack()

root.mainloop()
