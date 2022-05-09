"""Welcome screen component version 3. Made by Samuel Burgess"""


def welcome():
    print("Welcome to my Maori quiz!")
    name = input("What is your name?: ")
    while len(name) <= 1:
        name = input("please enter a name longer than 1 character: ")
    print(f"Welcome {name}, I hope you have a fun time playing my Quiz!")


welcome()
