import tkinter as tk

mainWindow = tk.Tk()

mainWindow.title("Gui_Calculator")
First_Label = tk.Label(mainWindow, text= " Numeric value 1",pady = (15))
First_Label.pack()
para1 = tk.Entry(mainWindow)
para1.pack()

Second_Label = tk.Label(mainWindow, text= "Numeric Value 2 ", pady = (15))
Second_Label.pack()

para2 = tk.Entry(mainWindow)
para2.pack()

num1 = 0;
num2 = 0;

def addition():
    try:
        num1 = int(para1.get())
        num2= int(para2.get())
        if (num2 > 0):
            o1 = num1 + num2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")


def substract():
    try:
        num1 = int(para1.get())
        num2 = int(para2.get())
        if (num2 > 0):
            o1 = num1 - num2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")


def multiply():
    try:
        num1 = int(para1.get())
        num2 = int(para2.get())
        if (num2 > 0):
            o1 = num1 * num2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        print("Input Values not integers ")
        Result.configure(text= "Input values cannot be string")

def divide():
    try:
        num1 = int(para1.get())
        num2 = int(para2.get())
        if (num2 > 0):
            o1 = num1 / num2;
        else:
            o1 = "divideByZeroError"
        Result.configure(text=o1)
    except ValueError:
        Result.configure(text= "Input values cannot be string")




button = tk.Button(mainWindow, text = "+", command = lambda: addition(), pady= (25))
button.pack()

button = tk.Button(mainWindow, text = "-", command= lambda: substract(), pady= (25))
button.pack()

button = tk.Button(mainWindow, text = "*", command= lambda: multiply(), pady= (25))
button.pack()

button = tk.Button(mainWindow, text = "/", command= lambda: divide(), pady= (25))
button.pack()

Result = tk.Label(mainWindow, text= "Result", pady= (15))
Result.pack()
mainWindow.mainloop()
