import tkinter as tk       # To make the UI
from tkinter import *      # Import all the functions from the tkinter library
import xlsxwriter          # To create an excel file
from tkinter import scrolledtext

root = Tk()                         # Making a box
root.title("Post Generator")   # Title of the box

root.resizable(False, False)

canvas = Canvas(root, height=350, width=400, bg ="gray25")   # creating a canvas of given color
canvas.pack()                                                # Attaching canvas to the root

# For Login-Page

frame_1 = tk.Frame(root, bg="gray25")                             # Making a frame
frame_1.place(relwidth=350, relheight=400, relx=0, rely=0)    # Attaching frame to the root

# Heading
heading = tk.Label(frame_1, text='Login Page', bg="gray26",fg="red", font=("Arial", 25, "bold"))
heading.place(x = 110, y = 15)

# Label 1
label_1_1 = tk.Label(frame_1, text='First name:', bg="gray26",fg="white")
label_1_1.place(x = 20, y = 70)

# Text box 1
nameEntered_1_1 = tk.Text(frame_1, height = 0.5, width = 35, bg="gray26",fg="white")
nameEntered_1_1.place(x = 110, y = 70)

# Label 2
label_2_2 = tk.Label(frame_1, text='Last name:', bg="gray26",fg="white")
label_2_2.place(x = 23, y = 120)

# Text box 2
nameEntered_2_2 = tk.Text(frame_1, height = 0.5, width = 35, bg="gray26",fg="white")
nameEntered_2_2.place(x = 110, y = 120)

# Label 3
label_3_3 = tk.Label(frame_1, text='E-mail:', bg="gray26",fg="white")
label_3_3.place(x = 36, y = 170)

# Text box 3
nameEntered_3_3 = tk.Text(frame_1, height = 0.5, width = 35, bg="gray26",fg="white")
nameEntered_3_3.place(x = 110, y = 170) 

# Label 3
label_4_4 = tk.Label(frame_1, text='Password:', bg="gray26",fg="white")
label_4_4.place(x = 29, y = 220)

# Text box 3
nameEntered_4_4 = tk.Text(frame_1, height = 0.5, width = 35, bg="gray26",fg="white")
nameEntered_4_4.place(x = 110, y = 220) 

# Label 3
label_5_5 = tk.Label(frame_1, text='Username:', bg="gray26",fg="white")
label_5_5.place(x = 32, y = 270)

# Text box 3
nameEntered_5_5 = tk.Text(frame_1, height = 0.5, width = 35, bg="gray26",fg="white")
nameEntered_5_5.place(x = 110, y = 270) 

