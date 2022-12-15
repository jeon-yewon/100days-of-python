import art
import random

WELCOME_MESSAGE = """Welcome to the Number Guessing Game!
✨I'm thinking of a number between 1 and 100✨
Choose a difficulty. 
- easy : you get 10 attemp
- hard : you get 5 attemp
"""

def set_try_count():
    """
    get level information, 
    return try_count depends on level
    """
    level = input("Type 'easy' or 'hard' : ")
    
    if level == "hard":
        try_count = 5
    elif level == "easy":
        try_count = 10
    return try_count

def set_random_number():
    """
    return random int btw 1 ~ 100
    """
    return random.randint(1, 100)

def compare_number(guess_number, random_number):
    """
    compare guess_number & random_number
    print current status, return is_correct value
    """
    is_correct = False
    if guess_number == random_number:
        is_correct = True
    else:
        if guess_number > random_number:
            print("Too High")
        elif guess_number < random_number:
            print("Too Low")

    return is_correct

def run_game():
    random_number = set_random_number()
    try_count = set_try_count()

    game_end = False
    while not game_end:
        print(f"You have {try_count} attempts remaining to guess the number")
        guess_number = int(input("➡️ Make a Guess: "))
        is_correct = compare_number(guess_number, random_number)
        
        if is_correct == True:
            game_end = True
            print(f"You got it! The answer was {random_number} 👍👍👍")
        elif is_correct == False:
            try_count -= 1
            if try_count == 0:
                game_end = True
                print("You've run out of guesses, you lose 🥲")
            elif try_count != 0:
                print("Guess Again")


print(art.logo)
print(WELCOME_MESSAGE)
run_game()
