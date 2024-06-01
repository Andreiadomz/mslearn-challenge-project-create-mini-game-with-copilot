# Help me create a multiplayer game of rock, paper, scissors in which my opponent is the computer.
# The interaction should be in the terminal.
# The player should be able to choose between rock, paper, and scissors, and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed of the result of the round.
# By the end of each round, the player should be able to choose whether to continue playing or not.
# Display the player's score and the computer's score at the end of the game.
# The game must handle user inputs, putting them in lowercase, and informing the user if they entered an invalid option.
# Implement this in python.

import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid option. Please try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    total_rounds = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "You win!":
            user_score += 1
        elif winner == "Computer wins!":
            computer_score += 1
        total_rounds += 1
        print(winner)
        print(f"Scores: Player - {user_score}, Computer - {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Game ended. Total rounds: {total_rounds}. Player wins: {user_score}. Computer wins: {computer_score}.")
            break

if __name__ == "__main__":
    play_game()














