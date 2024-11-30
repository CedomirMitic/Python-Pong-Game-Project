from turtle import Turtle
UP = 20
DOWN = -20


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)

    def up(self):
        position = self.ycor()
        up = position + UP
        self.goto(self.xcor(), up)

    def down(self):
        position = self.ycor()
        down = position + DOWN
        self.goto(self.xcor(), down)
