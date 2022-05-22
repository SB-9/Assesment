"""Maori quiz yes no checker trial 2"""


# ask if user has tried this quiz before
show_instructions = input("Have you played this quiz before?: ")

# instructions or continue program
if show_instructions.lower() == "y":
    print("continue program")
else:
    print("instructions")
