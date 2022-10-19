from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position,color) :
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color(color)
        self.goto(position)
        self.score = 0

    def goup(self):
        if(self.ycor()<=220):
            new_y = self.ycor()+20
            self.goto(self.xcor(),new_y)

    def godown(self):
        if(self.ycor()>=-220):
            new_y = self.ycor()-20
            self.goto(self.xcor(),new_y)
        
    
    def increase(self):
        self.score += 1