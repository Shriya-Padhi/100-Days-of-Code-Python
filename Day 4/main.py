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

user_play=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_play=random.randint(0,2)

if(user_play==0):
    print(f"You chose:\n {rock}")
if(user_play==1):
    print(f"You chose:\n {paper}")
if(user_play==2):
    print(f"You chose:\n {scissors}")
else:
    print("Please enter correct input.")

if(comp_play==0):
    print(f"Computer chose:\n {rock}")
if(comp_play==1):
    print(f"Computer chose:\n {paper}")
if(comp_play==2):
    print(f"Computer chose:\n {scissors}")
else:
    print("Please enter correct input.")

if((user_play==0 and comp_play==0) or (user_play==1 and comp_play==1) or (user_play==2 and comp_play==2)):
    print("It is a TIE!!")
elif((user_play==0 and comp_play==2) or (user_play==1 and comp_play==0) or (user_play==2 and comp_play==1)):
    print("Congratulations! You WON!!")
elif((user_play==2 and comp_play==0) or (user_play==0 and comp_play==1) or (user_play==1 and comp_play==2)):
    print("Oh no! You LOSE!!")
else:
    print("ERROR!! Please try again!")
