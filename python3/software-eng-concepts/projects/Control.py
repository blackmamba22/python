import sys

class Control:
    """Exercises with control-flow and conditional statements."""

    def __init__(self):
        pass

    @staticmethod
    def draw_regular_patterns():
        """Draw multiple shapes and colors using turtle library."""
        import turtle

        silly = turtle.Turtle()
        silly.color("#32D486")
        silly.fillcolor("red")
        x = 50
        d = 90

        a, b = (1,1)
        for p in range(10):
            silly.goto(a, b)
            for i in range(4):
                silly.forward(x)
                silly.right(d)     # Rotate clockwise by 90 degrees
            x += 25
            a+=10
            b+=20
        turtle.done()
