from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
  
  def __init__(self):
    self.segment = []
    self.create_snake()
    self.head = self.segment[0]


  def create_snake(self):
    for position in STARTING_POSITION:
      new_s = Turtle("square")
      new_s.color("white")
      new_s.penup()
      new_s.goto(position)
      self.segment.append(new_s)

  def move(self):
    for seg_num in range(len(self.segment)-1, 0, -1):
      new_x = self.segment[seg_num -1].xcor() 
      new_y = self.segment[seg_num -1].ycor()
      self.segment[seg_num].goto(new_x, new_y)   
    self.head.forward(MOVE_FORWARD)  
    
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  def down(self):
    if self.head.heading() != UP:
      self.heading.setheading(DOWN)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.heading.setheading(LEFT)

  def right(self):
    if self.head.heading() != DOWN:
      self.head.setheading(RIGHT)
