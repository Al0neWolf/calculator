from Useful import *

def base(num):
    pass

def fact(inp):
    global eq
    num = 1
    for i in inp:
        num *= i
    eq = num
    eqlabel.set(eq)
        

def button_press(num):
    global eq
    eq += str(num)
    eqlabel.set(eq)

def equals():
    global eq
    
    try:
        total = str(eval(eq))
        eqlabel.set(total)
        eq = total
    
    except ZeroDivisionError:
        eqlabel.set("NaN")
        eq = ""
    except SyntaxError:
        eqlabel.set("SYNTAX ERROR")
        eq = ""
        pass    
        

def clear():
    global eq

    eq = ""
    eqlabel.set(eq)

calculatorwindow = Tk()
calculatorwindow.title("Calculator Program v1.0")
calculatorwindow.geometry("500x300")

eq = ""
eqlabel = StringVar()

label = Label(calculatorwindow, textvariable= eqlabel, font=("consolas",20),width=24)
label.pack()

buttonsframe = Frame(calculatorwindow)

b0 = Button(buttonsframe,text="0",command= lambda:button_press(0))
b1 = Button(buttonsframe,text="1",command= lambda:button_press(1))
b2 = Button(buttonsframe,text="2",command= lambda:button_press(2))
b3 = Button(buttonsframe,text="3",command= lambda:button_press(3))
b4 = Button(buttonsframe,text="4",command= lambda:button_press(4))
b5 = Button(buttonsframe,text="5",command= lambda:button_press(5))
b6 = Button(buttonsframe,text="6",command= lambda:button_press(6))
b7 = Button(buttonsframe,text="7",command= lambda:button_press(7))
b8 = Button(buttonsframe,text="8",command= lambda:button_press(8))
b9 = Button(buttonsframe,text="9",command= lambda:button_press(9))

bplus = Button(buttonsframe,text="+",command=lambda:button_press("+")) 
bmins = Button(buttonsframe,text="-",command=lambda:button_press("-"))
bdivi = Button(buttonsframe,text="/",command=lambda:button_press("/"))
bmult = Button(buttonsframe,text="*",command=lambda:button_press("*"))
bfact = Button(buttonsframe,text="NOT DONE")
bbase = Button(buttonsframe,text="NOT DONE") 
bsqrt = Button(buttonsframe,text="sqrt",command=lambda:button_press("sqrt("))
bequal= Button(buttonsframe,text="=",command=equals)
bdeci = Button(buttonsframe,text=".",command=lambda:button_press(","))
bclea = Button(buttonsframe,text="CE",command=lambda:clear())
bparo = Button(buttonsframe,text="(",command=lambda:button_press("("))
bparc = Button(buttonsframe,text=")",command=lambda:button_press(")"))

b0.grid(row=3,column=1)
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

bplus.grid(row=0,column=3)
bmins.grid(row=1,column=3)
bdivi.grid(row=2,column=3)
bmult.grid(row=3,column=3)
bfact.grid(row=0,column=4)
bbase.grid(row=1,column=4)
bsqrt.grid(row=2,column=4)
bequal.grid(row=3,column=4)
bdeci.grid(row=3,column=2)
bclea.grid(row=3,column=0)
bparo.grid(row=0,column=5)
bparc.grid(row=1,column=5)

buttonsframe.pack()
calculatorwindow.mainloop()