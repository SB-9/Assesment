"""second version of the question component for Maori quiz, made by Samuel Burgess"""

# Setup answers
answers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
# Setup question numbers
questions = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
# Setup round counter
round_ = 0

# Loop until ten questions are done
for item in answers:
    # get user input
    user_answer = input(f"what is the Maori name for the number {questions[round_]}?: ")
    # if correct tell the user
    if user_answer.lower() == answers[round_]:
        print("correct")
    # else tell the user incorrect
    else:
        print("incorrect")
    # add one to the round counter
    round_ += 1

