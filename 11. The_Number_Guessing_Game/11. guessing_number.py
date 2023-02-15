import random

from guessing_number_logo import logo

print(logo)
print("Welcome to The Guess Number Game")


def play_again():
    num = random.randint(1, 100)
    print("I am thinking of a number between 1 to 100")
    difficulty = input('Choose a difficulty: hard or easy? ').lower()
    end_of_the_game = False

    if difficulty != 'hard' and difficulty != 'easy':
        end_of_the_game = True
        print('Choose between hard or easy')

    attempts = 10
    if difficulty == 'hard':
        attempts = 5

    while not end_of_the_game:

        print(f"you have {attempts} attempts remaining to guess the number")

        guess = int(input('Make a guess: '))

        if guess < num:
            print('too low')
            attempts -= 1
        elif guess > num:
            print('too high')
            attempts -= 1
        else:
            end_of_the_game = True
            print(f'you win, the answer is {num}')

        if attempts == 0:
            end_of_the_game = True
            print("you loose, your chances are over")
        elif guess != num:
            print('Guess again')

    if input('Do you want to play again? yes or no? ') == 'yes':
        play_again()
    else:
        end_of_the_game = True


play_again()
