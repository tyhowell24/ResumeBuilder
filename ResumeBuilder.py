# Project: Resume Builder
from tkinter import *
import tkinter as tk
from docx import Document

#Build the Window
window = tk.Tk()
# Set the geometry of the window
window.geometry("700x350")
window.title('Build My Resume')

# declaring string variable
# for storing name and address
fname_var=tk.StringVar()
lname_var=tk.StringVar()

# Function to pull and get the information for the word doc
def build_document():
    first_name =fname_var.get()
    last_name =lname_var.get()
    full_name= first_name + " " + last_name
    document = Document()
    document.add_heading(full_name, 0)
    

    document.save('demo.docx')
    
# Code to add the widgets will go here

# Create a label widget
first_name = tk.Label(window, text="First Name: ").place(x=10,y=10)
last_name = tk.Label(window, text="Last Name: ").place(x=10,y=50)
street = tk.Label(window, text="Street Address: ").place(x=10,y=90)
city = tk.Label(window, text="City: ").place(x=10,y=130)
state = tk.Label(window, text="State: ").place(x=10,y=170)
zip_code = tk.Label(window, text="Zip Code: ").place(x=10,y=210)

# Create entry area
first_name_input = tk.Entry(window, textvariable = fname_var, width = 30).place(x = 110, y = 10)
last_name_input = tk.Entry(window, textvariable = lname_var, width = 30).place(x = 110, y = 50)
street_input = tk.Entry(window, width = 30).place(x = 110, y = 90)
city_input = tk.Entry(window, width = 30).place(x = 110, y = 130)
state_input = tk.Entry(window, width = 30).place(x = 110, y = 170)
zip_input = tk.Entry(window, width = 30).place(x = 110, y = 210)

# Create a Button
submit_button = tk.Button(window,text = "Submit",command=build_document).place(x = 10,y = 250)

window.mainloop()