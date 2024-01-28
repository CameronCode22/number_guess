import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a value greater than zero next time")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time.")
        #goes back to input
        continue

    if guess == random_number:
        print("Congratulations you guessed it correct :)")
        #breaks out of the loop
        break
    elif guess > random_number:
        print("You were above the number!")
    else:
        print("you were below the number!")

print("you got it in", guesses, "guesses")


