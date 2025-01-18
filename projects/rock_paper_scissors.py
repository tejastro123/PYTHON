
import random

def get_computer_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

def get_user_move():
    while True:
        user_move = input("Enter your move (rock, paper, or scissors): ").lower()
        if user_move in ["rock", "paper", "scissors"]:
            return user_move
        else:
            print("Invalid move. Please try again.")

def determine_winner(computer_move, user_move):
    if computer_move == user_move:
        return "It's a tie!"
    elif (computer_move == "rock" and user_move == "scissors") or \
         (computer_move == "scissors" and user_move == "paper") or \
         (computer_move == "paper" and user_move == "rock"):
        return "Computer wins!"
    else:
        return "User wins!"

def play_game():
    computer_move = get_computer_move()
    user_move = get_user_move()

    print(f"Computer chose {computer_move}")
    print(f"User chose {user_move}")

    print(determine_winner(computer_move, user_move))

def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()