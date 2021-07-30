import random
import sys

while True:

    flag = True

    while flag:

        num = input("Please type upper bound limit of random numbers: ")

        if num.isdigit():
            print("Let's play!")
            num = int(num)
            flag = False
        else:
            print("Invalid input! Please enter a number. Try again!")

    secret = random.randint(1, num)

    guess = None
    count = 1

    while guess != secret:
        guess = input("Please type a number between 1 and " + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)
            if guess == secret:
                print("You got it!")
            else:
                if (secret - 5) <= guess and guess < secret:
                    print("Close. Too little.")
                    count += 1
                elif (secret + 5) >= guess and guess > secret:
                    print("Close. Too much.")
                    count += 1
                else:
                    print("Not close.")
                    count += 1

    print("It took you " + str(count) + " guesses.")

    play_again = True
    while play_again:
        again = input("Would you like to play again: ")
        if again == "No":
            raise sys.exit()
            play_again = False
