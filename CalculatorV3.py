
from ast import Lambda
from tkinter import *
from math import sqrt

root = Tk()
root.title("Basic Calculator")
add = "false"
take = "false"
multiply = "false"
devide = "false"

if add and take == "true":
    add="false"
    take= "false"
    multiply = "false"
elif take and multiply == "true":
    add ="false"
    take = "false"
    multiply = "false"
elif multiply and add == "true":
    add ="false"
    take = "false"
    multiply = "false"
elif multiply and add and take == "true":
    add ="false"
    take = "false"
    multiply = "false"




def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_add():
    getFirstNum()

    global add
    add = "true"
    e.delete(0, END)

def minus():
    getFirstNum()
    
    global take
    take = "true"
    e.delete(0, END)

def times():
    getFirstNum()

    global multiply
    multiply = "true"
    e.delete(0, END)

def devision():
    getFirstNum()

    global devide
    devide = "true"
    e.delete(0, END)

def square():
    getFirstNum()

    e.delete(0, END)
    e.insert(0, f_num * f_num)

def squareRoot():
    getFirstNum()

    e.delete(0, END)
    rooted = sqrt(f_num)
    e.insert(0, rooted)
    

def getFirstNum():
    firstNum = e.get()
    global f_num
    f_num = float(firstNum)


    
    

def button_equal():
    secondNumber = e.get()
    e.delete(0, END)
    sec_num = float(secondNumber)
    if add == "true":
        e.insert(0, f_num + sec_num)
        
        
    elif take == "true":
        e.insert(0, f_num - sec_num)
    
    elif multiply == "true":
        e.insert(0, f_num * sec_num)
    
    elif devide == "true":
        e.insert(0, f_num/sec_num)


       



def button_clear():
    e.delete(0, END)
    global take
    take = "false"

    global add
    add = "false"
    global multiply
    multiply = "false"
    global devide
    devide = "false"

e = Entry(root, width=35, borderwidth=5,)
e.grid(row=0, column=1, columnspan=3, padx = 10, pady=10)

Button1= Button(root, text="1", padx=40, pady=30, command= lambda: buttonClick(1))
Button2= Button(root, text="2", padx=40, pady=30, command=lambda: buttonClick(2))
Button3= Button(root, text="3", padx=40, pady=30, command=lambda: buttonClick(3))
Button4= Button(root, text="4", padx=40, pady=30, command=lambda: buttonClick(4))
Button5= Button(root, text="5", padx=40, pady=30, command=lambda: buttonClick(5))
Button6= Button(root, text="6", padx=40, pady=30, command=lambda: buttonClick(6))
Button7= Button(root, text="7", padx=40, pady=30, command=lambda: buttonClick(7))
Button8= Button(root, text="8", padx=40, pady=30, command=lambda: buttonClick(8))
Button9= Button(root, text="9", padx=40, pady=30, command=lambda: buttonClick(9))
Button0= Button(root, text="0", padx=40, pady=30, command=lambda: buttonClick(0))
buttonDecimal= Button(root, text=".", padx=40, pady=30, command=lambda:buttonClick("."))
buttonNegtive= Button(root, text="negtive",padx=121, pady=30, command=lambda:buttonClick("-"))
Button_Add= Button(root, text="+", padx=39, pady=30, command=lambda: button_add())
ButtonAC = Button(root, text="AC",  padx=91, pady=30,command=lambda: button_clear())
ButtonEqual= Button(root, text="=", padx=91, pady=30, command=lambda: button_equal())
ButtonTake= Button(root, text = "-", padx=40, pady=30, command= minus)
buttonTimes= Button(root, text = "x", padx=40, pady=30, command= times)
buttonDevide = Button(root, text= "÷", padx=40, pady= 30, command= devision)
buttonSquare = Button(root, text="x^2", padx=40, pady=30, command= square)
buttonRoot = Button(root, text = "√", padx=40, pady=30, command=squareRoot)

Button1.grid(row=3, column=1)
Button2.grid(row=3, column=2)
Button3.grid(row=3, column=3)

Button4.grid(row=2, column=1)
Button5.grid(row=2, column=2)
Button6.grid(row=2, column=3)

Button7.grid(row=1, column=1)
Button8.grid(row=1, column=2)
Button9.grid(row=1, column=3)

Button0.grid(row=4, column=1)
buttonDecimal.grid(row=6, column=3)
buttonNegtive.grid(row=8, column=1, columnspan=3)

ButtonAC.grid(row=4, column=2, columnspan=2)
ButtonEqual.grid(row=7,column=2,columnspan=2)
Button_Add.grid(row=5, column=1)
ButtonTake.grid(row=5, column=2)
buttonTimes.grid(row=5, column=3)
buttonDevide.grid(row=6, column=1)
buttonSquare.grid(row=6, column=2)
buttonRoot.grid(row=7, column=1)

root.mainloop()