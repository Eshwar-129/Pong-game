
from turtle import Turtle,Screen
from centerline import CenterLine
from ball import Ball
from scoreboards import Scoreboard
scoreboards=Scoreboard()
turtle=Turtle()
import time
ball=Ball()
centerline=CenterLine()
from paddle import Paddle
screen=Screen()
screen.tracer(0)
screen.bgcolor('black')

screen.setup(width=800,height=600)
screen.listen()
l_paddle = Paddle(380, 0)
r_paddle = Paddle(-380, 0)
screen.onkey(l_paddle.go_up,'Up')
screen.onkey(l_paddle.go_down,'Down')
screen.onkey(r_paddle.go_up,'w')
screen.onkey(r_paddle.go_down,'s')

is_game_on=True
while is_game_on:
   time.sleep(ball.move_speed)
   screen.update()
   centerline.__init__()
   ball.refresh()
   if ball.ycor()>270 or ball.ycor()<-270 :
     ball.ball_bounce_y()
   if ball.distance(l_paddle)<50 and ball.xcor()>320 or ball.distance(r_paddle)<50 and ball.xcor()<-320:
      ball.ball_bouce_x()
   if ball.xcor()>370 :
      ball.reset_position()
      scoreboards.l_point()

   if ball.xcor()<-370:
      ball.reset_position()
      scoreboards.r_point()

























































screen.exitonclick()