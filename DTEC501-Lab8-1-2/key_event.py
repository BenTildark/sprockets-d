"""
Capturing keyboard events
==========================

Keyboard events are sent to the widget that currently owns the keyboard focus.
You can use the focus_set method to move focus to a widget:

If you run this script, you’ll find that you have to click in the frame before it starts receiving any keyboard events.

Events #
Events are given as strings, using a special event syntax:

<modifier-type-detail>
The type field is the most important part of an event specifier. It specifies the kind of event that we wish to bind,
and can be user actions like Button, and Key, or window manager events like Enter, Configure, and others.
The modifier and detail fields are used to give additional information, and can in many cases be left out.
There are also various ways to simplify the event string; for example, to match a keyboard key, you can leave out
the angle brackets and just use the key as is. Unless it is a space or an angle bracket, of course.

Instead of spending a few pages on discussing all the syntactic shortcuts, let’s take a look on the most common event
formats:

Event Formats
<Button-1>
A mouse button is pressed over the widget. Button 1 is the leftmost button, button 2 is the middle button
(where available), and button 3 the rightmost button. When you press down a mouse button over a widget,
Tkinter will automatically “grab” the mouse pointer, and subsequent mouse events (e.g. Motion and Release events)
will then be sent to the current widget as long as the mouse button is held down, even if the mouse is moved outside
the current widget. The current position of the mouse pointer (relative to the widget) is provided in the x and y
members of the event object passed to the callback.

You can use ButtonPress instead of Button, or even leave it out completely: <Button-1>, <ButtonPress-1>, and <1> are all
synonyms. For clarity, I prefer the <Button-1> syntax.

<B1-Motion>
The mouse is moved, with mouse button 1 being held down (use B2 for the middle button, B3 for the right button).
The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback.

<ButtonRelease-1>
Button 1 was released. The current position of the mouse pointer is provided in the x and y members of the event object
passed to the callback.

<Double-Button-1>
Button 1 was double clicked. You can use Double or Triple as prefixes. Note that if you bind to both a single click
(<Button-1>) and a double click, both bindings will be called.

<Enter>
The mouse pointer entered the widget (this event doesn’t mean that the user pressed the Enter key!).

<Leave>
The mouse pointer left the widget.

<FocusIn>
Keyboard focus was moved to this widget, or to a child of this widget.

<FocusOut>
Keyboard focus was moved from this widget to another widget.

<Return>
The user pressed the Enter key. You can bind to virtually all keys on the keyboard. For an ordinary 102-key PC-style
keyboard, the special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key),
Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End,
Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock,
and Scroll_Lock.

<Key>
The user pressed any key. The key is provided in the char member of the event object passed to the callback
(this is an empty string for special keys).

a
The user typed an “a”. Most printable characters can be used as is. The exceptions are space (<space>) and less than
(<less>). Note that 1 is a keyboard binding, while <1> is a button binding.

<Shift-Up>
The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes like Alt, Shift, and Control.

<Configure>
The widget changed size (or location, on some platforms). The new size is provided in the width and height attributes
of the event object passed to the callback.

The Event Object
The event object is a standard Python object instance, with a number of attributes describing the event.

Event Attributes
widget
The widget which generated this event. This is a valid Tkinter widget instance, not a name. This attribute is set for
all events.

x, y
The current mouse position, in pixels.

x_root, y_root
The current mouse position relative to the upper left corner of the screen, in pixels.

char
The character code (keyboard events only), as a string.

keysym
The key symbol (keyboard events only).

keycode
The key code (keyboard events only).

num
The button number (mouse button events only).

width, height
The new size of the widget, in pixels (Configure events only).

type
The event type.

For portability reasons, you should stick to char, height, width, x, y, x_root, y_root, and widget.
Unless you know exactly what you’re doing, of course…


"""

from tkinter import *

root = Tk()


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)


frame = Frame()
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()

