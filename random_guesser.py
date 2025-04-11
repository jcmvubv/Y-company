import random


range_top = input("Please enter a number: ")

if range_top.isdigit():
    range_top = int(range_top)
    if range_top <= 0:
        print("Please enter a number greater than 0 next time!")
        quit()
else:
    print("Please enter a number!")
    quit()

random_number = random.randint(0, range_top)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time!")
        continue

    if user_guess == random_number:
        print("You got it :) ************")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses")
