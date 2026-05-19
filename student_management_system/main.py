import json
import csv
import os
students = []
while True:
    print("=========== student management system===========")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter the select options ")
    if choice == "1":
        print("===== Add student ====")
        def add_student():
            try:
                roll_number = int(input("Enter the roll number=="))
                name = input("Enter the student name==")
                course = input("Enter the course name==")
                marks = int(input("Enter the marks=="))
                for s in students:
                    if s["roll"] == roll_number:
                        print("already roll number present ")
                    student_data = {
                        "roll": roll_number,
                        "name": name,
                        "course": course,
                        "marks": marks
                    }
                    students.append(student_data)
                print("student add successfully")
            except ValueError:
                print("error in the add student section ")
        add_student()
    elif choice == "2":
        def view_student():
            if len(students) == 0:
                print("no student found")
                return
            print("roll\t name\t course\t marks")
            for s in students:
                print(s["roll"], s["name"], s["course"], s["marks"])
        view_student()
    elif choice == "3":
        def search_student():
            try:
                roll = int(input("Enter Roll Number : "))
                for student in students:
                    if student["roll"] == roll:
                        print("Student Found")
                        print("Roll :", student["roll"])
                        print("Name :", student["name"])
                        print("Course :", student["course"])
                        print("Marks :", student["marks"])
                        return
                print("Student Not Found")
            except ValueError:
                print("Invalid Input")
        search_student()
    elif choice == "4":
        def update_student():
            try:
                roll = int(input("Enter Roll Number : "))
                for student in students:
                    if student["roll"] == roll:
                        student["name"] = input("Enter New Name : ")
                        student["course"] = input("Enter New Course : ")
                        student["marks"] = float(input("Enter New Marks : "))
                        print("Student Updated Successfully")
                        return
                print("Student Not Found")
            except ValueError:
                print("Invalid Input")
        update_student()
    elif choice == "5":
        def delete_student():
            try:
                roll = int(input("Enter Roll Number : "))
                for student in students:
                    if student["roll"] == roll:
                        students.remove(student)
                        print("Student Deleted Successfully")
                        return
                print("Student Not Found")
            except ValueError:
                print("Invalid Input")
        delete_student()
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("========= Error in the code ===")