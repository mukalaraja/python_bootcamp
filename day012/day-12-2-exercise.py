from random import randint
from art import logo
easy_level_turn = 10
hard_level_turn = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("To high.")
    return turns - 1
  elif guess < answer:
    print("to low.")
    return turns - 1
  else:
    print(f"you got it! the answer was {answer} ")


def set_difficulty():
  level = input("choose a difficulty type'easy' or 'hard'.  ")
  if level == "easy":
    return easy_level_turn
  else:
    return hard_level_turn


def game():
  print (logo)
  print("Welcome to the number!.")
  print("I am thinking number between 1 to 100!!.")
  answer = randint(1, 100)
  print(f"the correct answer{answer}")
 


  turns = set_difficulty()

  guess= 0
  
  while guess != answer:
    print(f"you have {turns} attempts remaining too guess the number.")
    guess = int(input("make a guess."))
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("you have run out the guess. you lose!")
      return
    elif guess != answer:
      print("guess again.")
      



game()


