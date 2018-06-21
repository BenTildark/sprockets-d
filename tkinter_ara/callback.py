"""

Why your GUI app freezes
Imagine a simple Tkinter app. (Everything is pretty much the same for most other GUI frameworks,
 and many frameworks for games and network servers, and even things like SAX parsers, but most
  novices first run into this with GUI apps, and Tkinter is easy to explore because it comes with Python.)

    def handle_click():
        print('Clicked!')
    root = Tk()
    Button(root, text='Click me', command=handle_click).pack()
    root.mainloop()


Now imagine that, instead of just printing a message, you want it to pop up a window, wait 5 seconds,
 then close the window. You might try to write this:

    def handle_click():
        win = Toplevel(root, title='Hi!')
        win.transient()
        Label(win, text='Please wait...').pack()
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        win.destroy()


But when you click the button, the window doesn't show up. And the main window freezes up and beachballs for 5 seconds.

This is because your event handler hasn't returned, so the main loop can't process any events. It needs to
process events to display a new window, respond to messages from the OS, etc., and you're not letting it.

There are two basic ways around this problem: callbacks, or threads. There are advantages and disadvantages of both.
And then there are various ways of building thread-like functionality on top of callbacks, which let you get (part of)
 the best of both worlds, but I'll get to those in another post.
Callbacks
Your event handler has to return in a fraction of a second. But what if you still have code to run? You have to
 reorganize your code: Do some setup, then schedule the rest of the code to run later. And that "rest of the code"
  is also an event handler, so it also has to return in a fraction of a second, which means often it will have to do
   a bit of work and again schedule the rest to run later.

Depending on what you're trying to do, you may want to run on a timer, or whenever the event loop is idle, or
 every time through the event loop no matter what. In this case, we want to run once/second. In Tkinter, you do
  this with the after method:

"""

from tkinter import *

root = Tk()
root.mainloop()


def handle_click():
    win = Toplevel(root, title='Hi!')
    win.transient()
    Label(win, text='Please wait...').pack()
    i = 5

    def callback():
        nonlocal i, win
        print(i)
        i -= 1
        if not i:
            win.destroy()
        else:
            root.after(1000, callback)

    root.after(1000, callback)


handle_click()

