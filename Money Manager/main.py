from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from database import Database
from tkinter import messagebox as mb

window = Tk()
window.config(bg="#1b262c")
bg_color = "#1b262c"
button_color = "#ffa372"

db = Database(window, "database.txt")

def earn_button_clicked():
    db.earn()
    populate_list()

def spent_button_clicked():
    db.spent()
    populate_list()

def populate_list():
    current_amount = 0

    entry_listbox.delete(0, END)
    db.read()
    
    for entry in db.entries:
        if entry[0] == "earn":
            data = entry[1] + ": You earn $" + entry[2]
            entry_listbox.insert(END, data)
            current_amount += float(entry[2])

        elif entry[0] == "spent":
            data = entry[1] + ": You spent $" + entry[2] + " on " + entry[3]
            entry_listbox.insert(END, data)
            current_amount -= float(entry[2])

    current_amount_label.config(text="$" + format(current_amount, '.2f'))

def clear_button_clicked():
    db.clear_all()
    populate_list()

def delete_button_clicked():
    if len(entry_listbox.curselection()) == 0:
        mb.showerror("Error","Please select an entry to delete!")
    else:
        db.delete(entry_listbox.curselection()[0])
        entry_listbox.delete(entry_listbox.curselection())
        populate_list()

def edit_button_clicked(): 
    if len(entry_listbox.curselection()) == 0:
        mb.showerror("Error", "Please select an entry to edit!")
    else:
        db.edit(entry_listbox.curselection()[0])
        populate_list()

top_panel_frame = Frame(window, bg=bg_color)

profile_photo = ImageTk.PhotoImage(Image.open("images/profile.png").resize((80, 80)))
profile_photo_label = Label(top_panel_frame, image=profile_photo, bg=bg_color)
profile_photo_label.image = profile_photo

name_title_label = Label(top_panel_frame, text="Name:", font=("", 13), bg=bg_color, fg="white")
name_label = Label(top_panel_frame,text="Test", font=("", 20, "bold"), bg=bg_color, width=15, fg="white")

current_amount_title_label = Label(top_panel_frame, text="Current Amount:", font=("", 13), bg=bg_color, fg="white")
current_amount_label = Label(top_panel_frame, text="$0.00", font=("", 20, "bold"), bg=bg_color, width=15, fg="white")

profile_photo_label.grid(row=0, column=0, rowspan=2, padx=50, pady=20)
name_title_label.grid(row=0, column=1)
name_label.grid(row=0, column=2)
current_amount_title_label.grid(row=1, column=1)
current_amount_label.grid(row=1, column=2)

left_panel_frame = Frame(window, bg=bg_color)

earn_img = ImageTk.PhotoImage(Image.open("images/add.png").resize((100, 100)))
earn_button = Button(left_panel_frame, image=earn_img, bg=button_color, width=200, height=150, command=earn_button_clicked)
earn_button_Label = Label(left_panel_frame, text="Earn Money", bg=bg_color, fg="white")

spent_img = ImageTk.PhotoImage(Image.open("images/minus.png").resize((100, 100)))
spent_button = Button(left_panel_frame, image=spent_img, bg=button_color, width=200, height=150, command=spent_button_clicked)
spent_button_Label = Label(left_panel_frame, text="Spent Money", bg=bg_color, fg="white")

clear_img = ImageTk.PhotoImage(Image.open("images/clear.png").resize((100, 100)))
clear_button = Button(left_panel_frame, image=clear_img, bg=button_color, width=200, height=150, command=clear_button_clicked)
clear_button_Label = Label(left_panel_frame, text="Clear All Entries", bg=bg_color, fg="white")

earn_button.grid(row=0, column=0)
earn_button_Label.grid(row=1, column=0)
spent_button.grid(row=2, column=0)
spent_button_Label.grid(row=3, column=0)
clear_button.grid(row=4, column=0)
clear_button_Label.grid(row=5, column=0)
mid_panel_frame = Frame(window, bg=bg_color)

entry_listbox = Listbox(mid_panel_frame, font=("", 12), bg=bg_color, fg="white", width=40, height=27 )
entry_title = Label(mid_panel_frame, text="History", bg=bg_color, fg="white", font=("", 20, "bold"))

entry_title.grid(row=0, column=0)
entry_listbox.grid(row=1, column=0, sticky="news")

right_panel_frame = Frame(window, bg=bg_color)

edit_img = ImageTk.PhotoImage(Image.open("images/edit.png").resize((100, 100)))
edit_button = Button(right_panel_frame, image=edit_img, bg=button_color, width=200, height=150, command=edit_button_clicked)
edit_button_Label = Label(right_panel_frame, text="Edit Entry", bg=bg_color, fg="white")

delete_img = ImageTk.PhotoImage(Image.open("images/delete.png").resize((100, 100)))
delete_button = Button(right_panel_frame, image=delete_img, bg=button_color, width=200, height=150, command=delete_button_clicked)
delete_button_Label = Label(right_panel_frame, text="Delete Entry", bg=bg_color, fg="white")

edit_button.grid(row=0, column=0)
edit_button_Label.grid(row=1, column=0)
delete_button.grid(row=2, column=0)
delete_button_Label.grid(row=3, column=0)

top_panel_frame.grid(row=0, column=0, columnspan=3, padx=100,sticky="news")
left_panel_frame.grid(row=1, column=0, sticky="news")
mid_panel_frame.grid(row=1, column=1, sticky="news")
right_panel_frame.grid(row=1, column=2, sticky="news")

populate_list()

window.mainloop()
