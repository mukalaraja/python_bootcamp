import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
def random_color():
  r = random.randint(0, 255)
  b = random.randint(0, 255)
  g = random.randint(0, 255)
  random_color = (r, b, g)
  return random_color

direction = (0, 90, 180, 270)
tim.pensize(5)
tim.speed("fast")

for _ in range(100):
  tim.color(random_color())
  tim.forward(20)
  tim.setheading(random.choice(direction))