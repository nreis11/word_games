# /usr/local/bin/Python3

from wordhoard import Synonyms
import time
import random
import sys

wins = attempts = 0
SYN_LOOKUP = Synonyms
WORD_FILE_LOC = "password/wordlist.txt"
NUM_CLUES = 3

def create_word_list():
    wordlist = open(WORD_FILE_LOC).read().splitlines()
    words = []
    for word in wordlist:
        if len(word) > 3:
            words.append(word)
    random.shuffle(words)
    return words

def restart():
    choice = input("Play again: Y or N? ").strip().lower()
    if choice == "y":
        game()
    elif choice == "n":
        sys.exit()
    else:
        print("I don't know what that means.")
        restart()

def get_clues(password):
    syn = SYN_LOOKUP(search_string=password)
    return syn.find_synonyms()

def game():
    global attempts, wins
    idx = 0
    password = None
    clues = None
    while clues is None:
        password = words.pop()
        clues = get_clues(password)

    while idx < NUM_CLUES:
        clue = clues[idx]
        now = time.time()
        future = now + 10
        print("\nClue: " + clue)
        guess = input("Guess: ").lower()
        if guess == password or guess + "s" == password or guess == password[:-3]:
            print("\nCorrect!")
            wins += 1
            break
        elif now > future:
            print(f"You ran out of time! The password was {password}.")
            break
        else:
            print("\nIncorrect")
            idx += 1
            if idx == NUM_CLUES:
                print(f"\nThe password was {password}.")

    attempts += 1
    print("Game over. Your score was %d / %d." % (wins, attempts))
    print("-" * 10)
    restart()


def start():
    print(
        "\nWelcome to Password. Given 3 clues, try to guess",
        "the word. You have 10 seconds to respond to each clue. Good luck!\n",
    )
    delay = input("Press Return or Enter to continue...")
    game()


if __name__ == "__main__":
    words = create_word_list()
    start()
