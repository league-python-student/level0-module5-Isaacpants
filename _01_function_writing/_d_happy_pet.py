"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk
global happiness
happiness = 5


def happiness_checker():
    global happiness
    if happiness <= 0:
        messagebox.showinfo('Your pet is sad, make it happy!')
def feed():
    global happiness
    happiness += 10
    messagebox.showinfo('Your pet has ' + happiness+' happiness')

def walk(animal):
    global happiness
    if animal == 'fish':
        happiness -= 5
    elif animal == 'cat':
        happiness -=1
    else:
        happiness +=5

def play(animal):
    global happiness
    if animal == 'cat':
        happiness -= 5
    elif animal == 'dog':
        happiness += 10
    else:
        happiness +=5
def ignore(animal):
    global happiness
    if animal == 'dog':


if __name__ == '__main__':
    animal = simpledialog.askstring(None, "What type of pet do you want?(Cat, dog, or fish")

    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    pass
