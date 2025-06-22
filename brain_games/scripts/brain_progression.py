from random import randint

from brain_games.scripts.get_name import get_name


def generate_progression():
    start = randint(1, 11)
    step = randint(2, 3)
    lenght = randint(5, 11)
    play_gen = [start + i * step for i in range(lenght)]
    hide_element = randint(0, lenght - 1)
    correct_answer = play_gen[hide_element]
    play_gen[hide_element] = ".."
    progression_str = " ".join(map(str, play_gen))
    return progression_str, int(correct_answer)

    
def main():
    name = get_name()
    for _ in range(3):
        progression_str, correct_answer = generate_progression()
        print(f'Question: {progression_str}')
        user_answer = int(input('Your answer: '))
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()