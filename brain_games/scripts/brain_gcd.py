#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user, name


def get_gcd(num1, num2):
    if num1 > num2:
        for i in range(int(num1 / 2), 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i
    return get_gcd(num2, num1)


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        print(f'Question: {number1} {number2}')
        answer = prompt.string('Your answer: ')
        correct = get_gcd(number1, number2)

        if str(answer) == str(correct):
            count += 1
            print('Correct!')
        else:
            count = 0
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
