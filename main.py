import random


def roll_dice():
    # Generate a random number between 1 and 6 (inclusive)
    dice_roll = random.randint(1, 6)
    return dice_roll


def play_game():
    player1_name = input("Enter player 1's name: ")
    player2_name = input("Enter player 2's name: ")

    player1_roll = roll_dice()
    player2_roll = roll_dice()

    print(f"{player1_name} rolled a {player1_roll}!")
    print(f"{player2_name} rolled a {player2_roll}!")

    if player1_roll > player2_roll:
        print(f"{player1_name} wins!")
    elif player1_roll < player2_roll:
        print(f"{player2_name} wins!")
    else:
        print("It's a tie!")



while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
