import random

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
img = [rock, paper, scissors]
user = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
    ))
if user >= 3 or user < 0:
  print("It is invalid! You Lose!")
else:
 print(f"You chose:")
 print(img[user])
 computer = random.randint(0, 2)
 print(f"Computer chose:")
 print(img[computer])

 if user == 0 and computer == 2:
   print("you win!")
 elif user == 2 and computer == 0:
   print('you lose!')
 elif computer > user:
   print("you lose!")
 elif user > computer:
   print("you win!")
 elif user == computer:
   print("It is Draw!")
