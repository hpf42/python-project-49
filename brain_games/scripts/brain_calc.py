#!/usr/bin/env python3

from random import choice, randint

from brain_games.scripts.get_name import get_name


def get_operation():
    operators = ['+', '-', '*']
    operator = choice(operators)
    number_1 = randint(1, 101)
    number_2 = randint(1, 101)
    result = f'{number_1} {operator} {number_2}'
    correct_answer = int(eval(result))
    return correct_answer, result


def main():
    name = get_name()
    print('What is the result of the of the expression?')
    for _ in range(3):
        correct_answer, result = get_operation()
        user_question = f'Question: {result}'
        print(user_question)
        user_answer = int(input('Yous answer: '))

        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f'{str(user_answer)} is wrong answer ;(. Correct answer was {str(correct_answer)}')
            print(f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()