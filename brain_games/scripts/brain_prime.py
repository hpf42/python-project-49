from random import randint

from brain_games.scripts.get_name import get_name


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    name = get_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = randint(1, 101)
        print(f'Question: {number}')
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if is_prime(number) else 'no'
        if user_answer == correct_answer:
            print('Correct!')
        else:
            ua, ca = user_answer, correct_answer
            print(f"{ua} is wrong answer ;(. Correct answer was {ca}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()