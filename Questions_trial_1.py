"""First trial of the question component for Maori quiz, made by Samuel Burgess"""

answers = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]
questions = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
num = 0

for item in answers:
    user_answer = input(f"what is the Maori name for the number {questions[num]}?: ")
    if user_answer.lower() == answers[num]:
        print("correct")
    else:
        print("incorrect")
    num += 1

