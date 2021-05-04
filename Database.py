from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Database")
root.geometry("600x600")

try:
    # Create a Database or Connect to One
    conn = sqlite3.connect('address_book.db')

    # Create Cursor
    c = conn.cursor()

    # Create Table
    '''
    c.execute("""CREATE TABLE addresses (
              first_name text,
              last_name text,
              address text,
              city text,
              state text,
              zipcode integer
              )""")
    '''


    # Create a update function to save the edited record
    def update():
        r = messagebox.askokcancel("Save the changes ?")
        # global r
        if (r == 1):
            # Create a Database or Connect to One
            conn = sqlite3.connect('address_book.db')

            # Create Cursor
            c = conn.cursor()

            record_id = delete_box.get()
            c.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
    
                WHERE oid = :oid""",
                      {
                          'first': f_name_editor.get(),
                          'last': l_name_editor.get(),
                          'address': add_editor.get(),
                          'city': city_editor.get(),
                          'state': state_editor.get(),
                          'zipcode': zipcode_editor.get(),

                          'oid': record_id
                      })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()


    # Create Edit Function to Edit a Record
    def edit():
        if (delete_box.get() == ""):
            messagebox.showwarning("warning", "Please enter an id number.")
        else:
            editor = Tk()
            editor.title("Update a Record")
            editor.geometry("600x600")

            # Create a Database or Connect to One
            conn = sqlite3.connect('address_book.db')

            # Create Cursor
            c = conn.cursor()

            record_id = delete_box.get()
            # Query the database
            c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
            records = c.fetchall()

            # Create Global Variable for text box names
            global f_name_editor
            global l_name_editor
            global add_editor
            global city_editor
            global state_editor
            global zipcode_editor

            # Create Text Boxes
            f_name_editor = Entry(editor, width=30)
            f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
            l_name_editor = Entry(editor, width=30)
            l_name_editor.grid(row=1, column=1, padx=20)
            add_editor = Entry(editor, width=30)
            add_editor.grid(row=2, column=1, padx=20)
            city_editor = Entry(editor, width=30)
            city_editor.grid(row=3, column=1, padx=20)
            state_editor = Entry(editor, width=30)
            state_editor.grid(row=4, column=1, padx=20)
            zipcode_editor = Entry(editor, width=30)
            zipcode_editor.grid(row=5, column=1, padx=20)

            # Create Text Box Label
            f_name_label = Label(editor, text="First Name")
            f_name_label.grid(row=0, column=0, pady=(10, 0))
            l_name_label = Label(editor, text="Last Name")
            l_name_label.grid(row=1, column=0)
            add_label = Label(editor, text="Address")
            add_label.grid(row=2, column=0)
            city_label = Label(editor, text="City")
            city_label.grid(row=3, column=0)
            state_label = Label(editor, text="State")
            state_label.grid(row=4, column=0)
            zipcode_label = Label(editor, text="Zip Code")
            zipcode_label.grid(row=5, column=0)

            # Loop through Results
            for record in records:
                f_name_editor.insert(0, record[0])
                l_name_editor.insert(0, record[1])
                add_editor.insert(0, record[2])
                city_editor.insert(0, record[3])
                state_editor.insert(0, record[4])
                zipcode_editor.insert(0, record[5])

            # Create a Save Button
            save_btn = Button(editor, text="Save Record", command=update)
            save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

            # Deleting the ID number..
            delete_box.delete(0, END)


    # Create Function to Delete a Record
    def delete():
        if (delete_box.get() == ""):
            messagebox.showwarning("warning", "Please enter an id number.")
        else:
            response = messagebox.askquestion("Query", "Are you sure you want to delete it ?")
            if (response == "yes"):
                # Create a Database or Connect to One
                conn = sqlite3.connect('address_book.db')

                # Create Cursor
                c = conn.cursor()

                # Delete a Rocord
                c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

                # Commit Changes
                conn.commit()

                # Close Connection
                conn.close()

                # Deleting the ID number..
                delete_box.delete(0, END)


    # Create Function submit
    def submit():
        if ((f_name.get() == "") or (l_name.get() == "") or (add.get() == "") or (city.get() == "") or (
                state.get() == "") or (zipcode.get() == "")):
            messagebox.showwarning("warning", "Please Fill all Fields")
        elif ((f_name.get() == " ") or (l_name.get() == " ") or (add.get() == " ") or (city.get() == " ") or (
                state.get() == " ") or (zipcode.get() == " ")):
            messagebox.showwarning("warning", "Spaces are not allowed.")
        else:
            # Create a Database or Connect to One
            conn = sqlite3.connect('address_book.db')

            # Create Cursor
            c = conn.cursor()

            # Insert Into Table
            c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip)",
                      {
                          'f_name': f_name.get(),
                          'l_name': l_name.get(),
                          'address': add.get(),
                          'city': city.get(),
                          'state': state.get(),
                          'zip': zipcode.get()
                      })

            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()

            # clear The Text Boxes
            f_name.delete(0, END)
            l_name.delete(0, END)
            add.delete(0, END)
            city.delete(0, END)
            state.delete(0, END)
            zipcode.delete(0, END)


    # Create Query Function
    def query():
        # Create a Database or Connect to One
        conn = sqlite3.connect('address_book.db')

        # Create Cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM addresses")
        records = c.fetchall()

        # Loop through Results
        print_records = ""
        for record in records:
            print_records += str(record) + "\n"

        q_lbl = Label(root, text=print_records)
        q_lbl.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()


    # Create Text Boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1, padx=20)
    add = Entry(root, width=30)
    add.grid(row=2, column=1, padx=20)
    city = Entry(root, width=30)
    city.grid(row=3, column=1, padx=20)
    state = Entry(root, width=30)
    state.grid(row=4, column=1, padx=20)
    zipcode = Entry(root, width=30)
    zipcode.grid(row=5, column=1, padx=20)
    delete_box = Entry(root, width=30)
    delete_box.grid(row=8, column=1, padx=20)

    # Create Text Box Label
    f_name_label = Label(root, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(root, text="Last Name")
    l_name_label.grid(row=1, column=0)
    add_label = Label(root, text="Address")
    add_label.grid(row=2, column=0)
    city_label = Label(root, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(root, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(root, text="Zip Code")
    zipcode_label.grid(row=5, column=0)
    delete_box_label = Label(root, text="ID number")
    delete_box_label.grid(row=8, column=0)

    # Create Submit Button
    submit = Button(root, text="Add to the Database", command=submit)
    submit.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=122)

    # Create a Quarry Button
    q_btn = Button(root, text="Show Records", command=query)
    q_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Create a Delete Button
    delete_btn = Button(root, text="Delete Record", command=delete)
    delete_btn.grid(row=9, column=1, columnspan=2, pady=10, padx=(100, 0))

    # Create a Update Button
    edit_btn = Button(root, text="Edit Record", command=edit)
    edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=(0, 100))

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

except EXCEPTION as e :
    print(e)

root.mainloop()