from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed(5)
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        time.sleep(1*self.movespeed)
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)

    def bouncey (self):
        self.ymove *= -1

    def bouncex (self):
        self.xmove *= -1 
        self.movespeed *= 0.8
    
    def refresh(self):
        time.sleep(0.5)
        self.goto(0,0)
        self.bouncex()
        self.movespeed = 0.1
        