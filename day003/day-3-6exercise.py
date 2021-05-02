print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('you are at a crossroad. type "left" or "right".')
if choice1 == "left":
  choice2 = input('you have come to a lake. there is a island in the middle of the lake. type "swim"to swim across or type "wait" for a boat. ')
  if choice2 == "wait":
    choice3 = input("you arrive at a island. it contains 3doors. one red, one yellow, one blue.").
    if choice3 == "red":
      print("you are burned by fire. game over.")
    elif choice3 == "yellow":
      print("you got the treasure hunt. You Win!")
    elif choice3 == "blue":
      print("you have eaten by beasts.game over!")
    else:
      print("you choose a door that dose not exist. ")
  else:
    print("you have attaced by snake game over.")

else:
  print("game over. ")

