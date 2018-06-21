"""

from tkinter import *​


# Define a function to handle the event.​

def button_pressed():​

    print("Somebody pressed the button.")​

    print("{} was entered.".format(entered_data.get()))​

# Create the root window​

root_window = Tk()​

​

# Add a label to root window​

hello_label = Label(root_window,text = "Hello DTEC501") ​

hello_label.pack()​

​

# adds a text area for entering data​

entered_data = StringVar() # defines the widget state as string​

text_area = Entry(root_window, textvariable = entered_data) ​

text_area.pack()​

​

# Add a button to root window   ​

the_button = Button(None, text="Click to enter.", command = button_pressed) ​

the_button.pack() ​

​

root_window.mainloop()

"""
from tkinter import *


def button_pressed():
    print("{} was entered.".format(entered_data.get()))
    selected = "You typed " + str(entered_data.get())
    label.config(text=selected)
    root_window.quit()


def update_widget():
    print("You selected option {}.".format(option_value.get()))
    selected = "You selected option " + str(option_value.get())
    label.config(text=selected)
    root_window.quit()


# Create the root window
root_window = Tk()
option_value = IntVar()

# Set window title
root_window.title("Tk Experimentation Window")

# Set window size in pixels
root_window.geometry("400x400")

hello_label = Label(root_window, text="Hello DTEC501")
hello_label.pack()

entered_data = StringVar()
text_area = Entry(root_window, textvariable=entered_data)
text_area.pack()

radio_btn1 = Radiobutton(root_window, text="Option 1", variable=option_value, value=1, command=update_widget)
radio_btn1.pack(anchor=W)

radio_btn2 = Radiobutton(root_window, text="Option 2", variable=option_value, value=2, command=update_widget)
radio_btn2.pack(anchor=W)

the_button = Button(None, text="Click to enter.", command=button_pressed)
the_button.pack()

label = Label(root_window)
label.pack()

# Keep the window running​
root_window.mainloop()

