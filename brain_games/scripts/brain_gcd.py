#!/usr/bin/env python3

from random import randint

from math import gcd

from brain_games.scripts.get_name import get_name


def main():
    name = get_name()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        number_1 = randint(1, 101)
        number_2 = randint(1, 101)
        correct_answer = int(gcd(number_1, number_2))
        print(f'Question: {number_1} {number_2}')
        user_answer = int(input('Your answer: '))
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f'{str(user_answer)} is wrong answer ;(. Correct answer was {str(correct_answer)}')
            print(f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}')


if __name__ == '__main__()':
    main()