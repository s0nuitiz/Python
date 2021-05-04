from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Menu")
root.geometry("600x600")

# Creating states Function..
def states():
    hide_frames()
    states_frame.pack(fill="both", expand=1)
    my_label = Label(states_frame, text="States").pack()

# Creating state_cap Function..
def state_cap():
    hide_frames()
    state_cap_frame.pack(fill="both", expand=1)
    my_label = Label(state_cap_frame, text="Capitals").pack()

# Hiding previous frames...
def hide_frames():
    for widget in states_frame.winfo_children():
        widget.destroy()

    for widget in state_cap_frame.winfo_children():
        widget.destroy()

    states_frame.pack_forget()
    state_cap_frame.pack_forget()

# Creating Our Menu...
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating Menu Items..
cas_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=cas_menu)

# Creating Sub Items...
cas_menu.add_command(label="States", command=states)
cas_menu.add_command(label="State_Capitals", command=state_cap)
cas_menu.add_separator()
cas_menu.add_command(label="Exit", command=root.quit)

# Adding Frames....
states_frame = Frame(root, width=600, height=600)
state_cap_frame = Frame(root, width=600, height=600)

root.mainloop()