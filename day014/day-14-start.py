from art import logo
from art import vs
from game_data import data
import random
from replit import clear


def format_data(account):
  account_name = account["name"]
  account_dsrp = account["description"]
  account_country = account["country"]
  return f"{account_name}, a{account_dsrp}, from{account_country}"

def check_answer(guess, a_follower, b_follower):
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"CompareA: {format_data(account_a)}")
  print(vs)
  print(f"AganistB: {format_data(account_b)}")

  guess = input("Who has more followers? type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"you got a right: {score}")
  else:
    game_should_continue = False
    print(f"sorry you got a wrong. final score:{score}.")