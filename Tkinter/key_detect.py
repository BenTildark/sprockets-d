
from tkinter import *

wn = Tk()
wn.title('KeyDetect')


def down(e):
    print(e.char, e)


wn.bind('<KeyPress>', down)

wn.mainloop()
