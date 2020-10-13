from tkinter import *
from random import randint


my_window = Tk()
my_window.geometry("1020x220")
my_window.title("Kubikud")
cvs = Canvas(my_window, width=1020, height=220)
cvs.configure(background = "white")


cvs.create_rectangle(20,20,200,200,fill="yellow")
cvs.create_rectangle(220,20,400,200,fill="yellow")
cvs.create_rectangle(420,20,600,200,fill="yellow")
cvs.create_rectangle(620,20,800,200,fill="yellow")
cvs.create_rectangle(820,20,1000,200,fill="yellow")


x1 = 30
x2 = 70

    
def number1():
    a = cvs.create_oval(x1, 90, x2, 130, fill = "black")
    cvs.move(a, 60, 0)

def number2():
    a = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(a, 0, 120)
    b = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(b, 120, 0)

def number3():
    a = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(a, 0, 120)
    b = cvs.create_oval(x1, 90, x2, 130, fill = "black")
    cvs.move(b, 60, 0)
    c = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(c, 120, 0)

def number4():
    a = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    b = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(b, 120, 0)
    c = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(c, 0, 120)
    d = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(d, 120, 120)

def number5():
    cvs.create_oval(x1, 30, x2, 70, fill = "black")
    a = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    b = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(b, 120, 0)
    c = cvs.create_oval(x1, 90, x2, 130, fill = "black")
    cvs.move(c, 60, 0)
    d = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(d, 0, 120)
    e = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(e, 120, 120)

def number6():
    a = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    b = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(b, 120, 0)
    c = cvs.create_oval(x1, 90, x2, 130, fill = "black")
    cvs.move(c, 0, 0)
    d = cvs.create_oval(x1, 90, x2, 130, fill = "black")
    cvs.move(d, 120, 0)
    e = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(e, 0, 120)
    f = cvs.create_oval(x1, 30, x2, 70, fill = "black")
    cvs.move(f, 120, 120)


for i in range(5):
    num = randint(1,6)
    if num == 1:
        number1()
    elif num == 2:
        number2()
    elif num == 3:
        number3()
    elif num == 4:
        number4()
    elif num == 5:
        number5()
    else:
        number6()
    x1 = x1 + 200
    x2 = x2 + 200


cvs.pack()
my_window.mainloop
