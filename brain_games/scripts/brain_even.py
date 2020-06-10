#!/usr/bin/env python3
"""That script is a game checking for an even of inputs numbers."""
import prompt

from brain_games import even_check


def main():
    """Promt user, check input numbers for even."""
    welcome_string = 'Welcome to the Brain Games!'
    rules_string = 'Answer "yes" if number even otherwise answer "no"'
    win_game_string = 'Congratulations'
    lose_game_string = "Let's try again"

    print('{0}\n{1}\n'.format(welcome_string, rules_string))

    user_name = prompt.string('May I have your name? ')
    print('{0}, {1}!\n'.format('Hello', user_name))

    if even_check.count_answer() is True:
        print('{0}, {1}!'.format(win_game_string, user_name))
    else:
        print('{0}, {1}!'.format(lose_game_string, user_name))


if __name__ == '__main__':
    main()
