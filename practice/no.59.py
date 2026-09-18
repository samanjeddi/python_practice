import random

def win(computer_number, guess):
    return computer_number == guess

def answer(computer_number, guess):
    if computer_number > guess:
        return "my number is larger..."
    if computer_number < guess:
            return "my number is smaller..."
    return "wow...you won"

def get_a_guess():
     result = int(input("guess a number between 1 to 20: "))
     return result

computer_number = random.randint(1, 20)
guess = 0

while (not win(computer_number, guess)):
     guess = get_a_guess()
     print(answer(computer_number, guess))