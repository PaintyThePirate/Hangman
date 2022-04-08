import random

wins = 0
loses = 0
print("Welcome to hangman.\n\n\n\n")


def random_word(word):
    word_bank = ["Jazz", "Pudding", "Sofa", "Pixel", "Trophy", "Python", "Cucumber", "Orange", "Hyper", "Computer",
                 "Dice", "Electrolyte", "Turnip", "Fallacy", "Battery", "Quandary", "Descent", "Power", "House",
                 "Mainframe", "Dillusion", "Sanctuary", "Rat", "Cream", "Locomotive", "Guitar", "Quarter", "Nickle",
                 "Iron", "Sword", "Tableture", "Whiskey", "Xylophone", "Trumpet", "Pizza"]
    random_word = random.randint(0, len(word_bank) - 1)
    answer = word_bank[random_word]
    # print(word_bank)
    return (answer)


def show_hangman(incorrect_guess):
    if incorrect_guess == 0:
        print("_____\n|   |\n|\n|\n|\n|____\n")
    elif incorrect_guess == 1:
        print("_____\n|   |\n|   0\n|\n|\n|____\n")
    elif incorrect_guess == 2:
        print("_____\n|   |\n|   0\n|   |\n|\n|____\n")
    elif incorrect_guess == 3:
        print("_____\n|   |\n|   0\n|  /|\n|\n|____\n")
    elif incorrect_guess == 4:
        print("_____\n|   |\n|   0\n|  /|\ \n|\n|____\n")
    elif incorrect_guess == 5:
        print("_____\n|   |\n|   0\n|  /|\ \n|  / \n|____\n")
    else:
        print("_____\n|   |\n|   0\n|  /|\ \n|  / \ \n|____\n")


# Global variables defined in reset_game function so they can be easily reset later to restart the game.
def reset_game():
    global current_word
    current_word = random_word("")
    global current_word_lower
    current_word_lower = current_word.lower()
    global display
    display = ("_" * len(current_word))
    print("\n")
    print(display)

    global game_active
    game_active = True
    # The maximum number of mistakes players can make.
    global max_incorrect
    max_incorrect = 6
    global incorrect_guess
    incorrect_guess = 0
    global previous_guesses
    previous_guesses = ""
    global previous_guesses_incorrect
    previous_guesses_incorrect = ""

    # Compare score with number of letters in word. If == then player has one.
    global score
    score = 0
    global game_round
    game_round = 0
    # If the word is a phrase or otherwise contains a space begin with the spaces blanked out by default and adjust score accordingly.

    if current_word_lower.find(" ") != -1:
        # Find ' ' location in string.
        score = score + current_word_lower.count(" ")
        for letters in range(current_word_lower.count(" ")):
            letter_location = current_word_lower.find(" ")
            # modify the ____ to show ' ' instead of '_'
            display = display[:letter_location] + " " + display[letter_location + 1:]
            # Replace spaces with _ to avoid conflicts if the player enters ' ' as an answer.
            current_word_lower = current_word_lower[:letter_location] + "_" + current_word_lower[letter_location + 1:]
            # add current guess to previous_guesses to inform the player they already guessed that letter.

    print(f"Current wins: {wins}\nCurrent loses: {loses}\n")


def endgame():
    x = False
    while x == False:
        endgame_response = input("Would you like to play again? y/n\n>")
        endgame_response = endgame_response.lower()
        if endgame_response == "y":
            reset_game()
            x = True
        elif endgame_response == "n":
            print("Thank you for playing.\n")
            x = True
            global game_active
            game_active = False
        else:
            print("Input invalid\n")


# Calls reset_game function to set the game to beginning state.

reset_game()

while game_active == True:
    game_round += 1



    input_invalid = True
    while input_invalid == True:
        show_hangman(incorrect_guess)
        print(display)
        if game_round > 1:
            print(f"Previous guesses: {previous_guesses_incorrect}")

        guess = str(input("Input Guess\n>"))
        if len(guess) > 1:
            print("Please only enter a single character.")
            input_invalid = True
        else:
            guess = guess.lower()
            input_invalid = False

    # Verify if letter is in word.
    if current_word_lower.find(guess) != -1:
        # .find finds location in string.
        previous_guesses = previous_guesses + guess + " "
        score = score + current_word_lower.count(guess)
        for letters in range(current_word_lower.count(guess)):
            letter_location = current_word_lower.find(guess)
            # modify the ____ display to show the correctly guessed letters.
            display = display[:letter_location] + guess + display[letter_location + 1:]
            # append current_word_lower so that the letter no longer shows up as a correct answer.
            current_word_lower = current_word_lower[:letter_location] + "_" + current_word_lower[letter_location + 1:]
            # add current guess to previous_guesses to inform the player they already guessed that letter.

        if score == len(current_word):
            print("YOU WON!!!")
            wins += 1
            endgame()

        else:
            print("Correct!")
            # show_hangman(incorrect_guess)
            # print(display)
    elif previous_guesses.find(guess) != -1:
        print(f"You already guessed {guess}!!!")
    else:
        incorrect_guess += 1
        previous_guesses_incorrect = previous_guesses_incorrect + guess + " "
        previous_guesses = previous_guesses + guess + " "
        show_hangman(incorrect_guess)
        # If incorrect_guess is equal to max incorrect guesses intitate endgame state in which player is prompted to reset the game.
        if incorrect_guess == max_incorrect:
            print(f"YOU LOST!\nThe answer was: {current_word}\n")
            loses += 1
            endgame()

        else:

            print(
                f"Sorry, there is no '{guess}' in the word. You have {max_incorrect - incorrect_guess} mistakes left.")