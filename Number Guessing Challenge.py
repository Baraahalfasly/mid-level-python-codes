import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Your guess is too low, try a higher number.")
            elif guess > number_to_guess:
                print("Your guess is too high, try a lower number.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guessing_game()
