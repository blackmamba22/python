import sys
import random

class Control:
    """Exercises with control-flow and conditional statements."""

    def __init__(self):
        pass

    @staticmethod
    def draw_regular_patterns():
        """Draw multiple shapes and colors using turtle library."""
        import turtle
        turtle.screensize(800, 800)
        color_lst = ["#90C3D4", "#C390D4", "#D4A190", "#A1D490", "#92E85D", "#5DD7E8", "#B35DE8", "#E86E5D", "#34EAED", "#EBF779"]

        print ("This program draws squares of many colors.\n")
        num_squares = input("\nEnter the number of squares to draw: ")

        if not num_squares.isdigit():
            print("The number must be an integer and at least 1.\nPlease try again.")
            sys.exit(1)
        elif int(num_squares) < 1:
            print("The number must be an integer and at least 1.\nPlease try again.")
            sys.exit(1)


        num_squares = int(num_squares)
        turtle_man = turtle.Turtle()
        x_direction, degree = (100, 90)
        x_cor, y_cor = (0, 0)

        for i in range(num_squares):
            turtle_man.goto(x_cor, y_cor)
            turtle_man.begin_fill()
            turtle_man.down()
            turtle_man.color(color_lst[random.randrange(0,10)])

            for j in range(4):
                turtle_man.forward(x_direction)
                turtle_man.right(degree)
            turtle_man.up() # pick up pen
            turtle_man.end_fill() # end shape color fill
            x_cor += 20
            y_cor += 10
        #turtle.done()
        turtle.clear()

        #======================================================================#
        # DRAW CIRCLES
        #======================================================================#
        print ("This program draws circles of many colors.\n")
        num_circles = input("\nEnter the number of circles to draw: ")

        if not num_circles.isdigit():
            print("The number must be an integer and at least 1.\nPlease try again.")
            sys.exit(1)
        elif int(num_circles) < 1:
            print("The number must be an integer and at least 1.\nPlease try again.")
            sys.exit(1)

        num_circles = int(num_circles)
        radius = 20
        turtle_circa = turtle.Turtle()
        w_cor, z_cor = (0, 0)
        for i in range(num_circles):
            turtle_circa.goto(w_cor, z_cor)
            turtle_circa.begin_fill()
            turtle_circa.down()
            turtle_circa.color(color_lst[random.randrange(0,10)])
            turtle_circa.circle(radius * 10)
            turtle_circa.up()
            turtle_circa.end_fill()
            w_cor += 50
            #z_cor += 50
        turtle.done()
