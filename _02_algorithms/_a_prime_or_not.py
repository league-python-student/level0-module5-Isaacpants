"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


def prime_or_nah(num):
    if int(num) == 2 or int(num) == 0:
        messagebox.showinfo(None, "Prime")
    elif int(num) % 2 == 0:
        messagebox.showinfo(None, "Not prime")
    else:
        messagebox.showinfo(None, "Prime")


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num = simpledialog.askstring(None, "Give me a number")
    prime_or_nah(num)

    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    pass
