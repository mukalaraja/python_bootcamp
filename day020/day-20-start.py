from turtle import Screen, Turtle
from snake import Snake
import time
screen =  Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)   
  
  snake.move()
   
     





#s_1 = Turtle("square")
#s_1.color("white")

#s_2 = Turtle("square")
#s_2.color("white")
#s_2.goto(-40, 0)
#s_3 = Turtle("square")
#s_3.color("white")
#s_3.goto(-20, 0)
