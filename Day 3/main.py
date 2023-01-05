print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
name=input("What is your name? ")
print(f"Dear Detective {name}, Welcome to Treasure Island.")
print("Your mission is to find the treasure by using the given clues by choosing the correct option.") 
print(f"HINT 1: {name}! Please walk to the building that has the most stories.")
print("A: School, B: Library, C: Hospital")
ans1=input("Input your answer: A,B or C.")

if(ans1=='A' or ans1=='C'):
  print("Tough Luck! Please start again.")
  exit()
elif(ans1=='B'):
  print("Good job!")
  print(f"{name} proceeds to walk towards the library!")
  print(f"{name} reaches the library.")
  print("Lets head to the next level!")
else:
  print("Invalid input! Please start again.")
  exit()
  
print(f"HINT 2: {name}! I go up and down, but I never move.")
print("A: Stairs, B: Age, C: Height")
ans2=input("Input your answer: A,B or C.")
if(ans2=='B' or ans2=='C'):
  print("Tough Luck! Please start again.")
  exit()
elif(ans2=='A'):
  print("Good job once again!")
  print(f"{name} proceeds to walk towards the stairs!")
  print(f"{name} reaches the terrace.")
  print("Lets head to the final level!")
else:
  print("Invalid input! Please start again.")
  exit()

print(f"Final Hint {name}! You are at the terrace and can see 3 sacks infront of you. One of them has the key to the treasure box.")
print("The clue is: Put your phone in me after dropping it in water. I also make a cheap and easy dinner, on nights you just don’t want to bother.")
print("A: Wheat, B: Oats, C: Rice")
ans3=input("Input your answer: A,B or C.")
if(ans3=='B' or ans3=='A'):
  print("Tough Luck! Please start again.")
  exit()
elif(ans3=='C'):
  print(f"{name} searches through the sack of rice!")
  print(f"{name} finds the KEY!!!")
  print("Congratulations! You win the game! ^-^")
else:
  print("Invalid input! Please start again.")
  exit()





