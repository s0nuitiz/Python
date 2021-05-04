from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')
root.geometry('272x380')

# Creating the Entry Boxes...
my_entry1 = Entry(root, text="")
my_entry1.grid(row=1, column=2, columnspan=4, pady=10, padx=7)

my_entry2 = Entry(root, text="")
my_entry2.grid(row=2, column=2, columnspan=4, pady=10, padx=7)

def main():
    global bclick
    bclick = True
    # Creating button disable function
    def btndisable():
        btn1.config(state='disable')
        btn2.config(state='disable')
        btn3.config(state='disable')
        btn4.config(state='disable')
        btn5.config(state='disable')
        btn6.config(state='disable')
        btn7.config(state='disable')
        btn8.config(state='disable')
        btn9.config(state='disable')

    # Creating function for checking winner....
    def checkforwin():
        if (btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
            btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
            btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
            btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
            btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X' or
            btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
            btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
            btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X'):
            btndisable()
            messagebox.showinfo("Tic-Tac-Toe", p1)

        elif (btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
            btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
            btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
            btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or
            btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O' or
            btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
            btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O' or
            btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O'):
            btndisable()
            messagebox.showinfo("Tic-Tac-Toe", p2)

        elif ((btn1['text']=='O' or btn1['text']=='X') and
              (btn2['text']=='O' or btn2['text']=='X') and
              (btn3['text']=='O' or btn3['text']=='X') and
              (btn4['text']=='O' or btn4['text']=='X') and
              (btn5['text']=='O' or btn5['text']=='X') and
              (btn6['text']=='O' or btn6['text']=='X') and
              (btn7['text']=='O' or btn7['text']=='X') and
              (btn8['text']=='O' or btn8['text']=='X') and
              (btn9['text']=='O' or btn9['text']=='X')):
            btndisable()
            messagebox.showinfo("Tic-Tac-Toe", "The match is draw!")

    def btnclick(buttons):
        global bclick, p1, p2
        if buttons['text'] == "" and bclick == True:
            buttons['text'] = "X"
            bclick = False
            p1 = my_entry1.get()+" wins!"
            checkforwin()
        elif buttons['text'] == "" and bclick == False:
            buttons['text'] = "O"
            bclick = True
            p2 = my_entry2.get()+" wins!"
            checkforwin()
        else:
            messagebox.showinfo("Tic-Tac-Toe", "Button is already clicked.")

    # Creating the Labels...
    my_lable1 = Label(root, text="Player 1", font=('Helvetica'), foreground = 'red')
    my_lable1.grid(row=1, column=1, pady=10, padx=7)
    my_lable2 = Label(root, text="Player 2", font=('Helvetica'), fg = 'green')
    my_lable2.grid(row=2, column=1, pady=10, padx=7)

    # Creating the boxes...
    #buttons = StringVar()
    btn1 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn1))
    btn1.grid(row=3, column=1)
    btn2 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn2))
    btn2.grid(row=3, column=2)
    btn3 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn3))
    btn3.grid(row=3, column=3)
    btn4 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn4))
    btn4.grid(row=4, column=1)
    btn5 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn5))
    btn5.grid(row=4, column=2)
    btn6 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn6))
    btn6.grid(row=4, column=3)
    btn7 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn7))
    btn7.grid(row=5, column=1)
    btn8 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn8))
    btn8.grid(row=5, column=2)
    btn9 = Button(root, text="", font='Times 20 bold', bg='grey', fg='white', height=2, width=5, command=lambda :btnclick(btn9))
    btn9.grid(row=5, column=3)

    btn10 = Button(root, text="Refresh", command=main)
    btn10.grid(row=6, column=2, pady=5)
    root.mainloop()

main()