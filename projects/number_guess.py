import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You found the number in {attempts} attempts.")
            break

def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()