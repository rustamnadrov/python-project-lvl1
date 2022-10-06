#!/usr/bin/env python3
import prompt
from random import randrange
from brain_games.cli import welcome_user, name


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:
        random_number = randrange(100)

        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')

        if answer == 'yes' and is_prime(random_number):
            count += 1
            print('Correct!')
        elif answer == 'no' and not is_prime(random_number):
            count += 1
            print('Correct!')
        else:
            count = 0
            correct = 'yes'
            if answer == 'yes':
                correct = 'no'
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
