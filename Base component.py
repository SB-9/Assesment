"""Base component for Maori quiz made by Samuel Burgess. Created on 9th March 2022."""


def welcome():
    print("Welcome to my Maori quiz!")
    name = input("What is your name?: ")
    while len(name) <= 1:
        name = input("please enter a name longer than 1 character: ")
    print(f"Welcome {name}, I hope you have a fun time playing my Quiz!")


# Main routine
welcome()
