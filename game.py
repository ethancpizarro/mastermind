# libraries
import random
import time

# colors used for guesses
COLORS = ["R", "G", "B", "Y", "W", "O"]

'''
generate_code

generates a random code to be guessed
inputs: none
outputs: code - the correct code for the player to guess
'''
def generate_code():
    code = []

    # pick CODE_LENGTH random colors for the code to guess
    for _ in range(code_length):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

'''
guess_code

requests a guess from the player and handles it for other functions
inputs: none
outputs: guess - the processed guess for use by other functions
'''
def guess_code():
    # keep asking for guesses until a valid one is made
    while True:
        guess = input("Guess: ").upper().split(" ")

        # length of guess is not the same as the code length
        if len(guess) != code_length:
            print(f"You must guess {code_length} color(s).")
            continue

        # invalid color detection
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
        
        else:
            break
    
    return guess

'''
check_code

checks the player's guess against the answer code
inputs: guess - the guess received from the player
        real_code - the answer code generated at the start of the game
outputs: correct_pos - the amount of colors in the correct position from the guess
         incorrect_pos - the amount of colors in the incorrect position from the guess
'''
def check_code(guess, real_code):
    # constants for tracking amount of each color and the return values
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # count number of each color in the real code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    # check for colors in the right position from the guess
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    # check for colors in the wrong position, but still in real code from the guess
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

'''
game

handles the game logic
inputs: none
outputs: none
'''
def game():
    # list the number of tries given, the length of the code, valid colors, and guess format
    print(f"You have {tries} tries to guess the code of {code_length} color(s).")
    time.sleep(1)
    print("The valid colors are", *COLORS)
    time.sleep(1)
    print("Please enter your guess with each color separated by a space, i.e. \"R G B Y\" ")
    time.sleep(1)

    # generate code and let player guess until tries run out
    code = generate_code()
    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        # end game when correct answer is given
        if correct_pos == code_length:
            print(f"You guessed the code in {attempts} tries!")
            break

        # print no. of colors in correct position and no. of colors in incorrect position
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    
    # lose condition
    else:
        print("You ran out of tries! The code was", *code)

'''
settings

handles changing settings
inputs: none
outputs: none
'''

def settings():
    while True:
        print("1: Tries")
        time.sleep(0.5)
        print("2: Code Length")
        time.sleep(0.5)
        print("3: Reset to Defaults")
        time.sleep(0.5)
        print("4: Go Back")
        time.sleep(0.5)
        choice = input("Choose a setting you would like to change: ")

        # set no. of tries
        if choice == "1":
            global tries
            tries = int(input("Enter the number of tries you want to change to (default - 10): "))
        # set the length of the real code
        elif choice == "2":
            global code_length
            code_length = int(input("Enter the code length you want to change to (default - 4): "))
        # reset tries and code length to defaults
        elif choice == "3":
            tries = 10
            code_length = 4
            print("Tries and Code Length set to defaults")
        # go back to main menu
        elif choice == "4":
            break
        # invalid choice handling, repeats question
        else:
            print("Invalid choice!")
'''
main

processes both settings and how many times the player wants to play the game
inputs: none
outputs: none
'''
if __name__ == "__main__":
    # set global variables
    global tries
    tries = 10
    global code_length
    code_length = 4

    print("Welcome to Mastermind! Guess the code in the allotted amount of tries!")
    time.sleep(0.5)

    # allow players to play or change settings until they want to exit
    while True:
        print("1: Play")
        time.sleep(0.5)
        print("2: Settings")
        time.sleep(0.5)
        print("3: Exit")
        time.sleep(0.5)
        choice = input("Choose an option: ")
        
        # plays the game
        if choice == "1":
            game()
        # goes to settings menu
        elif choice == "2":
            settings()
        # exit the game
        elif choice == "3":
            break
        # invalid choice handling, repeats question
        else:
            print("Invalid choice!")
            time.sleep(0.5)