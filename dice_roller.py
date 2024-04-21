# Import the random module to generate random numbers
import random

def roll_dice():
    """
    This function simulates rolling a dice and returns a random number between 1 and 6.
    """
    # Generate and return a random integer between 1 and 6 (inclusive)
    return random.randint(1, 6)

def main():
    """
    Main function to handle user interactions.
    """
    while True:
        # Ask the user if they want to roll the dice
        input_value = input("Do you want to roll the dice? (yes/no): ")
        
        # Check if the user wants to continue or not
        if input_value.lower() == 'yes':
            # If yes, roll the dice and display the result
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif input_value.lower() == 'no':
            # If no, break out of the loop to end the program
            print("Thank you for playing. Goodbye!")
            break
        else:
            # If the user inputs something other than 'yes' or 'no'
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
