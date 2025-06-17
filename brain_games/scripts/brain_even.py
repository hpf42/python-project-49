from random import randint
import prompt


def is_even(number):
    return number % 2 == 0

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no"')

    correct_answers = 0

    while correct_answers < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your ansver: ").strip().lower()

        correct_answer = 'yes' if is_even(number) else 'no'

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer is 'no'.")
            print(f"Let's try again, {name}!")
            return  

    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()