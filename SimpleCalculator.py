from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    global curr
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first = e.get()
    global f
    global math
    math = "add"
    f = int(first)
    e.delete(0, END)

def button_sub():
    first = e.get()
    global f
    global math
    math = "sub"
    f = int(first)
    e.delete(0, END)

def button_mul():
    first = e.get()
    global f
    global math
    math = "mul"
    f = int(first)
    e.delete(0, END)

def button_div():
    first = e.get()
    global f
    global math
    math = "div"
    f = int(first)
    e.delete(0, END)
    #e.insert(0, str(f) + "+")

def button_equal():
    second = e.get()
    e.delete(0, END)
    if math == "add" : e.insert(0, f + int(second))
    elif math == "sub" : e.insert(0, f - int(second))
    elif math == "mul" : e.insert(0, f * int(second))
    elif math == "div" : e.insert(0, f / float(second))

def pressing(event):
    if event.char=="0" : button_click(0)
    elif event.char=="1" : button_click(1)
    elif event.char=="2" : button_click(2)
    elif event.char=="3" : button_click(3)
    elif event.char=="4" : button_click(4)
    elif event.char=="5" : button_click(5)
    elif event.char=="6" : button_click(6)
    elif event.char=="7" : button_click(7)
    elif event.char=="8" : button_click(8)
    elif event.char=="9" : button_click(9)
    elif event.char=="+" : button_add()
    elif event.char=="-" : button_sub()
    elif event.char=="/" : button_div()
    elif event.char=="*" : button_mul()
    elif event.char=="=" : button_equal()
    elif event.char == "c" : button_clear()
    elif event.char == "enter" : button_equal()
    elif len(curr)==0 : button_click(0)

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
btn1.grid(row=1, column=0)
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn2.grid(row=1, column=1)
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn3.grid(row=1, column=2)
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn6.grid(row=2, column=2)
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn7.grid(row=3, column=0)
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn8.grid(row=3, column=1)
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn9.grid(row=3, column=2)
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
btn0.grid(row=4, column=0)

plus = Button(root, text="+", padx=40, pady=20, command=button_add)
plus.grid(row=5, column=0)
clr = Button(root, text="clr", padx=79, pady=20, command=button_clear)
clr.grid(row=4, column=1, columnspan=2)
res = Button(root, text="=", padx=82, pady=20, command=button_equal)
res.grid(row=5, column=1, columnspan=3)
btn_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
btn_sub.grid(row=6, column=0)
btn_mul = Button(root, text="*", padx=40, pady=20, command=button_mul)
btn_mul.grid(row=6, column=1)
btn_div = Button(root, text="/", padx=40, pady=20, command=button_div)
btn_div.grid(row=6, column=2)


# Events

root.bind("<Key>", pressing)

root.mainloop()