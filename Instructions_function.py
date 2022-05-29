""""Instructions function for Maori quiz made by Samuel Burgess"""


# functions go here
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


def formatter(text, symbol):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def instructions():
    show_instructions = yes_no("Have you played this quiz before?: ")
    if show_instructions == "Yes":
        print(formatter("I hope you enjoy playing again!", "!"))
    else:
        print(formatter("Welcome to my Maori quiz!", "*"))
        print("In this quiz, you will be asked ten questions.")
        print("once the question has been asked, the program will wait for your answer")
        print()
        print("enter your answer without accents")
        print()
        print("you will then be told if you got the question correct or not")
        print("and you will be asked the next question")
        print()
        print("at the end of ten questions, you will be told your score")
        print()
        print("you will then be asked if you want to play again")
        print("at that point, if you enter 'x' the program will end")
        print("but if you enter anything else you can play again for a better score")
        print(formatter("enjoy", "!"))
        print("scroll up for instructions")


# main routine goes here
instructions()
