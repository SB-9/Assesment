"""Maori quiz Yes no checker version 3 (for testing)"""

show_instructions = ""
while show_instructions != "x":
    # ask if user has played this quiz before
    show_instructions = input("Have you played this quiz before?: ")

    # check for unexpected inputs
    while show_instructions.lower() != "y" and show_instructions.lower() != "n":
        show_instructions = input("Please enter y or n: ")

    # check for yes
    if show_instructions.lower() == "y":
        print("continue program")

    # otherwise, show instructions
    else:
        print("instructions")
