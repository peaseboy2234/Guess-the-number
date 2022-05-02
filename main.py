print('\033[91m' '\033[1m' "Enjoy the game folks" '\033[0m' '\033[96m')

import random

n = random.randint(1, 100)
guess = int(input("Enter a number from 1 to 100: "))
while n != "guess":
	print
	if guess < n:
		print("guess is low")
		guess = int(input("Enter an number from 1 to 100: "))
	elif guess > n:
		print("guess is high")
		guess = int(input("Enter an number from 1 to 100: "))
	else:
		print("CONGRATS! You got it right, would you like a cookie?")

		break

print('\033[92m' '\033[4m' '\033[1m')
choice = input(">")
if choice == "yes":
	print("to bad")

if choice == "Yes":
	print("*Gives cookie*")

if choice == "YES":
	print("Stop yelling")

if choice == "no":
	print("Whats wrong with you")

if choice == "No":
	print("Im not your friend anymore")

if choice == "NO":
	print("Stop yelling, my gosh")

if choice == "I dont like cookies":
	print("Go see a doctor")

if choice == "No thank you":
	print("Thanks for being polite *gives cookie*")

if choice == "Yes please":
	print("*gives 2 cookies*")

if choice == "nein":
	print("arschloch")

if choice == "e":
	print("E")

if choice == "E":
	print("E")

if choice == "ya":
	print("*starts to hand cookie then pulls back* Pranked")

if choice == "cookie":
	print("eikooc")

if choice == "Cookie":
	print("eikooC")

if choice == "Zoom":
	print("sucks")

if choice == "yes please":
	print("Capitalization is important, try again and you may get two cookies")

if choice == "YES PLEASE":
	print("To much capitalization friend, try again")

if choice == "nah man im good":
	print("k bro")

if choice == "No but can I have a cat?":
	print("──────▄▀▄─────▄▀▄")
	print("─────▄█░░▀▀▀▀▀░░█▄")
	print("─▄▄──█░░░░░░░░░░░█──▄▄")
	print("█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")

if choice == "Im to fat for a cookie":
	print("*gives cookie* Same")
if choice == "YELLS":
	print("Will you stop yelling if I give tou a cookie")

if choice == "YELLS AGAIN":
	print("Fine heres your cookie *gives cookie*")

if choice == "YELLS A THIRD TIME":
	print("*takes the cookie back and calls a living relative of yours*")

