import random

player = input("What is your name?")


print("Good luck", player)


names = ["Sage", 'Storm', 'Rogue', 'Wolverine', 'Nightcrawler', 'Magneto', 'Cyclops', 'Colossus', 'Beast', 'Gambit', 'Jean', 'Jubilee']

name = random.choice(names)

print("Guess the X-man")

guesses = ''

turns = 13

while turns > 0:

    failed = 0


    for char in name:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")

            failed += 1

    if failed == 0:
        print("Welcome to the x-men")

        print("The x-man is", name)
        break


    print()
    guess = input('Guess the x-man:')


    guesses += guess

    if guess not in name:
        turns -= 1

        print("Try again")


        print("You have", + turns, 'more guesses')

        if turns == 0:
            print('You lose')