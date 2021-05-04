from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")

frame = LabelFrame(root)
frame.pack(padx=10, pady=0)

my_img1 = ImageTk.PhotoImage(Image.open("img/2.png"))
my_img2 = ImageTk.PhotoImage(Image.open("img/3.png"))
my_img3 = ImageTk.PhotoImage(Image.open("img/4.png"))
my_img4 = ImageTk.PhotoImage(Image.open("img/5.png"))
my_img5 = ImageTk.PhotoImage(Image.open("img/6.png"))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(frame, text="image 1 of " + str(len(img_list)), relief=FLAT, anchor=W)
status.grid(row=0, column=0, columnspan=3, sticky=W+E, pady=5)

my_label = Label(frame, image = my_img1)
my_label.grid(row=1, column=1)

def forward(img_num):
    global my_label
    global btn3
    global btn1

    my_label.grid_forget()
    my_label = Label(frame, image = img_list[img_num-1])
    btn3 = Button(frame, text=">>", command=lambda: forward(img_num+1), relief=FLAT)
    btn1 = Button(frame, text ="<<", command=lambda: back(img_num-1), relief=FLAT)

    if img_num == 5:
        btn3 = Button(frame, text=">>", state=DISABLED, relief=FLAT)

    my_label.grid(row=1, column=1)
    btn3.grid(row=1, column=2, sticky=N+S)
    btn1.grid(row=1, column=0, sticky=N+S)
    status = Label(frame, text="image " + str(img_num) + " of " + str(len(img_list)), relief=FLAT, anchor=W)
    status.grid(row=0, column=0, columnspan=3, sticky=W + E, pady=5)

def back(img_num):
    global my_label
    global btn3
    global btn1

    my_label.grid_forget()
    my_label = Label(frame, image = img_list[img_num-1])
    btn3 = Button(frame, text=">>", command=lambda: forward(img_num+1), relief=FLAT)
    btn1 = Button(frame, text ="<<", command=lambda: back(img_num-1), relief=FLAT)

    if img_num == 1:
        btn1 = Button(frame, text="<<", state=DISABLED, relief=FLAT)

    my_label.grid(row=1, column=1)
    btn3.grid(row=1, column=2, sticky=N+S)
    btn1.grid(row=1, column=0, sticky=N+S)
    status = Label(frame, text="image " + str(img_num) + " of " + str(len(img_list)), relief=FLAT, anchor=W)
    status.grid(row=0, column=0, columnspan=3, sticky=W + E, pady=10)

btn1 = Button(frame, text = "<<", command=lambda: back(), state=DISABLED, relief=FLAT)
btn1.grid(row=1, column=0, sticky=N+S)
btn2 = Button(frame, text = 'Exit', command = root.quit, anchor=E)
btn2.grid(row=2, column=0, columnspan=3, sticky=W+E)
btn3 = Button(frame, text = ">>", command=lambda: forward(2), relief=FLAT)
btn3.grid(row=1, column=2, sticky=N+S)


root.mainloop()