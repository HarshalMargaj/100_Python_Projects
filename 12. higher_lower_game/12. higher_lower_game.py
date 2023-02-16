import os
import random

from higher_lower_data import data
from higher_lower_logo import logo, vs


def get_random_account():
    return random.choice(data)


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f'{account_name}, a {account_description}, from {account_country}'


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    account_b = get_random_account()
    should_continue = True

    while should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input('Who has more followers? A or B: ').lower()

        a_follower = account_a["follower_count"]
        b_follower = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower, b_follower)

        os.system('clear')
        print(logo)

        if is_correct:
            score += 1
            print(f'you are right, your score is {score}.')
        else:
            should_continue = False
            print(f'you are wrong, final score is {score}.')


game()