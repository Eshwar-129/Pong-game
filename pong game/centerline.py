from turtle import  Turtle
class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.pendown()
        self.right(90)
        self.color('white')

        for i in range(30):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()


