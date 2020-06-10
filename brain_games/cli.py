"""Command line interface for brain-games."""


import prompt


def welcome_user():
    """Get an user name, promt user."""
    welcome_string = 'Welcome to the brain Brain Games!\n'
    print(welcome_string)
    name = prompt.string('May I have your name? ')
    print('{0}, {1}!'.format('Hello', name))
