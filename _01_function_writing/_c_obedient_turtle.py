"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

isaac = turtle.Turtle()

def triangle():
    isaac.pendown()
    isaac.hideturtle()
    isaac.forward(50)
    isaac.right(120)
    isaac.forward(50)
    isaac.right(120)
    isaac.forward(50)
    isaac.right(120)

def square():
    isaac.pendown()
    isaac.hideturtle()
    isaac.forward(50)
    isaac.right(90)
    isaac.forward(50)
    isaac.right(90)
    isaac.forward(50)
    isaac.right(90)
    isaac.forward(50)
def circle():
    isaac.pendown()
    isaac.hideturtle()
    for i in range(360):
        isaac.forward(1)
        isaac.right(1)

if __name__ == '__main__':
    shape = simpledialog.askstring(None, "What shape do you want(square, circle, triangle")
    if str(shape) == 'square':
        square()
    elif str(shape) == 'triangle':
        triangle()
    elif str(shape) == 'circle':
        circle()
    else:
        pass
    messagebox.showinfo('Not a shape; try square, circle, triangle')

    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    turtle.done()
    pass
