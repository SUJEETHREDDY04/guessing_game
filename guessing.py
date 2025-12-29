import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
guess = 0
attempts = 0
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
