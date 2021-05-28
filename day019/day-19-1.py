from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race?. enter a color: ")
print(user_bet)
colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_positions = [-80, -50, -20, 50, 20, 80]
all_tim = []

for turtle_index in range (0, 6):
  new_tim = Turtle(shape="turtle")
  new_tim.color(colors[turtle_index])
  new_tim.penup()
  new_tim.goto(x=-240, y=y_positions[turtle_index])
  all_tim.append(new_tim)


if user_bet:
  is_race_on = True


while is_race_on:


  for turtle in all_tim:
    if turtle.xcor() > 240:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"you win! the {winning_color} is the winner!!")
      else:
        print(f"you lose! the {winning_color} is the winner!!")
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)
