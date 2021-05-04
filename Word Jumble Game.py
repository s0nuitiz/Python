from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox

root = Tk()
root.title("")
root.geometry("600x300")

my_lbl = Label(root, text="", font=("Helvetica", 42))
my_lbl.pack(pady=20)

def shuffler():
    # Clearing Entry box...
    enter_ans.delete(0, END)

    # Clearing the Answer label...
    ans_lbl.config(text="")

    # Creating  a list of states....
    states =["WEST BENGAL", "BIHAR", "NEPAL", "BHUTAN", "MADHYAPRADESH", "UTTARPRADESH", "JANMU", "KASHMIR", "KARNATAKA"]

    # Choosing an item from the list...
    global word
    word = choice(states)

    # Breaking the chosen word and making a list of its letters...
    breaking_word = list(word)

    # Shuffling the letters of the chosen word....
    shuffle(breaking_word)

    # Gathering the shuffled letters together as a whole word...
    global shuffled_word
    shuffled_word = ""
    for letters in breaking_word:
        shuffled_word += letters

    # Putting the shuffled word on screen...
    my_lbl.config(text=shuffled_word)

def answer():
    if word==enter_ans.get().upper():
        ans_lbl.config(text="Correct!", font=("Helvetica", 12))
    elif len(enter_ans.get())==0:
        messagebox.showwarning("warning", "Please enter something.")
    else:
        ans_lbl.config(text="Incorrect!", font=("Helvetica", 12))


# Creating entry box..
v=StringVar()
enter_ans = Entry(root, text="")
enter_ans.pack()

frame = Frame(root)
frame.pack()

# Creating buttons..
my_btn = Button(frame, text="Pick Another Word", command=shuffler)
my_btn.grid(row = 0, column= 0, padx=10, pady=20)
ans_btn = Button(frame, text="Answer", command=answer)
ans_btn.grid(row = 0, column= 1, padx=10, pady=20)

# Creating Answer label...
ans_lbl = Label(root, text="")
ans_lbl.pack()


shuffler()

root.mainloop()