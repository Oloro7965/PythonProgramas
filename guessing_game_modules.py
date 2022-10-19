import random
def menu():
    print('Welcome to the guessing game. Please type a number for me to pick a number on the range from 1 to it and try to guess')
    number=int(input('type a number '))
    guess(number)
def guess(x):
    random_number=random.randint(1,x)
    attempts=0
    while True:
        user_number=int(input('try guessing the number I chose '))
        attempts += 1
        if user_number==random_number:
            break
        print('wrong number,try again ')
    print(f'you guessed it right after {attempts} attempts')


