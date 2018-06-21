from tkinter import *


# We create a class called App, which is the Frame where widgets are held.
class App(Frame):

    # We create a method called __init__. This initializes the class, and runs another method called widgets.
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.widgets()

    # We create the widgets method. This is where the widget, menubar is added. If we were to create anymore widgets,
    #  they would also be here.
    def widgets(self):
        menubar = Menu(root)
        menubar.add_command(label="File")
        menubar.add_command(label="Quit", command=root.quit())

        root.config(menu=menubar)


root = Tk()
root.title("Menubar")
app = App(root)
root.mainloop()
# Lastly, we give the entire window some properties. We give it a title, Menubar, and run the App class. lastly,
#  we start the GUI's mainloop with root.mainloop.
