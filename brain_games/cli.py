import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have you name? ')
    print(f'Hello, {name}')