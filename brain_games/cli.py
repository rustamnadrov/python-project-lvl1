import prompt

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}!')
