from turtle import Turtle

class Paddle:
  def __init__(self, position):
    super().__init__()
    # paddle = Turtle()
    self.color('white')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.shape('square')
    self.goto(position)

  def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)