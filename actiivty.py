import random

while True: 
    user_action = input("enter a chocie(rock, paper, scissors: )")
    possible = ["rock", "paper", "scissors"]

    computer = random.choice(possible)
    print(f"\nyou chose {user_action}, computer chose {computer}.\n")

    if user_action == computer:
        print("both players selected {user_action}. its a tie")

    elif user_action == "rock":
        if computer == "scissors":
            print("rock smashes scissors, You win!")

        else:
            print("paper covers rock, you lose")

    elif user_action == "scissors":
        if computer == "rock":
            print("rock beats scissors, you lose!")

        else:
            print("scissors beats paper, you win!")

    elif user_action == "paper":
        if computer == "rock":
            print("paper beats rock, you win!")

        else:
            print("scissors beats paper, you lose!")                      

    play_again = input("play again? (y/n)")              
    if play_again != "y":
        break