from random import randint
import sys

print('''***WELCOME TO ROCK PAPER SCISSORS***
      ROCK SMASHES SCISSORS
      PAPER COVERS ROCK
      SCISSORS CUT PAPER''')


def numbers_to_strings(choice):
    switcher = {
        1: "Rock",
        2: "Paper",
        3: "Scissor",
        4: "Exit"
    }
    return switcher.get(choice)


def exit_game():
    if player == "Exit":
        print("Bye Bye 😊")
        sys.exit()


def game():
    if computer == player:
        print("Tie!")
    elif (computer == "Rock" and player == "Scissor") or (computer == "Paper" and player == "Rock") or (
            computer == "Scissors" and player == "Paper"):
        print("Computer Wins")
    else:
        print("Player Wins")


while True:
    p_choice = int(input("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n 4. Exit "))
    while (p_choice < 1) or (p_choice > 4):
        print("INVALID NUMBER!!! PLEASE ENTER A NUMBER BETWEEN 1-4")
        p_choice = int(input("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n 4. Exit "))
    player = numbers_to_strings(p_choice)
    exit_game()
    c_choice = randint(1, 4)
    computer = numbers_to_strings(c_choice)
    print(f"Computer: {computer}")
    print(f"Player: {player}")
    game()
