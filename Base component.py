"""Base component for Maori quiz made by Samuel Burgess. Created on 9th March 2022."""


# Functions go here
def welcome():
    print(formatter("Welcome to my Maori quiz!", "*"))
    name = input("What is your name?: ")
    while len(name) <= 1:
        name = input("please enter a name longer than 1 character: ")
    print(formatter(f"Welcome {name}, I hope you have a fun time playing my Quiz!", "*"))


def formatter(text, symbol):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)

    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


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


def questions():
    # Setup answers
    answers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
    # Setup question numbers
    questions_ = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    # Setup round counter
    round_ = 0

    # Loop until ten questions are done
    for item in answers:
        # get user input
        user_answer = input(f"what is the Maori name for the number {questions_[round_]}?: ")
        # if correct tell the user
        if user_answer.lower() == answers[round_]:
            print(formatter("correct", "!"))
        # else tell the user incorrect
        else:
            print(formatter("incorrect", "-"))
        # add one to the round counter
        round_ += 1


def loop():
    # Setup variables
    playing = "l"

    # Question loop
    while playing.lower() != "x":
        questions()
        playing = input("Do you want to play again? ( 'x' to quit any other key to play again ):  ")


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


# Main routine
welcome()
instructions()
loop()
