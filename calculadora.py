from tkinter import *
from math import *
from tkinter import ttk

# wn=Tk()
# ttk.Button(wn, text="hola mundo in tk").grid()
# wn.mainloop()

wn=Tk()
wn.geometry('400x400')
wn.config(bg='SlateBlue4')
wn.resizable(0,0)
wn.title("La Calculadora")

buttonColor="turquoise"
buttonWidth=5
buttonHeight=3
operator=""
screenText = StringVar()

def clear():
    global operator
    operator=""
    screenText.set("0")

def click(b):
    global operator
    operator+=str(b)
    screenText.set(operator)

def equal():
    global operator

    try:
        r = str(eval(operator))
    except:
        r = 'ERROR'
    
    operator=r
    screenText.set(r)


buttonCe= Button(wn, text="C", font=("arial",10,"bold"), background=buttonColor, height=buttonHeight, width=40, command=lambda:clear())
buttonCe.grid(row=1, column=0, columnspan=4, padx=2,pady=2)

button1 = Button(wn, text="1", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(1))
button1.grid(row=2,column=0,columnspan=1,pady=2,padx=2)
button2 = Button(wn, text="2", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(2))
button2.grid(row=2,column=1,columnspan=1,pady=2,padx=2)
button3 = Button(wn, text="3", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(3))
button3.grid(row=2, column=2, columnspan=1, padx=2, pady=2)

#botones segunda fila

button4 = Button(wn, text="4", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(4))
button4.grid(row=3, column=0, columnspan=1, padx=2, pady=2)
button5 = Button(wn, text="5", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(5))
button5.grid(row=3, column=1, columnspan=1, padx=2, pady=2)
button6 = Button(wn, text="6", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(6))
button6.grid(row=3, column=2, columnspan=1, padx=2, pady=2)

#botones tercera fila

button7 = Button(wn, text="7", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(7))
button7.grid(row=4, column=0, columnspan=1, padx=2, pady=2)
button8 = Button(wn, text="8", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(8))
button8.grid(row=4, column=1, columnspan=1, padx=2, pady=2)
button9 = Button(wn, text="9", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(9))
button9.grid(row=4, column=2, columnspan=1, padx=2, pady=2)

#botones cuarta fila

button0 = Button(wn, text="0", font=("arial", 10, "bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click(0))
button0.grid(row=5, column=0,   columnspan=1, padx=2, pady=2)
buttonFloat = Button(wn, text=".", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:click("."))
buttonFloat.grid(row=5, column=1, columnspan=1,padx=2,pady=2)
buttonEqual = Button(wn, text="=", font=("arial",10,"bold"), background=buttonColor, width=buttonWidth, height=buttonHeight, command=lambda:equal())
buttonEqual.grid(row=5, column=2, columnspan=1,padx=2,pady=2)

buttonAdd = Button(wn, text="+", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("+"))
buttonAdd.grid(row=2, column=3,   columnspan=1, padx=2, pady=2)
buttonSub = Button(wn, text="-", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("-"))
buttonSub.grid(row=3, column=3,   columnspan=1, padx=2, pady=2)
buttonMul = Button(wn, text="*", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("*"))
buttonMul.grid(row=4, column=3,   columnspan=1, padx=2, pady=2)
buttonDiv = Button(wn, text="/", font=("arial", 10, "bold"), background=buttonColor, width=10, height=buttonHeight, command=lambda:click("/"))
buttonDiv.grid(row=5, column=3,   columnspan=1, padx=2, pady=2)

screen=Entry(wn, font=("arial",20,"bold"), width=20, borderwidth=5, background="green2", textvariable=screenText)
screen.grid(row=0, column=0, columnspan=4, padx=4, pady=4)

wn.mainloop()

#asdasdasdasdasdasd