def login_button():

    inp_1_1 = nameEntered_1_1.get(1.0, "end-1c")
    first_name = inp_1_1.split("\n")

    inp_2_2 = nameEntered_2_2.get(1.0, "end-1c")
    last_name = inp_2_2.split("\n")

    inp_3_3 = nameEntered_3_3.get(1.0, "end-1c")
    email_data = inp_3_3.split("\n")

    inp_4_4 = nameEntered_4_4.get(1.0, "end-1c")
    pass_word = inp_4_4.split("\n")

    inp_5_5 = nameEntered_5_5.get(1.0, "end-1c")
    user_name = inp_5_5.split("\n")

    workbook_1 = xlsxwriter.Workbook('Info.xlsx')

    worksheet = workbook_1.add_worksheet("Login_Information")
    worksheet.write('A1', 'Firstname')
    worksheet.write('B1', 'Lastname')
    worksheet.write('C1', 'Email')
    worksheet.write('D1', 'Password')
    worksheet.write('E1', 'username')

    row_1_1 = 1
    col_1_1 = 0

    row_1_2 = 1

    row_1_3 = 1

    row_1_4 = 1

    row_1_5 = 1

    for fn in (first_name):
        worksheet.write(row_1_1, col_1_1, fn)
        row_1_1 += 1

    for ln in (last_name):
        worksheet.write(row_1_2, col_1_1+1, ln)
        row_1_2 += 1

    for em in (email_data):
        worksheet.write(row_1_3, col_1_1+2, em)
        row_1_3 += 1

    for pas in (pass_word):
        worksheet.write(row_1_4, col_1_1+3, pas)
        row_1_4 += 1

    for user in (user_name):
        worksheet.write(row_1_5, col_1_1+4, user)
        row_1_5 += 1
    
    workbook_1.close()

    root.destroy()

    root_1 = Tk()                         # Making a box
    root_1.title("Post Generator")   # Title of the box   

    root_1.resizable(False, False)

    frame_2 = tk.Frame(root_1, bg="gray25")                             # Making a frame
    frame_2.place(relwidth=700, relheight=400, relx=0, rely=0)    # Attaching frame to the root

    canvas = Canvas(root_1, height=400, width=700, bg ="gray25")   # creating a canvas of given color
    canvas.pack()

    # Label 1
    label_1 = tk.Label(root_1, text='User:', bg="gray26",fg="white")
    label_1.place(x = 20, y = 15)

    # Text box 1
    nameEntered_1 = scrolledtext.ScrolledText(root_1, height = 7, width = 38, bg="gray26",fg="white")
    nameEntered_1.place(x = 20, y = 40)

    # Label 2
    label_2 = tk.Label(root_1, text='Post:', bg="gray26",fg="white")
    label_2.place(x = 350, y = 15)

    # Text box 2
    nameEntered_2 = scrolledtext.ScrolledText(root_1, height = 7, width = 40, bg="gray26",fg="white")
    nameEntered_2.place(x = 350, y = 40)

    # Text box 3
    nameEntered_3 = scrolledtext.ScrolledText(root_1, height = 7, width = 38, bg="gray26",fg="white")
    nameEntered_3.place(x = 20, y = 190)

    # Label 3_1
    label_3_1 = tk.Label(root_1, text='Created_at:', bg="gray26",fg="white")
    label_3_1.place(x = 20, y = 165)

    # Label 4
    label_4 = tk.Label(root_1, text='Updated_at:', bg="gray26",fg="white")
    label_4.place(x = 355, y = 170)

    # Text box 4
    nameEntered_4 = scrolledtext.ScrolledText(root_1, height = 7, width = 40, bg="gray26",fg="white")
    nameEntered_4.place(x = 355, y = 190)

    def sql_button():                                               # Defining a Function 

        inp_1 = nameEntered_1.get(1.0, "end-1c")
        user_name = inp_1.split("\n")

        inp_2 = nameEntered_2.get(1.0, "end-1c")
        post_name = inp_2.split("\n")

        inp_3 = nameEntered_3.get(1.0, "end-1c")
        created_at = inp_3.split("\n")

        inp_4 = nameEntered_4.get(1.0, "end-1c")
        updated_at = inp_4.split("\n")

        # Making an excel file

        workbook = xlsxwriter.Workbook('Post.xlsx')

        worksheet_p = workbook.add_worksheet("Post_Information")
        worksheet_p.write('A1', 'User')
        worksheet_p.write('B1', 'Post')
        worksheet_p.write('C1', 'Created_at')
        worksheet_p.write('D1', 'Updated_at')

        row_1_1 = 1
        col_1_1 = 0

        row_1_2 = 1

        row_1_3 = 1

        row_1_4 = 1


        for tb in (user_name):
            worksheet.write(row_1_1, col_1_1, tb)
            row_1_1 += 1

        for cn in (post_name):
            worksheet.write(row_1_2, col_1_1+1, cn)
            row_1_2 += 1

        for jc in (created_at):
            worksheet.write(row_1_3, col_1_1+2, jc)
            row_1_3 += 1

        for oj in (updated_at):
            worksheet.write(row_1_4, col_1_1+3, oj)
            row_1_4 += 1
            
        workbook.close()

    # sql_generation_criteria button
    button_1 = tk.Button(root_1, text="POST", padx=20, pady=5, fg="white", bg="red", command = sql_button)
    button_1.place(x=300, y=320)

    root_1.mainloop()
    
button_1_1 = tk.Button(frame_1, text="Login", padx=20, pady=5, fg="white", bg="red", command = login_button)
button_1_1.place(x=160, y=305)

root.mainloop()
