from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.title("Password Generator")
root.geometry("600x300")


# Creating function to generate passwords...
def new_pswd():
    # Clearing the entry box...
    pw_entry.delete(0, END)

    # Creating a variable to hold our...
    my_pswd = ""

    # Get pw length and convert into a integer...
    pw_length = int(my_entry.get())

    # Looping through the length...
    for x in range(pw_length):
        my_pswd += chr(randint(33, 126))

    #Output password to screen...
    pw_entry.insert(0,my_pswd)

def copy_pswd():
    # Clearing to clipboard...
    root.clipboard_clear()
    # Coping to clipboard...
    root.clipboard_append(pw_entry.get())
    # Displaing the message...
    messagebox.showinfo("info", "copied to clipboard")


# Creating a Label Frame....
lframe = LabelFrame(root, text="number of characters", font=("Helvetica", 12))
lframe.pack(pady=10)

# Creating an entry box to provide length of the password....
my_entry = Entry(lframe, font=("Helvetica", 24))
my_entry.pack(pady=10)

# Creating an entry box for returned password....
pw_entry = Entry(root, font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20, padx=20)

# Creating a frame for buttons....
bframe = Frame(root)
bframe.pack(pady=10)

# Creating buttons...
btn1 = Button(bframe, text="Generate Password", command = new_pswd)
btn1.grid(row = 0, column= 0, padx=20, pady=20)
btn2 = Button(bframe, text="Copy Password", command = copy_pswd)
btn2.grid(row = 0, column= 1, padx=20, pady=20)

root.mainloop()