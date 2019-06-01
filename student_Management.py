import sqlite3
import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("Student Management Database ")

Name_Label = tk.Label(text="Enter Name", pady =(12))
Name_Field = tk.Entry( )
Name_Label.pack( )
Name_Field.pack()
College_Label = tk.Label(text="College Name" , pady =(12))
College_Field = tk.Entry()
College_Label.pack()
College_Field.pack()
Phone_Label = tk.Label(text="Enter Phone Number", pady =(12)).pack()
Phone_Field = tk.Entry()
Phone_Field.pack()
Location_Label = tk.Label(text = "Address", pady = (12)).pack()
Location_Field = tk.Entry()
Location_Field.pack()

connection = sqlite3.connect('student_records.db')
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
def enterData():
    try:
        Name = Name_Field.get()
        College = College_Field.get()
        Phone = Phone_Field.get()
        Address = Location_Field.get()
        if len(Name) <= 0 or len(College) <= 0  :
            Result.config(text = "Fields cannot be blank")
        else:
            connection.execute("INSERT INTO " + "student_table"+ " ( " +
                               STUDENT_NAME + ", " +
                               STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                               ", " + STUDENT_PHONE +
                               " ) VALUES ( '" + Name + "', '" + College + "', " +
                               "'" + Address + "', "+ Phone + " ); ")
            connection.commit()
    except ValueError:
        print("An Exception Occured query not executed ")
        Result.config(text="Invalid Entry ")
def Quit():
    exit(0)

b1 = tk.Button(mainWindow, text = "Enter Value", command=lambda: enterData())
b1.pack()
b2 = tk.Button(mainWindow, text = "Quit", command = lambda: Quit())
b2.pack()
Result = tk.Label(mainWindow, text= "", pady= (10))
Result.pack()
mainWindow.mainloop()
