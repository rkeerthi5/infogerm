import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Set range for the random number
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        
        # Generate random number
        target_number = random.randint(lower_bound, upper_bound)
        attempts = 0
        
        print(f"Guess a number between {lower_bound} and {upper_bound}.")
        
        while True:
            try:
                # User input for guess
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess < target_number:
                    print("Too low, try again.")
                elif guess > target_number:
                    print("Too high, try again.")
                else:
                    print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

# Start the game
number_guessing_game()
