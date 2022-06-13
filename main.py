import random

comp_wins = 0
player_wins = 0


def Choose_Option():
    player_choice = input("Choose Rock, Paper or Scissors: ")

    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return player_choice


def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")

    player_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")

    if player_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")

        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    elif player_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1

        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")


        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif player_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1

        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    player_choice = input("Do you want to play again? (y/n)")
    if player_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif player_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
