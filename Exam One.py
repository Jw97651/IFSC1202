from random import randint
user_name = input("Please enter your name: ")
print(f"Hello, {user_name} , You have 5 tries to guess a number between 1 and 20.")
random_number = randint(1, 20)
for tries in range(1, 6):
    guess = int(input("Take a guess: "))
    if guess > random_number:
        print("Your guess is too high.")
    elif guess < random_number:
        print("Your guess is too low.")
    else:
        print(f"Congratulations, {user_name}! You guessed the number {random_number} in {tries} tries!")
        break
else:
    print(f"Sorry, {user_name}. Sorry, you lose. The number was {random_number}.")
