"""

Imagine a simple Tkinter app. (Everything is pretty much the same for most other GUI frameworks,
and many frameworks for games and network servers, and even things like SAX parsers, but most novices
first run into this with GUI apps, and Tkinter is easy to explore because it comes with Python.)

    def handle_click():
        print('Clicked!')



Now imagine that, instead of just printing a message, you want it to pop up a window, wait 5 seconds,
then close the window. You might try to write this:

"""
from tkinter import *
import time

root = Tk()
root.mainloop()

print(time)


def handle_click():

    win = Toplevel(root, title='Hi!')
    win.transient()
    Label(win, text='Please wait...').pack()
    Button(root, text='Click me', command=handle_click).pack()
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    win.destroy()


handle_click()


