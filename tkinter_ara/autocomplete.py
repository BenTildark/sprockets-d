# AUTO COMPLETE tkinter module

from tkinter import *
from tkinter import ttk


class Autocomplete(Frame, object):
    def __init__(self, *args, **kwargs):
        width, height, entries = kwargs.pop('width'), kwargs.pop('height'), kwargs.pop('entries')
        super(Autocomplete, self).__init__(*args, **kwargs)
        self.list = []
        self._entries = entries
        self.listbox_height = height
        self.entry_width = width
        self.text = StringVar()
        self.entry = ttk.Entry(self, textvariable=self.text, width=self.entry_width)
        self.frame = Frame(self)
        self.listbox = Listbox(self.frame, height=self.listbox_height, width=self.entry_width)
        self.dropdown = Listbox(self.frame, height=self.listbox_height, width=self.entry_width, background="#cfeff9",
                                takefocus=0)
        self.entry.pack()
        self.frame.pack()
        self.listbox.grid(column=0, row=0, sticky=N)
        self.dropdown.grid(column=0, row=0, sticky=N)
        self.dropdown.grid_forget()


root = Frame(Tk())
root.pack()

autocomplete = Autocomplete(root, width=74, height=10, entries=['02', '01', '01', '02', '01'])
autocomplete.pack()
mainloop()
