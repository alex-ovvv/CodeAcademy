# простая игра, где вам предстоит загадывать число, которое должно равняться сумме двух бросков костей компьютером. Если угадали - победили, если нет - то нет
from random import randint
from time import sleep


def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print ("Max val is %d" % max_val)
    guess = get_user_guess()
    if guess > max_val:
        print ("It is not right!!")
        return
    else:
        print ("Rolling...")
        sleep(2)
        print ("The 1-st roll is: %d" % first_roll)
        sleep(1)
        print ("The 2-nd roll is: %d" % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print ("Result...")
        sleep(1)
        if total_roll == guess:
            print ("Great job!")
        else:
            print ("Looooser")


roll_dice(6)