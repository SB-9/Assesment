"""Maori quiz yes no checker version 1"""


# ask if user has tried this quiz before
show_instructions = input("Have you played this quiz before?: ")

# if input is yes, output is program continues
if show_instructions.lower() == "y":
    print("program continues")

# if input is no print instructions
elif show_instructions.lower() == "n":
    print("instructions")

# check for y/n
else:
    print("please enter y or n")
