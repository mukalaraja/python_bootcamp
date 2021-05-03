rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor] 
user_choice = int(input("what do you want to choose? type 0 fo rock , type 1 for paper or 2 for scissor .\n" ))
if user_choice >=3 or user_choice < 0:
  print("you typed a invalid number")
else:
 print(game_images[user_choice])
import random 
computer_choice = random.randint(0, 2) 

print(f"computerchoose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("you win!")
elif user_choice == 0 and computer_choice == 2:
  print("you lose!")
elif computer_choice > user_choice:
  print("you lose!")
elif  user_choice >computer_choice:  
  print("you win!")
elif computer_choice == user_choice:
  print("it is a draw.")

 
