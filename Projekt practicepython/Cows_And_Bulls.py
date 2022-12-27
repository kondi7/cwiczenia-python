import random


def compare_numbers(number, user_guess):
    cowbulls = [0, 0]
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbulls[1] += 1
        else:
            cowbulls[0] += 1
    return cowbulls


if __name__ == "__main__":
    number = str(random.randint(1000, 9998))
    print(number)
    playing = True
    guesses = 0
    while playing:
        user_guess = input("Give me your 4 digit number guess! >>> ")
        if user_guess == "exit":
            break

        cowbullcount = compare_numbers(number, user_guess)
        guesses += 1

        print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1] == 4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was " + str(number))
            break  # redundant exit
        else:
            print("Your guess isn't quite right, try again.")
