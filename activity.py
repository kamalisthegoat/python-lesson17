import random
playing = True
number = str(random.randint(0,9))

print("i will generate a number from 0 to 9 and u have to guess the number one digit at a time")

print("the game ends when u get 1 hero")

while playing:
    guess = input("give me ur guess!:  \n")
    if number == guess:
        print("you win the game")
        print("the number was ",  number)
        break

    else:
        print("your guess isnt quite right,try again. \n")