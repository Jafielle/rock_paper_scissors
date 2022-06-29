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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#user =int(user)
if user == 0:
  print(rock)
elif user == 1:
  print(paper)
elif user == 2:
  print(scissors)
  
print("Computer chose:\n")
game = [rock, paper, scissors]

PC_chose= random.choice(game)
print(PC_chose)

if user == 0 and PC_chose == rock:
  print("Its a draw")
elif user == 0 and PC_chose == paper:
  print("You lose")
elif user == 0 and PC_chose == scissors:
  print("You win!")
  
if user == 1 and PC_chose == paper:
  print("Its a draw")
elif user == 1 and PC_chose == scissors:
  print("You lose")
elif user == 1 and PC_chose == rock:
  print("You win!")

if user == 2 and PC_chose == scissors:
  print("Its a draw")
elif user == 2 and PC_chose == rock:
  print("You lose")
elif user == 2 and PC_chose == paper:
  print("You win!")
