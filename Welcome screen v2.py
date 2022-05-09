"""Welcome screen component version 2. Made by Samuel Burgess"""

# Setup name variable
name = 0
# welcome the user
print("Welcome to my Maori quiz!")
# ask the user for their name
name = input("What is your name?: ")
# check for invalid responses
while len(name) <= 1:
    name = input("please enter a name longer than 1 character: ")
