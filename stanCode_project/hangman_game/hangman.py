"""
File: hangman.py
Name: Vanessa
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    To guess the random word. If user guess the correct alphabet included in the random word,
    the correct alphabet will replace the dashed line.
    If user guess wrong for 7 times, then the user will die.
    """
    answer = random_word()
    dashed = ''
    for i in range(len(answer)):
        # create the dashed word
        dashed += '-'
    print('The word look like: ' + dashed)
    print('You have 7 guesses left.')
    # guess: the chances that the user left
    guess = N_TURNS
    while True:
        input_ch = input('Your guess: ')
        if input_ch.isalpha() and (len(input_ch) == 1):
            # if the input is one alphabet
            # case-insensitive
            input_ch = input_ch.upper()
            # the number that input matches the random words
            ct = 0
            ans = ''
            for i in range(len(answer)):
                # create the new dashed word that include the correct guess
                if answer[i] == input_ch:
                    ans += answer[i]
                    ct += 1
                else:
                    ans += dashed[i]
            dashed = ans
            if ct != 0:
                # guess true
                print('You are correct!')
                if dashed != answer:
                    # still have the dash sign in the dashed (need to guess again)
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(guess) + ' guesses left.')
                else:
                    print('You win!!')
                    print('The word was: ' + answer)
                    break
            else:
                # guess wrong
                guess -= 1
                print('There is no ' + input_ch + "\'s in the word.")
                if guess == 0:
                    # No chance to guess again
                    print('You are completely hung : ( ')
                    print('The word was: ' + answer)
                    break
                else:
                    # still have chance to guess
                    print('The word looks like: ' + dashed)
                    print('You have ' + str(guess) + ' guesses left.')
        else:
            # the input is not one alphabet
            print('illegal format')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
