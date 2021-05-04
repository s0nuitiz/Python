from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Othello")
root.geometry('360x380')

# Creating button frame...
btnfrm = Frame(root)
btnfrm.pack(pady=10)


def main():
    global bclick
    bclick = True

    # Creating white's suggetion function...
    def suggestion1():

        # At the begining of the game...
        if  (btn28['fg']=='white' and btn29['fg']=='black' and btn36['fg']=='black' and btn37['fg']=='white'):
            if  ((btn20['fg']!='black' and btn27['fg']!='black' and btn38['fg']!='black' and
                btn45['fg'] != 'black') and (btn20['fg']!='white' and btn27['fg']!='white'
                and btn38['fg']!='white' and btn45['fg'] != 'white')):
                btn20.config(text=U'\u26AB', fg='CadetBlue3')
                btn27.config(text=U'\u26AB',fg='CadetBlue3')
                btn38.config(text=U'\u26AB', fg='CadetBlue3')
                btn45.config(text=U'\u26AB', fg='CadetBlue3')

            elif(btn18['fg']=='black' and btn19['fg']=='black' and btn20['fg']=='black'):
                btn10.config(text=U'\u26AB', fg='CadetBlue3')
                btn12.config(text=U'\u26AB', fg='CadetBlue3')
                btn21.config(text=U'\u26AB', fg='CadetBlue3')
                btn30.config(text=U'\u26AB', fg='CadetBlue3')
                btn44.config(text=U'\u26AB', fg='CadetBlue3')
            #elif(btn18['fg']=='black' and btn19['fg']=='white' and btn20['fg']=='black'):

        # For black's possible 1st move....
        elif(btn27['fg']=='black' and btn28['fg']=='black' and btn29['fg']=='black' and
            btn36['fg']=='black'):
            if  (btn37['fg']=='white'):
                if  (btn19['fg']!='black' and btn19['fg']!='white' and btn21['fg']!='black'
                    and btn21['fg']!='white' and btn35['fg']!='black' and btn35['fg']!='white'):
                    btn19.config(text=U'\u26AB',fg='CadetBlue3')
                    btn21.config(text=U'\u26AB', fg='CadetBlue3')
                    btn35.config(text=U'\u26AB', fg='CadetBlue3')
                elif(btn1['fg']=='white' and btn2['fg']=='black' and btn10['fg']=='white' and
                btn18['fg']=='black' and btn19['fg']=='white' and btn20['fg']=='black'):
                    if  (btn3['fg']!='white' and btn3['fg']!='black' and btn17['fg']!='white' and
                        btn17['fg']!='black' and btn21['fg']!='white' and btn21['fg']!='black' and
                        btn26['fg']!='white' and btn26 ['fg']!='black' and btn35['fg']!='white' and
                        btn35['fg']!='black'):
                        btn3.config(text=U'\u26AB', fg='CadetBlue3')
                        btn17.config(text=U'\u26AB', fg='CadetBlue3')
                        btn21.config(text=U'\u26AB', fg='CadetBlue3')
                        btn26.config(text=U'\u26AB', fg='CadetBlue3')
                        btn35.config(text=U'\u26AB', fg='CadetBlue3')
                elif(btn1['fg'] == 'white' and btn2['fg'] == 'white' and btn3['fg'] == 'white' and
                    btn11['fg'] == 'black' and  btn18['fg'] == 'black' and btn19['fg'] == 'black'
                    and btn20['fg'] == 'black'):
                    if  (btn12['fg'] != 'white' and btn12['fg'] != 'black' and btn21['fg'] != 'white'
                        and btn21['fg'] != 'black' and btn26['fg'] != 'white' and btn26['fg'] != 'black'
                        and btn35['fg'] != 'white' and btn35['fg'] != 'black'):
                        if  (btn10['fg'] == 'white'):
                            btn12.config(text=U'\u26AB', fg='CadetBlue3')
                            btn21.config(text=U'\u26AB', fg='CadetBlue3')
                            btn26.config(text=U'\u26AB', fg='CadetBlue3')
                            btn35.config(text=U'\u26AB', fg='CadetBlue3')
                    elif(btn4['fg'] == 'white' and btn5['fg'] == 'white' and btn9['fg'] == 'black' and
                    btn10['fg'] == 'black' and  btn12['fg'] == 'black'):
                        btn17.config(text=U'\u26AB', fg='CadetBlue3')
                        btn21.config(text=U'\u26AB', fg='CadetBlue3')
                        btn25.config(text=U'\u26AB', fg='CadetBlue3')
                        btn26.config(text=U'\u26AB', fg='CadetBlue3')
                        btn35.config(text=U'\u26AB', fg='CadetBlue3')
                        btn38.config(text=U'\u26AB', fg='CadetBlue3')
                        btn44.config(text=U'\u26AB', fg='CadetBlue3')
                    elif(btn4['fg'] == 'black' and  btn12['fg'] == 'black'):
                        if  (btn5['fg'] != 'white' and btn5['fg'] != 'black' and btn13['fg'] != 'white' and
                            btn13['fg'] != 'black' and btn21['fg'] != 'white' and btn21['fg'] != 'black' and
                            btn26['fg'] != 'white' and btn26['fg'] != 'black'and btn35['fg'] != 'white' and
                            btn35['fg'] != 'black'):
                            btn5.config(text=U'\u26AB', fg='CadetBlue3')
                            btn13.config(text=U'\u26AB', fg='CadetBlue3')
                            btn21.config(text=U'\u26AB', fg='CadetBlue3')
                            btn26.config(text=U'\u26AB', fg='CadetBlue3')
                            btn35.config(text=U'\u26AB', fg='CadetBlue3')
            elif(btn37['fg']=='black'):
                if  (btn1['fg'] == 'white' and btn2['fg'] == 'white' and btn3['fg'] == 'white' and
                    btn4['fg'] == 'white' and btn5['fg'] == 'white' and btn9['fg'] == 'white' and
                    btn10['fg'] == 'white' and btn11['fg'] == 'black' and btn12['fg'] == 'black'
                    and  btn17['fg'] == 'white' and  btn18['fg'] == 'black' and btn19['fg'] == 'black'
                    and btn20['fg'] == 'black' and btn38['fg'] == 'black'):
                    btn13.config(text=U'\u26AB', fg='CadetBlue3')
                    btn21.config(text=U'\u26AB', fg='CadetBlue3')
                    btn25.config(text=U'\u26AB', fg='CadetBlue3')
                    btn26.config(text=U'\u26AB', fg='CadetBlue3')
                    btn35.config(text=U'\u26AB', fg='CadetBlue3')
                    btn44.config(text=U'\u26AB', fg='CadetBlue3')
                    btn45.config(text=U'\u26AB', fg='CadetBlue3')
                    btn46.config(text=U'\u26AB', fg='CadetBlue3')
                    btn47.config(text=U'\u26AB', fg='CadetBlue3')
        elif(btn20['fg']=='black' and btn28['fg']=='black' and btn29['fg']=='black' and
            btn36['fg']=='black' and btn37['fg']=='white'):
            if (btn19['fg']!='black' or
                btn21['fg']!='black' or btn35['fg']!='black' or btn19['fg']!='white' or
                btn21['fg']!='white' or btn35['fg']!='white'):
                btn19.config(text=U'\u26AB',fg='CadetBlue3')
                btn21.config(text=U'\u26AB', fg='CadetBlue3')
                btn35.config(text=U'\u26AB', fg='CadetBlue3')
        elif(btn28['fg']=='white' and btn29['fg']=='black' and
            btn36['fg']=='black' and btn37['fg']=='black' and btn38['fg']=='black'):
            if  (btn30['fg']!='white' and btn30['fg']!='black' and btn44['fg']!='white'
                and btn44['fg']!='black' and btn46['fg']!='white' and btn46['fg']!='black'):
                btn30.config(text=U'\u26AB',fg='CadetBlue3')
                btn44.config(text=U'\u26AB', fg='CadetBlue3')
                btn46.config(text=U'\u26AB', fg='CadetBlue3')

        #elif():

    # Creating black's suggetion function...
    def suggestion2():
        if  (btn28['fg'] == 'white' and btn29['fg'] == 'black' and btn36['fg'] == 'black' and btn37['fg'] == 'white'):
            if (btn1['fg'] == 'white' and btn2['fg'] == 'black' and btn10['fg'] == 'white' and btn18['fg'] == 'black' and
                 btn19['fg'] == 'white' and btn20['fg'] == 'black'):
                if  (btn27['fg'] != 'white' and btn27['fg'] != 'black' and btn38['fg'] != 'white' and btn38['fg'] != 'black'
                    and btn45['fg'] != 'white' and btn45['fg'] != 'black'):
                    btn27.config(text=U'\u26AB', fg='CadetBlue3')
                    btn38.config(text=U'\u26AB', fg='CadetBlue3')
                    btn45.config(text=U'\u26AB', fg='CadetBlue3')
            elif(btn2['fg'] == 'black' and btn10['fg'] == 'black' and btn18['fg'] == 'black' and
                 btn19['fg'] == 'white' and btn20['fg'] == 'black'):
                if  (btn1['fg'] != 'white' and btn1['fg'] != 'black' and btn17['fg'] != 'white'
                    and btn17['fg'] != 'black' and btn21['fg'] != 'white' and btn21['fg'] != 'black'
                    and btn30['fg'] != 'white' and btn30['fg'] != 'black' and btn35['fg'] != 'white'
                    and btn35['fg'] != 'black' and btn12['fg'] != 'white' and btn12['fg'] != 'black'
                    and btn44['fg'] != 'white' and btn44['fg'] != 'black'):
                    btn1.config(text=U'\u26AB', fg='CadetBlue3')
                    btn17.config(text=U'\u26AB', fg='CadetBlue3')
                    btn21.config(text=U'\u26AB', fg='CadetBlue3')
                    btn30.config(text=U'\u26AB', fg='CadetBlue3')
                    btn35.config(text=U'\u26AB', fg='CadetBlue3')
                    btn12.config(text=U'\u26AB', fg='CadetBlue3')
                    btn44.config(text=U'\u26AB', fg='CadetBlue3')
            elif(btn10['fg'] == 'white' and btn18['fg'] == 'black' and btn19['fg'] == 'white' and btn20['fg'] == 'black'):
                if  (btn2['fg'] != 'white' and btn2['fg'] != 'black' and btn27['fg'] != 'white'
                    and btn27['fg'] != 'black' and btn38['fg'] != 'white' and btn38['fg'] != 'black'
                    and btn45['fg'] != 'white' and btn45['fg'] != 'black'):
                    btn2.config(text=U'\u26AB', fg='CadetBlue3')
                    btn27.config(text=U'\u26AB', fg='CadetBlue3')
                    btn38.config(text=U'\u26AB', fg='CadetBlue3')
                    btn45.config(text=U'\u26AB', fg='CadetBlue3')
            elif(btn19['fg'] == 'white' and btn20['fg'] == 'black'):
                if  (btn18['fg'] != 'white' and btn18['fg'] != 'black' and btn27['fg'] != 'white'
                    and btn27['fg'] != 'black' and btn38['fg'] != 'white' and btn38['fg'] != 'black'
                    and btn45['fg'] != 'white' and btn45['fg'] != 'black' ):
                    btn18.config(text=U'\u26AB', fg='CadetBlue3')
                    btn27.config(text=U'\u26AB', fg='CadetBlue3')
                    btn38.config(text=U'\u26AB', fg='CadetBlue3')
                    btn45.config(text=U'\u26AB', fg='CadetBlue3')
        elif(btn28['fg'] == 'black' and btn29['fg'] == 'black' and btn36['fg'] == 'black'):
            if  (btn37['fg'] == 'white'):
                if  (btn1['fg'] == 'white' and btn2['fg'] == 'white' and btn3['fg'] == 'white' and
                    btn10['fg'] == 'white' and btn11['fg'] == 'black' and  btn18['fg'] == 'black'
                    and btn19['fg'] == 'black'and btn20['fg'] == 'black' and btn27['fg'] == 'black'):
                    if  (btn4['fg'] == 'white' and btn5['fg'] == 'white' and btn12['fg'] == 'black'):
                        if  (btn9['fg'] != 'white' and btn9['fg'] != 'black' and btn38['fg'] != 'white'
                            and btn38['fg'] != 'black' and btn45['fg'] != 'white' and btn45['fg'] != 'black'
                            and btn46['fg'] != 'white' and btn46['fg'] != 'black'):
                            btn9.config(text=U'\u26AB', fg='CadetBlue3')
                            btn38.config(text=U'\u26AB', fg='CadetBlue3')
                            btn45.config(text=U'\u26AB', fg='CadetBlue3')
                            btn46.config(text=U'\u26AB', fg='CadetBlue3')
                        elif(btn9['fg'] == 'white' and btn17['fg'] == 'white'):
                            btn38.config(text=U'\u26AB', fg='CadetBlue3')
                            btn45.config(text=U'\u26AB', fg='CadetBlue3')
                            btn46.config(text=U'\u26AB', fg='CadetBlue3')
                elif(btn1['fg'] == 'white' and btn2['fg'] == 'white' and btn3['fg'] == 'white' and
                    btn10['fg'] == 'white'):
                    if (btn18['fg'] == 'black' and btn19['fg'] == 'white'
                        and btn20['fg'] == 'black' and btn27['fg'] == 'black'):
                        if  (btn11['fg'] != 'white' and btn11['fg'] != 'black' and btn38['fg'] != 'white'
                            and btn38['fg'] != 'black' and btn45['fg'] != 'white' and btn45['fg'] != 'black'
                            and btn46['fg'] != 'white' and btn46['fg'] != 'black'):
                            btn11.config(text=U'\u26AB', fg='CadetBlue3')
                            btn38.config(text=U'\u26AB', fg='CadetBlue3')
                            btn45.config(text=U'\u26AB', fg='CadetBlue3')
                            btn46.config(text=U'\u26AB', fg='CadetBlue3')
                    elif(btn11['fg'] == 'white' and btn12['fg'] == 'white' and btn18['fg'] == 'black' and
                        btn19['fg'] == 'black' and btn20['fg'] == 'black' and btn27['fg'] == 'black'):
                        if  (btn4['fg'] != 'white' and btn4['fg'] != 'black' and btn38['fg'] != 'white'
                            and btn38['fg'] != 'black' and btn45['fg'] != 'white' and btn45['fg'] != 'black'
                            and btn46['fg'] != 'white' and btn46['fg'] != 'black'):
                            btn4.config(text=U'\u26AB', fg='CadetBlue3')
                            btn38.config(text=U'\u26AB', fg='CadetBlue3')
                            btn45.config(text=U'\u26AB', fg='CadetBlue3')
                            btn46.config(text=U'\u26AB', fg='CadetBlue3')
            elif(btn37['fg'] == 'black'):
                if  (btn1['fg'] == 'white' and btn2['fg'] == 'white' and btn3['fg'] == 'white' and
                    btn4['fg'] == 'white' and btn5['fg'] == 'white' and btn9['fg'] == 'white' and
                    btn10['fg'] == 'white' and btn11['fg'] == 'white' and btn12['fg'] == 'white'
                    and  btn13['fg'] == 'white' and btn17['fg'] == 'white' and btn18['fg'] == 'black'
                    and btn19['fg'] == 'black' and btn20['fg'] == 'black'
                    and btn27['fg'] == 'black' and btn38['fg'] == 'black'):
                    btn6.config(text=U'\u26AB', fg='CadetBlue3')

    # Defining black's ruls..
    def rule1():
        # Omitting suggestion/suggestions and putting the right color/colors...
        if (btn38['fg'] == 'black'):
            if(btn20['fg'] != 'white' and btn20['fg'] != 'black' and btn27['fg'] != 'white'
                and btn27['fg'] != 'black'):
                btn20.config(text="")
                btn27.config(text="")
            btn37.config(text=U'\u26AB', fg="black")
            btn45.config(text="")
            btn46.config(text="")
        elif(btn4['fg'] == 'black'):
            btn11.config(text=U'\u26AB', fg="black")
            btn12.config(text=U'\u26AB', fg="black")
            btn38.config(text="")
            btn45.config(text="")
            btn46.config(text="")
        elif(btn9['fg'] == 'black'):
            btn10.config(text=U'\u26AB', fg="black")
            btn38.config(text="")
            btn45.config(text="")
            btn46.config(text="")
        elif(btn11['fg'] == 'black'):
            btn19.config(text=U'\u26AB', fg="black")
            btn38.config(text="")
            btn45.config(text="")
            btn46.config(text="")
        elif(btn27['fg'] == 'black'):
            btn28.config(text=U'\u26AB', fg="black")
            btn38.config(text="")
            btn45.config(text="")
            if(btn20['fg'] != 'black' and btn20['fg'] != 'white'):
                btn20.config(text="")
        elif (btn2['fg'] == 'black'):
            btn10.config(text=U'\u26AB', fg="black")
            btn27.config(text="")
            btn38.config(text="")
            btn45.config(text="")
        elif(btn18['fg'] == 'black'):
            btn19.config(text=U'\u26AB', fg="black")
            btn27.config(text="")
            btn38.config(text="")
            btn45.config(text="")
        elif(btn20['fg'] == 'black'):
            btn27.config(text="")
            btn38.config(text="")
            btn45.config(text="")
            btn28.config(text=U'\u26AB', fg="black")
        elif (btn45['fg'] == 'black'):
            btn27.config(text="")
            btn38.config(text="")
            btn20.config(text="")
            btn37.config(text=U'\u26AB', fg="black")

    # Defining white's ruls..
    def rule2():
        # Omitting suggestion/suggestions and putting the right color/colors...
        if  (btn13['fg'] == 'white'):
            btn11.config(text=U'\u26AB', fg='white')
            btn12.config(text=U'\u26AB', fg='white')
            btn21.config(text="")
            btn25.config(text="")
            btn26.config(text="")
            btn35.config(text="")
            btn44.config(text="")
            btn45.config(text="")
            btn46.config(text="")
            btn47.config(text="")
        elif(btn17['fg'] == 'white'):
            btn9.config(text=U'\u26AB', fg='white')
            btn10.config(text=U'\u26AB', fg='white')
            btn21.config(text="")
            btn25.config(text="")
            btn26.config(text="")
            btn35.config(text="")
            btn38.config(text="")
            btn44.config(text="")
        elif (btn5['fg'] == 'white'):
            btn4.config(fg="white")
            btn13.config(text="")
            btn21.config(text="")
            btn26.config(text="")
            btn35.config(text="")
        elif(btn12['fg'] == 'white'):
            btn11.config(text=U'\u26AB', fg='white')
            btn21.config(text="")
            btn26.config(text="")
            btn35.config(text="")
        elif (btn3['fg'] == 'white'):
            btn2.config(text=U'\u26AB', fg='white')
            btn17.config(text="")
            btn21.config(text="")
            btn26.config(text="")
            btn35.config(text="")
        elif(btn1['fg'] == 'white'):
            btn10.config(text=U'\u26AB', fg='white')
            btn17.config(text="")
            btn21.config(text="")
            btn30.config(text="")
            btn35.config(text="")
            btn12.config(text="")
            btn44.config(text="")
        elif(btn10['fg'] == 'white'):
            btn12.config(text="")
            btn19.config(text=U'\u26AB', fg='white')
            btn21.config(text="")
            btn30.config(text="")
            btn44.config(text="")
        elif(btn19['fg'] == 'white'):
            btn21.config(text="")
            btn28.config(text=U'\u26AB', fg="white")
            btn35.config(text="")
        elif(btn21['fg'] == 'white'):
            btn19.config(text="")
            btn29.config(text=U'\u26AB', fg="white")
            btn35.config(text="")
        elif(btn35['fg'] == 'white'):
            btn19.config(text="")
            btn21.config(text="")
            btn36.config(text=U'\u26AB', fg="white")
        elif(btn46['fg'] == 'white'):
            btn30.config(text="")
            btn44.config(text="")
            btn37.config(text=U'\u26AB', fg="white")
        '''
        elif (btn45['fg'] == 'black'):
            btn27.config(text="")
            btn38.config(text="")
            btn20.config(text="")
            btn37.config(fg="black")
        elif (btn20['fg'] == 'black'):
            btn27.config(text="")
            btn38.config(text="")
            btn45.config(text="")
            btn28.config(fg="black")
        elif (btn38['fg'] == 'black'):
            btn20.config(text="")
            btn27.config(text="")
            btn45.config(text="")
            btn37.config(fg="black")
        '''

    def btnclick(buttons):
        global bclick
        if buttons['text'] == U'\u26AB' and buttons['fg'] == 'CadetBlue3' and bclick == True:
            buttons.config( fg='black')
            bclick = False
            rule1()

        elif buttons['text'] == U'\u26AB' and buttons['fg'] == 'CadetBlue3' and bclick == False:
            buttons.config( text=U'\u26AB', fg='white')
            bclick = True
            rule2()

        suggestion1()
        suggestion2()

    # Creating 64 boxes...
    btn1 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn1))
    btn1.grid(row=1,column=1)
    btn2 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn2))
    btn2.grid(row=1, column=2)
    btn3 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn3))
    btn3.grid(row=1, column=3)
    btn4 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn4))
    btn4.grid(row=1,column=4)
    btn5 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn5))
    btn5.grid(row=1,column=5)
    btn6 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn6))
    btn6.grid(row=1,column=6)
    btn7 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn7))
    btn7.grid(row=1,column=7)
    btn8 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn8))
    btn8.grid(row=1,column=8)

    btn9 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn9))
    btn9.grid(row=2,column=1)
    btn10 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn10))
    btn10.grid(row=2,column=2)
    btn11 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn11))
    btn11.grid(row=2,column=3)
    btn12 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn12))
    btn12.grid(row=2,column=4)
    btn13 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn13))
    btn13.grid(row=2,column=5)
    btn14 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn14))
    btn14.grid(row=2,column=6)
    btn15 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn15))
    btn15.grid(row=2,column=7)
    btn16 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn16))
    btn16.grid(row=2,column=8)

    btn17 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn17))
    btn17.grid(row=3,column=1)
    btn18 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn18))
    btn18.grid(row=3,column=2)
    btn19 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn19))
    btn19.grid(row=3,column=3)
    btn20 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn20))
    btn20.grid(row=3,column=4)
    btn21 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn21))
    btn21.grid(row=3,column=5)
    btn22 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn22))
    btn22.grid(row=3,column=6)
    btn23 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn23))
    btn23.grid(row=3,column=7)
    btn24 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn24))
    btn24.grid(row=3,column=8)

    btn25 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn25))
    btn25.grid(row=4,column=1)
    btn26 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn26))
    btn26.grid(row=4,column=2)
    btn27 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn27))
    btn27.grid(row=4,column=3)
    btn28 = Button(btnfrm, text=U'\u26AB',fg='white', height=2, width=5, bg="DeepSkyBlue4")
    btn28.grid(row=4,column=4)
    btn29 = Button(btnfrm, text=U'\u26AB',fg='black', height=2, width=5, bg="DeepSkyBlue2")
    btn29.grid(row=4,column=5)
    btn30 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn30))
    btn30.grid(row=4,column=6)
    btn31 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn31))
    btn31.grid(row=4,column=7)
    btn32 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn32))
    btn32.grid(row=4,column=8)

    btn33 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn33))
    btn33.grid(row=5,column=1)
    btn34 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn34))
    btn34.grid(row=5,column=2)
    btn35 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn35))
    btn35.grid(row=5,column=3)
    btn36 = Button(btnfrm, text=U'\u26AB',fg='black', height=2, width=5, bg="DeepSkyBlue2")
    btn36.grid(row=5,column=4)
    btn37 = Button(btnfrm, text=U'\u26AB',fg='white', height=2, width=5, bg="DeepSkyBlue4")
    btn37.grid(row=5,column=5)
    btn38 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn38))
    btn38.grid(row=5,column=6)
    btn39 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn39))
    btn39.grid(row=5,column=7)
    btn40 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn40))
    btn40.grid(row=5,column=8)

    btn41 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn41))
    btn41.grid(row=6,column=1)
    btn42 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn42))
    btn42.grid(row=6,column=2)
    btn43 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn43))
    btn43.grid(row=6,column=3)
    btn44 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn44))
    btn44.grid(row=6,column=4)
    btn45 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn45))
    btn45.grid(row=6,column=5)
    btn46 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn46))
    btn46.grid(row=6,column=6)
    btn47 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn47))
    btn47.grid(row=6,column=7)
    btn48 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn48))
    btn48.grid(row=6,column=8)

    btn49 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn49))
    btn49.grid(row=7,column=1)
    btn50 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn50))
    btn50.grid(row=7,column=2)
    btn51 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn51))
    btn51.grid(row=7,column=3)
    btn52 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn52))
    btn52.grid(row=7,column=4)
    btn53 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn53))
    btn53.grid(row=7,column=5)
    btn54 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn54))
    btn54.grid(row=7,column=6)
    btn55 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn55))
    btn55.grid(row=7,column=7)
    btn56 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn56))
    btn56.grid(row=7,column=8)

    btn57 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn57))
    btn57.grid(row=8,column=1)
    btn58 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn58))
    btn58.grid(row=8,column=2)
    btn59 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn59))
    btn59.grid(row=8,column=3)
    btn60 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn60))
    btn60.grid(row=8,column=4)
    btn61 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn61))
    btn61.grid(row=8,column=5)
    btn62 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn62))
    btn62.grid(row=8,column=6)
    btn63 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue2", command=lambda :btnclick(btn63))
    btn63.grid(row=8,column=7)
    btn64 = Button(btnfrm, text='', height=2, width=5, bg="DeepSkyBlue4", command=lambda :btnclick(btn64))
    btn64.grid(row=8,column=8)

    suggestion1()
    suggestion2()

    root.mainloop()
main()