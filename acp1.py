import random
playing = True
number = random.randint(1, 60)

print("this is a numer guessing game, guess the number i chose")
print("guess a number between 1 and 60")

while playing:
    gues = int(input("Enter your guess: "))

    if gues < number:
        print("too low")

    elif gues > number:
        print("too high")

    else:
        print("you guessed the number.you winnn")
        break