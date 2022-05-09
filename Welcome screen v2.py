"""Welcome screen component version 2. Made by Samuel Burgess"""

name = 0
print("Welcome to my Maori quiz!")
name = input("What is your name?: ")
while len(name) <= 1:
    name = input("please enter a name longer than 1 character: ")
