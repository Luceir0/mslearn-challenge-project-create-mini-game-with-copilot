
import random

valid_options = ["rock", "paper", "scissors"]
score = {"wins": 0, "losses": 0, "ties": 0}

while True:
    user_choice = input("Choose rock, paper, or scissors: ")
    if user_choice not in valid_options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    machine_choice = random.choice(valid_options)
    print(f"Machine chose {machine_choice}.")

    if user_choice == machine_choice:
        print("Tie!")
        score["ties"] += 1
    elif (user_choice == "rock" and machine_choice == "scissors") or \
         (user_choice == "paper" and machine_choice == "rock") or \
         (user_choice == "scissors" and machine_choice == "paper"):
        print("You won!")
        score["wins"] += 1
    else:
        print("You lost!")
        score["losses"] += 1

    print(f"Score: Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break

print(f"Final score: Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")
