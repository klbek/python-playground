from random import randint

print('You are guessing a number between 1 and 100.')
random_number = randint(1, 100)
guess_number = 0
count_attempt = 0

while random_number != guess_number:
    
    try:
        guess_number = int(input('Enter a number:\n'))
        if guess_number > random_number:
            print(f'Number is too large.\n{round(random_number/guess_number, 2)}% guess accuracy.\n')
        if guess_number < random_number:
            print(f'Number is too small.\n{round(guess_number/random_number, 2)}% guess accuracy.\n')
    except ValueError:
        print('Invalid input.\n')

    count_attempt += 1 # including invalid input

print(f'Right! Count attempt: {count_attempt}')
