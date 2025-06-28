import random

choices = ["rock", "paper", "scissors"]


user_score = 0
computer_score = 0
round_number = 1

print(" Welcome to Rock, Paper, Scissors Game!")
print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

while True:
    print(f"\n--- Round {round_number} ---")
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print(" Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f" Computer chose: {computer_choice}")
    print(f" You chose: {user_choice}")

   
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = " You win this round!"
        user_score += 1
    else:
        result = " Computer wins this round!"
        computer_score += 1

    
    print(result)
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("\n Final Score:")
        print(f" You: {user_score}")
        print(f" Computer: {computer_score}")
        print("Thanks for playing! Goodbye! ")
        break

    round_number += 1
