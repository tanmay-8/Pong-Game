from turtle import Screen, onkeypress
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=550)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


leftpaddle = Paddle((-380,0),"red")
rightpaddle = Paddle((375,0),"blue")
ball = Ball()
sb = Scoreboard()


screen.listen()
screen.onkeypress(rightpaddle.goup,'Up')
screen.onkeypress(rightpaddle.godown,'Down')
screen.onkeypress(leftpaddle.goup,'w')
screen.onkeypress(leftpaddle.godown,'s')

while True:
    ball.move()
    screen.update()

    if(ball.ycor()>255 or ball.ycor()<-255):
        ball.bouncey()
    
    if((ball.xcor()>= 353  and ball.ycor()-rightpaddle.ycor()==60) or (ball.ycor()-leftpaddle.ycor()==60 and ball.xcor()<=-355) ):
        ball.bouncey()

    if((ball.distance(rightpaddle)<50 and ball.xcor()>=353 ) or (ball.distance(leftpaddle)<50) and ball.xcor()<=-355):
        ball.bouncex()

    if(ball.xcor()>375):
        ball.refresh()
        leftpaddle.increase()
        sb.l_point()
    if(ball.xcor()<-375):
        ball.refresh()
        rightpaddle.increase()
        sb.r_point()
    
screen.exitonclick()

