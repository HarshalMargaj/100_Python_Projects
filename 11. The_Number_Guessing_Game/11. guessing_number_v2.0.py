import random

from guessing_number_logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, num, turns):
    if guess < num:
        print("Too low")
        return turns - 1
    elif guess > num:
        print('Too high')
        return turns - 1
    else:
        print(f'You win, the answer is {num}')


def difficulty():
    level = input('Choose a difficulty: hard or easy? ')
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    print(logo)
    print('Welcome to the number guessing game')
    print('I am thinking a number between 1 to 100')
    num = random.randint(1, 100)
    turns = difficulty()

    guess = 0
    while guess != num:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, num, turns)

        if turns == 0:
            print('you loose, your chances are over')
        elif guess != num:
            print('Guess again')


game()
