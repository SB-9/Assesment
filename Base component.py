"""Base component for Maori quiz made by Samuel Burgess. Created on 9th March 2022."""


def welcome():
    print("Welcome to my Maori quiz!")
    name = input("What is your name?: ")
    while len(name) <= 1:
        name = input("please enter a name longer than 1 character: ")
    print(f"Welcome {name}, I hope you have a fun time playing my Quiz!")


def yes_no(question):
    # ask if user has played the quiz before
    answer = input(question)

    # check for unexpected inputs
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("Please enter y or n: ")

    # check for yes
    if answer.lower() == "y":
        return "Yes"

    # otherwise, show instructions
    else:
        return "No"


# Main routine
welcome()
show_instructions = yes_no("Have you played this quiz before")
