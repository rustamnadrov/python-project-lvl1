#!/usr/bin/env python3
import prompt
from random import randrange, randint
from brain_games.cli import welcome_user, name


def make_progression():
    progression = []
    step = randrange(20)
    first_number = randrange(20)
    progression.append(str(first_number))

    while len(progression) <= randint(5, 20):
        progression.append(str(first_number + step))
        first_number += step

    hidden_index = randrange(len(progression))
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    return (progression, correct_answer)


def main():
    welcome_user()
    print('What number is missing in the progression?')

    count = 0
    while count < 3:
        progression, correct_answer = make_progression()

        print(f"Question: {' '.join(progression)}")
        answer = prompt.string('Your answer: ')

        if str(answer) == str(correct_answer):
            count += 1
            print('Correct!')
        else:
            count += 0
            print(f"{answer} is wrong answer ;(. \
Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
