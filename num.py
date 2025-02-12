import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    random_number = random.randint(1, 100)  # CPU generates a random number between 1 and 100
    attempts = 5
    
    for attempt in range(attempts):
        try:
            user_guess = int(input(f"Attempt {attempt + 1}/{attempts}: Enter your guess (1-100): "))
            
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if user_guess == random_number:
                print("Congratulations! You won! 🎉")
                return
            else:
                print("Wrong guess! Try again.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f"You lose! The correct number was {random_number}.")

if __name__ == "__main__":
    number_guessing_game()
