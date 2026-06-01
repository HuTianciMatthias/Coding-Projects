from tkinter import *
from PIL import ImageTk, Image


window = Tk()
bg_color = "#1b262c"


###################### Top panel UI ######################
# Top panel widgets
top_panel_frame = Frame(window, bg=bg_color)

profile_photo = ImageTk.PhotoImage(Image.open("images/profile.png").resize((80, 80)))
profile_photo_label = Label(top_panel_frame, image=profile_photo, bg=bg_color)
profile_photo_label.image = profile_photo

name_title_label = Label(top_panel_frame, text="Name:", font=("", 13), bg="#1b262c", fg="white")
name_label = Label(top_panel_frame,text="Teacher Dora", font=("", 20, "bold"), bg="#1b262c", width=15, fg="white")

current_amount_title_label = Label(top_panel_frame, text="Current Amount:", font=("", 13), bg="#1b262c", fg="white")
current_amount_label = Label(top_panel_frame, text="$0.00", font=("", 20, "bold"), bg="#1b262c", width=15, fg="white")

# Top panel grid position
profile_photo_label.grid(row=0, column=0, rowspan=2, padx=50, pady=20)
name_title_label.grid(row=0, column=1)
name_label.grid(row=0, column=2)
current_amount_title_label.grid(row=1, column=1)
current_amount_label.grid(row=1, column=2)


###################### Left Panel UI ######################
# Left Panel widgets
left_panel_frame = Frame(window, bg=bg_color)

earn_img = ImageTk.PhotoImage(Image.open("images/add.png").resize((100, 100)))
earn_button = Button(left_panel_frame, image=earn_img, bg="#ffa372", width=200, height=150)
earn_button_Label = Label(left_panel_frame, text="Earn Money", bg="#1b262c", fg="white")

spent_img = ImageTk.PhotoImage(Image.open("images/minus.png").resize((100, 100)))
spent_button = Button(left_panel_frame, image=spent_img, bg="#ffa372", width=200, height=150)
spent_button_Label = Label(left_panel_frame, text="Spent Money", bg="#1b262c", fg="white")

clear_img = ImageTk.PhotoImage(Image.open("images/clear.png").resize((100, 100)))
clear_button = Button(left_panel_frame, image=clear_img, bg="#ffa372", width=200, height=150)
clear_button_Label = Label(left_panel_frame, text="Clear All Entries", bg="#1b262c", fg="white")

# Left panel grid position
earn_button.grid(row=0, column=0)
earn_button_Label.grid(row=1, column=0)
spent_button.grid(row=2, column=0)
spent_button_Label.grid(row=3, column=0)
clear_button.grid(row=4, column=0)
clear_button_Label.grid(row=5, column=0)


###################### Right Panel UI ######################
# Right Panel widgets
right_panel_frame = Frame(window, bg=bg_color)

edit_img = ImageTk.PhotoImage(Image.open("images/edit.png").resize((100, 100)))
edit_button = Button(right_panel_frame, image=edit_img, bg="#ffa372", width=200, height=150)
edit_button_Label = Label(right_panel_frame, text="Edit Entry", bg="#1b262c", fg="white")

delete_img = ImageTk.PhotoImage(Image.open("images/delete.png").resize((100, 100)))
delete_button = Button(right_panel_frame, image=delete_img, bg="#ffa372", width=200, height=150)
delete_button_Label = Label(right_panel_frame, text="Delete Entry", bg="#1b262c", fg="white")

# Right panel grid position
edit_button.grid(row=0, column=2)
edit_button_Label.grid(row=1, column=2)
delete_button.grid(row=2, column=2)
delete_button_Label.grid(row=3, column=2)



###################### Middel Panel UI ######################
# Middel Panel widgets
mid_panel_frame = Frame(window, bg=bg_color)

entry_listbox = Listbox(mid_panel_frame, font=("", 12), bg="#1b262c", fg="white", width=40, height=25 )
entry_title = Label(mid_panel_frame, text="History", bg="#1b262c", fg="white", font=("", 20, "bold"))

entry_title.grid(row=0, column=0)
entry_listbox.grid(row=1, column=0, sticky="news")
 
# frames grid position
top_panel_frame.grid(row=0, column=0, columnspan=3)
left_panel_frame.grid(row=1, column=0, sticky="news")
mid_panel_frame.grid(row=1, column=1, sticky="news")
right_panel_frame.grid(row=1, column=2,sticky = "news")


window.mainloop()
