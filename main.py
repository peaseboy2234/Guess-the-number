print ('\033[91m' '\033[1m'"Enjoy the game folks"'\033[0m' '\033[96m')

import random

n = random.randint(1, 100)
guess = int(input("Enter a number from 1 to 100: "))
while n != "guess":
  print
  if guess < n:
    print ("guess is low")
    guess = int(input("Enter an number from 1 to 100: "))
  elif guess > n:
    print ("guess is high")
    guess = int(input("Enter an number from 1 to 100: "))
  else:
    print ("CONGRATS! You got it right, do you want a cookie?")
    
    break


choice = input(">")
if choice == "yes": 
  print ("to bad")
  
if choice == "Yes": 
  print ("*Gives cookie*")
 
if choice == "YES": 
  print ("Stop yelling") 
  
if choice == "no": 
  print ("Whats wrong with you")  
  
if choice == "No": 
  print ("Im not your friend anymore")  
  
if choice == "NO":
  print ("Stop yelling, my gosh")  

if choice == "yah":
  print ("No")

if choice == "Yah":
  print ("I guess you can have one *gives cookie*")

if choice == "No thank you":
  print ("*gives cookie* thanks for being nice")

