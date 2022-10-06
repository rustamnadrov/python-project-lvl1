#!/usr/bin/env python3
import prompt
from random import randrange
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('What is the result of the expression?')

    symbols = ['+', '-', '*']
    count = 0
    while count < 3:
        number1 = randrange(100)
        number2 = randrange(100)
        symbol = symbols[randrange(len(symbols))]

        print(f'Question: {number1} {symbol} {number2}')
        answer = prompt.string('Your answer: ')
        correct_answers = {
            '+': number1 + number2,
            '-': number1 - number2,
            '*': number1 * number2
        }
        correct = correct_answers[symbol]

        if str(answer) == str(correct):
            count += 1
            print('Correct!')
        else:
            count = 0
            print(f"{answer} is wrong answer ;(. Correct answer was {correct}.")
            print("Let's try again, Sam!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
