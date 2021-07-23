"""
Write an algorithm to change a string into a "goofy" version.
"""
import random
from tkinter import messagebox, simpledialog, Tk


def goofy(goofy_name):
    name_list = list(name)
    for i in range(len(name)):
        if i % 2 == 0:
            name_list[i] = name_list[i].upper()
        else:
            name_list[i] = name_list[i].lower()
    goofy_name = name_list
    messagebox.showinfo(None, goofy_name)

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(None, "What is your name")
    goofy(name)

    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    pass
