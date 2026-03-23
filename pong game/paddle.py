from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,new_x,new_y):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(new_x,new_y)
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)


    def go_down(self):
        new_y1=self.ycor()-20
        self.goto(self.xcor(),new_y1)




























        #self.head1=None
        #self.head2=None
    #def first_paddle(self):
    #    for pos in postions_first:
    #        new_segment=Turtle(shape="square")
    #        new_segment.color("white")
    #        new_segment.penup()
    #        new_segment.goto(pos)
    #        self.segments.append(new_segment)
    #    self.head1=self.segments[0]
    #def second_paddle(self):
    #    for pos2 in postions_second:
    #        new_segment1 = Turtle(shape="square")
    #        new_segment1.color("white")
    #        new_segment1.penup()
    #        new_segment1.goto(pos2)
    #        self.segments1.append(new_segment1)
    #    self.head2=self.segments1[0]
    #ef move(self):
    #   self.head1.forward(move_distance)
    #ef up(self):
    #   if self.head1.heading()!=down:
    #       self.head1.setheading(up)
    #ef down(self):
    #   if self.head1.heading()!=up:
    #       self.head1.setheading(down)



































