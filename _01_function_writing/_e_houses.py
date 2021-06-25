"""
Have the turtle draw a row of houses.
"""
import random
import turtle
from tkinter import messagebox, simpledialog, Tk
isaac = turtle.Turtle()
isaac.penup()
isaac.hideturtle()
isaac.goto(-300, -250)
isaac.pendown()


def pointy_top_house(height):
    isaac.left(90)
    isaac.forward(height)
    isaac.right(45)
    isaac.forward(25)
    isaac.right(90)
    isaac.forward(25)
    isaac.right(45)
    isaac.forward(height)
    isaac.left(90)
    isaac.pencolor("green")
    isaac.forward(30)
    isaac.pencolor("black")


def flat_top_house(height):
    isaac.left(90)
    isaac.forward(height)
    isaac.right(90)
    isaac.forward(25)
    isaac.right(90)
    isaac.forward(height)
    isaac.left(90)
    isaac.pencolor("green")
    isaac.forward(30)
    isaac.pencolor("black")



if __name__ == '__main__':
    size = simpledialog.askstring(None, "What size do you want(random, small, medium, or large")
    if size == "random":
        for i in range(9):
            pointy_top_house(random.randint(0, 100))
    elif size == "small":
        for i in range(9):
            pointy_top_house(60)
    elif size == "medium":
        for i in range(9):
            pointy_top_house(120)
    elif size == "large":
        for i in range(9):
            flat_top_house(250)
    else:
        messagebox.showinfo(None, "I don't know that size, please enter either random, small, medium, or large")

    window = Tk()
    window.withdraw()



    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.


    turtle.done()
    pass
