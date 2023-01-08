#Password Generator Project
import random

#List of possible inputs
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Take user input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Random password generator (category wise)
i=0
let=""
for char in range(1,nr_letters+1):
  lt = random.choice(letters)
  let=let+lt

sym=""
for char in range(1,nr_symbols+1):
  sy = random.choice(symbols)
  sym=sym+sy

num=""
for char in range(1,nr_numbers+1):
  nu = random.choice(symbols)
  num=num+nu

password=let+sym+num #merging all categories

l=list(password) #shuffling password
random.shuffle(l)
shf_l=''.join(l)
print(f" Your password is: {shf_l}") #print result
