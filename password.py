#/usr/local/bin/Python3

from PyDictionary import PyDictionary
import time
import random
import os

# TO DO!
# Install PyDictionary for Python 3

# To download the PyDictionary module go to
# https://pypi.python.org/pypi/PyDictionary/1.5.2

def create_word_list():
    word_file = "password/wordlist.txt"
    wordlist = open(word_file).read().splitlines()
    words = []
    for word in wordlist:
        if len(word) > 3:
            words.append(word)
    return words

wins, attempts = 0, 0

def restart():
    choice = ''
    while choice != 'y' and choice != 'n':
        choice = input('\nPlay again: Y or N? ').lower()
    if choice == 'y':
        game()

def game():
    words = create_word_list()
    lookup = PyDictionary()
    global attempts, wins
    idx = 0
    answer = random.choice(words)
    while idx < 3:
        clue = lookup.synonym(answer)[idx]
        now = time.time()
        future = now + 10
        print('\nClue: ' + clue)
        guess = input('Guess: ').lower()
        if guess == answer or guess + 's' == answer or guess == answer[:-3]:
            print("\nCorrect!")
            wins += 1
            break
        elif now > future:
            print("You ran out of time! The answer was %s." % answer)
            break
        else:
            print("\nWrong.")
            idx += 1
            if idx == 3:
                print("\nThe answer was %s." % answer)

    attempts += 1
    print("Game over. Your score was %d / %d." % (wins, attempts))
    print('-' * 10)
    words.remove(answer)
    restart()

def start():
    print("\nWelcome to Password. Given 3 clues, try to guess",
    "the word. You have 10 seconds to respond to each clue. Good luck!")
    delay = input('Press any key to continue...')
    game()

if __name__ == '__main__':
    start()
