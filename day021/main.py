from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen =  Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

#food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
   
#collision with wall
  if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.xcor() < -230:
    game_is_on = False
    scoreboard.gameover()

#detect head hit the tail
  for segment in snake.segment:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.gameover()
      



#s_1 = Turtle("square")
#s_1.color("white")

#s_2 = Turtle("square")
#s_2.color("white")
#s_2.goto(-40, 0)
#s_3 = Turtle("square")
#s_3.color("white")
#s_3.goto(-20, 0)