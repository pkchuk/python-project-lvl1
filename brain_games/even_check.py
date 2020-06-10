"""Check input numbers for even."""


import random

import prompt


def ask_and_check():  # noqa: WPS231
    """Ask about even's number. Returns true-correct answer, false - wrong."""
    rand_number = random.randint(1, 100)
    print('{0} {1}'.format('Question:', rand_number))
    answer = prompt.string('Your answer: ')
    wrong_answer = ' is wrong answer ;(. Correct answer was'
    correct_answer = 'Correct!'
    if rand_number % 2 == 0:  # noqa: WPS502
        number = True
    else:
        number = False
    if answer == 'yes' and rand_number % 2 == 0:
        print(correct_answer)
        return True
    elif answer == 'no' and rand_number % 2 != 0:
        print(correct_answer)
        return True
    elif answer != 'yes' and number is True:
        print("'{0}' {1} 'yes'".format(answer, wrong_answer))
        return False
    else:
        print("'{0}' {1} 'no'".format(answer, wrong_answer))  # noqa: WPS503
        return False  # noqa: WPS503


def count_answer():
    """Count for correct answer. Returns True for 3 correct answer."""
    correct_answer_count = 0
    while correct_answer_count < 3:
        if ask_and_check() is True:
            correct_answer_count += 1
        else:
            return False
    return True
