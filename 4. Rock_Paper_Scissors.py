# Rock Paper scissors
import random

import pyttsx3

engine = pyttsx3.init()
engine.say('Welcome to Rock Paper Scissors️')
print('Welcome to Rock👊 Paper✋ Scissors✌️')
engine.say('3 Simple Rules')
print('*********3 Simple Rules**********')
engine.say('''
1. Rock wins against scissors.
2. Scissors wins against paper.
3. Paper wins against rock.
''')
print('''
1. Rock wins against scissors.
2. Scissors wins against paper.
3. Paper wins against rock.
''')
engine.runAndWait()

while True:
    your_chance = int(input('What do you choose: 0 for rock, 1 for paper, 2 for scissors? '))

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    print('You choose: ')
    rps = [rock, paper, scissors]
    user = rps[your_chance]
    print(user)

    print('Computer choose: ')
    random_rps = random.choice(rps)
    print(random_rps)

    if (user == rock and random_rps == scissors) or (user == scissors and random_rps == paper) or (
            user == paper and random_rps == rock):
        engine.say('You win')
        print('✅ You win ✅')
    elif (user == rock and random_rps == rock) or (user == scissors and random_rps == scissors) or (
            user == paper and random_rps == paper):
        engine.say('No result')
        print('No Result')
    else:
        engine.say('You lose')
        print('❌ You lose ❌')

    engine.runAndWait()
    continue
