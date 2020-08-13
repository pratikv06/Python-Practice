from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Address Book")
root.iconbitmap('learning.ico')
root.geometry("400x500")

# Database
# Create or connecct to Database
conn = sqlite3.connect('address_book.db')
# Creating cursor
c = conn.cursor()
# Create Table
try:
    c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer)""")
except:
    pass

# Method to add record to database
def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Insert statement
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    conn.commit()
    conn.close()
    # Clear Entry Record
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Method to fetch record from database
def show():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query
    c.execute("SELECT oid, * FROM addresses")
    records = c.fetchall()
    # c.fetchone() # Only one record
    # c.fetchmany(10) # Return specifed record
    # Looping through Records
    print_records = '*'*5 + 'Record' +'*'*5 +'\n'
    for r in records:
        print_records += str(r[0]) +".  "+ str(r[1]) +" "+ str(r[2]) +"\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=10, column=1)

    conn.commit()
    conn.close()


# MEthod to delete records from database
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Delete Records
    c.execute("DELETE FROM addresses WHERE oid=" + del_id.get())
    conn.commit()
    conn.close()
    del_id.delete(0, END)


# Updating to datbase
def update_db():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    record_id = sel_id.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :iod""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'iod': record_id
        })
    conn.commit()
    conn.close()
    editor.destroy()


# Method to Update record from database New Window and entry
def update():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.iconbitmap('learning.ico')
    editor.geometry("400x190")
    editor.resizable(width=False, height=False)

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query
    record_id = sel_id.get()
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()
    conn.commit()
    conn.close()

    # Labels for Input Boxes
    f_name_lbl_editor = Label(editor, text="First Name").grid(row=0, column=0, padx=20, pady= (15, 0), sticky=W)
    l_name_lbl_editor = Label(editor, text="Last Name").grid(row=1, column=0, padx=20, sticky=W)
    address_lbl_editor = Label(editor, text="Address").grid(row=2, column=0, padx=20, sticky=W)
    city_lbl_editor = Label(editor, text="City").grid(row=3, column=0, padx=20, sticky=W)
    state_lbl_editor = Label(editor, text="State").grid(row=4, column=0, padx=20, sticky=W)
    zipcode_lbl_editor = Label(editor, text="Zip Code").grid(row=5, column=0, padx=20, sticky=W)

    # Making global Input variable
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Input Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=15, pady= (15, 2), ipadx=40)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=15, pady=2, ipadx=40)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=15, pady=2, ipadx=40)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=15, pady=2, ipadx=40)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=15, pady=2, ipadx=40)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=15, pady=2, ipadx=40)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create Update button
    update_btn_editor = Button(editor, text="Save Record", padx=10, command=update_db)
    update_btn_editor.grid(row=9, column=1, padx=15, pady=(2,10), ipadx=10, sticky=W)
    # Create cancel button
    cancel_btn_editor = Button(editor, text="Cancel", padx=10, command=editor.destroy)
    cancel_btn_editor.grid(row=9, column=1, padx=15, pady=(2,10), ipadx=10, sticky=E)

    


# Labels for Input Boxes
f_name_lbl = Label(root, text="First Name").grid(row=0, column=0, padx=20, pady= (15, 0), sticky=W)
l_name_lbl = Label(root, text="Last Name").grid(row=1, column=0, padx=20, sticky=W)
address_lbl = Label(root, text="Address").grid(row=2, column=0, padx=20, sticky=W)
city_lbl = Label(root, text="City").grid(row=3, column=0, padx=20, sticky=W)
state_lbl = Label(root, text="State").grid(row=4, column=0, padx=20, sticky=W)
zipcode_lbl = Label(root, text="Zip Code").grid(row=5, column=0, padx=20, sticky=W)
sel_id_lbl = Label(root, text="Select ID ").grid(row=8, column=0, padx=20, sticky=W)

# Create Input Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=15, pady= (15, 2), ipadx=40)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=15, pady=2, ipadx=40)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=15, pady=2, ipadx=40)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=15, pady=2, ipadx=40)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=15, pady=2, ipadx=40)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=15, pady=2, ipadx=40)
sel_id = Entry(root, width=30)
sel_id.grid(row=8, column=1, padx=15, pady=2, ipadx=40)

# Submit Button
submit_btn = Button(root, text="Save Record to Database", command=save)
submit_btn.grid(row=6, column=1,  pady=8, ipadx=62)

# Create Fetch button
query_btn = Button(root, text="Show Record", padx=10, command=show)
query_btn.grid(row=7 , column=1, pady=(0,8), ipadx=83)

# Create Delete button
delete_btn = Button(root, text="Delete Record", padx=10, command=delete)
delete_btn.grid(row=9, column=1, padx=15, pady=(2,10), ipadx=10, sticky=E)

# Create Update button
update_btn = Button(root, text="Update Record", padx=10, command=update)
update_btn.grid(row=9, column=1, padx=15, pady=(2,10), ipadx=10, sticky=W)

root.mainloop()