"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk

z = 0


def prime_or_nah(num):
    global z
    for i in range(int(num)-1):
        if i > 1:
            if int(num) % i == 0:
                z += 1
            else:
                z += 0
    if z >= 1:
        messagebox.showinfo(None, "Not Prime")
    elif z == 0:
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
