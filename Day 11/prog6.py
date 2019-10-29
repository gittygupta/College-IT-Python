from Tkinter import *
  
expression = "" 

def click(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
  
def equal(): 
    try: 
        global expression 
        total = str(eval(expression))
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

if __name__ == "__main__": 
    gui = Tk() 
    gui.configure(background="light grey") 
    gui.title("Simple Calculator")
    gui.geometry("305x125")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=60) 
    equation.set('enter your expression') 
    b1 = Button(gui, text=' 1 ', fg='black', bg='grey', command=lambda: click(1), height=1, width=6) 
    b1.grid(row=2, column=0) 
  
    b2 = Button(gui, text=' 2 ', fg='black', bg='grey', command=lambda: click(2), height=1, width=6) 
    b2.grid(row=2, column=1) 
  
    b3 = Button(gui, text=' 3 ', fg='black', bg='grey', command=lambda: click(3), height=1, width=6) 
    b3.grid(row=2, column=2) 
  
    b4 = Button(gui, text=' 4 ', fg='black', bg='grey', command=lambda: click(4), height=1, width=6) 
    b4.grid(row=3, column=0) 
  
    b5 = Button(gui, text=' 5 ', fg='black', bg='grey', command=lambda: click(5), height=1, width=6) 
    b5.grid(row=3, column=1) 
  
    b6 = Button(gui, text=' 6 ', fg='black', bg='grey', command=lambda: click(6), height=1, width=6) 
    b6.grid(row=3, column=2) 
  
    b7 = Button(gui, text=' 7 ', fg='black', bg='grey', command=lambda: click(7), height=1, width=6) 
    b7.grid(row=4, column=0) 
  
    b8 = Button(gui, text=' 8 ', fg='black', bg='grey', command=lambda: click(8), height=1, width=6) 
    b8.grid(row=4, column=1) 
  
    b9 = Button(gui, text=' 9 ', fg='black', bg='grey', command=lambda: click(9), height=1, width=6) 
    b9.grid(row=4, column=2) 
  
    b0 = Button(gui, text=' 0 ', fg='black', bg='grey', command=lambda: click(0), height=1, width=6) 
    b0.grid(row=5, column=0) 
  
    add = Button(gui, text=' + ', fg='black', bg='grey', command=lambda: click("+"), height=1, width=6) 
    add.grid(row=2, column=3) 
  
    sub = Button(gui, text=' - ', fg='black', bg='grey', command=lambda: click("-"), height=1, width=6) 
    sub.grid(row=3, column=3) 
  
    mul = Button(gui, text=' * ', fg='black', bg='grey', command=lambda: click("*"), height=1, width=6) 
    mul.grid(row=4, column=3) 
  
    div = Button(gui, text=' / ', fg='black', bg='grey', command=lambda: click("/"), height=1, width=6) 
    div.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='grey', command=equal, height=1, width=6) 
    equal.grid(row=5, column=2) 
  
    clr = Button(gui, text='Clear', fg='black', bg='grey', command=clear, height=1, width=6) 
    clr.grid(row=5, column='1') 

 
    gui.mainloop() 
