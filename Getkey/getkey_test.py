"""
Testing get-key module

"""
from getkey import getkey, keys

key = getkey()
if key == keys.UP:
    print("key up")
elif key == keys.DOWN:
    print("key down")
elif key == 'a':
    print("clicked a")
elif key == 'Y':
    print("Held shift & clicked y")


