import random

while True:
    try:
        n = int(input('Level: '))
        if n < 0:
            pass
        else:
            r = random.randrange(1, n)
            while True:
                try:
                    guess = int(input('Guess: '))
                    if guess < 0:
                        pass
                    elif guess < r:
                        print('Too small!')
                    elif guess > r:
                        print('Too large!')
                    elif guess == r:
                        print('Just right!')
                        break
                except ValueError:
                    pass
            break

    except ValueError:
        pass