import random


def main():
    level = get_level()
    problems_count = 0
    score = 0

    while problems_count < 10:
        wrong_answer_count = 0
        problems_count += 1
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y

        while wrong_answer_count < 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == sum:
                    score += 1
                    break
                else:
                    print('EEE')
                    wrong_answer_count += 1

            except ValueError:
                print('EEE')
                wrong_answer_count += 1

        if wrong_answer_count == 3:
            print(f'{x} + {y} = {sum}')
            pass

    print('Score:', score)


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input('Level: '))
            if level in levels:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        start = 0
    else:
        start = 10 ** (level - 1)
    end = (10 ** level)
    return random.randrange(start, end)


if __name__ == "__main__":
    main()