from tkinter import *

def leftClickButton(Event):
    def BMIresult(BMI):  # ผลลัพธ์หลังจากคำนวน
        if BMI <= 18.5:
            result.configure(text="Too thin")
        elif (BMI > 18.5) and BMI <= 23.0:
            result.configure(text="Normal weight")
        elif (BMI > 23.0) and BMI < 24.0:
            result.configure(text="Overweight")
        elif (BMI >= 24) and BMI < 30.0:
            result.configure(text="Fat")
        else:
            result.configure(text="Very fat")

    windowTwo = Tk()
    windowTwo.title("Result Calculate")
    windowTwo.geometry("200x40")
    Label(windowTwo, text="BMI : ").grid(row=0, column=0)
    result = Label(windowTwo, text="Result")
    result.grid(row=1, column=1)
    resultNumber = Label(windowTwo, text="Number Result")
    resultNumber.grid(row=0, column=1)
    weight = float(textBox2.get())
    height = float(textBox.get())/100
    BMI = weight/(height**2)
    resultNumber.configure(text="%.2f" %(BMI))
    BMIresult(BMI)
    windowTwo.mainloop()

mainWindow = Tk()

mainWindow.title("BMI")
label = Label(mainWindow, text="Height (cm.)")
label.grid(row=0, column=0)
textBox = Entry(mainWindow)
textBox.grid(row=0, column=1)

label2 = Label(mainWindow, text="weight (kg.)")
label2.grid(row=1, column=0)
textBox2 = Entry(mainWindow)
textBox2.grid(row=1,column=1)

calculateButton = Button(mainWindow, text="Calculate BMI")
calculateButton.grid(row=2, column=1)
calculateButton.bind("<Button-1>", leftClickButton)

mainWindow.mainloop()