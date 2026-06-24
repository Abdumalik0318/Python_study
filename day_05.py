import random

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess the secret number between 1 and 100: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Correct! You guesssed it in {attempts} attempts!")