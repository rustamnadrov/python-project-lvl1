#!/usr/bin/env python3
import prompt
from random import randrange
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        number = randrange(100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if answer == 'yes' and number % 2 == 0:
            count += 1
            print('Correct!')
        elif answer == 'no' and number % 2 != 0:
            count += 1
            print('Correct!')
        elif answer not in ['yes', 'no']:
            count = 0
            print('Answer "yes" if the number is even, otherwise answer "no".')
        else:
            count = 0
            correct = 'no'
            if answer == 'no':
                correct = 'yes'
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
