# Python 3
import random
import sys
import os

# Pseudocode

# Choose random word in database
# Scramble the letters
# Compare with original word

# Code

def clear_screen(numlines=100):
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)

def start():
    clear_screen()
    print('Welcome to Unscrambler!\n\nGiven 3 turns, try to unscramble the word',
    'given.\nTo rescramble the word, press Enter with no input given.')
    game()

def set_difficulty():
    difficulty = ['easy', 'normal', 'hard']
    choice = ''
    while choice not in difficulty:
        choice = input('Easy, normal, or hard? ').lower()
    return choice

def create_word_list(difficulty):
    word_list = []
    with open('unscrambler/words.txt') as words:
        words = words.read().splitlines()
        for word in words:
            if difficulty == 'easy':
                if len(word) >= 4 and len(word) <= 5:
                    word_list.append(word)
            elif difficulty == 'normal':
                if len(word) >= 4 and len(word) <= 6:
                    word_list.append(word)
            else:
                if len(word) >= 5:
                    word_list.append(word)
    return word_list

def choose_number_of_questions():
    number = 0
    while number == 0:
        try:
            number = int(input('Number of questions: '))
        except Exception:
            print('Please type in a valid number.')
    return number

def choose_random_word(wordlist):
    random_word = random.choice(wordlist)
    wordlist.remove(random_word)
    return random_word

def scramble_word(word):
    scrambled = word
    # Prevents scrambled from becoming word
    while word == scrambled:
        my_list = list(word)
        scrambled = random.shuffle(my_list)
        scrambled = ''.join(my_list)
    return scrambled.upper()


def is_correct(guess, answer):
    if guess.upper() == answer.upper():
        return True
    else:
        return False

def play_again():
    choice = ''
    while choice != 'Y' and choice != 'N':
        choice = input('Play again: Y or N? ').upper()
    if choice == 'Y':
        clear_screen()
        game()
    else:
        pass

def game():
    difficulty = set_difficulty()
    wordlist = create_word_list(difficulty)
    num_questions = choose_number_of_questions()
    correct = 0
    attempts = num_questions
    for i in range(num_questions):
        answer = choose_random_word(wordlist)
        scrambled = scramble_word(answer)
        print('\n' + scrambled)
        turns = 3
        while turns > 0:
            guess = input('Guess: ')
            if is_correct(guess, answer):
                print('\nCorrect!')
                correct += 1
                break
            elif not guess:
                print('\n' + scramble_word(answer))
            else:
                print('Incorrect.')
                turns -= 1
                if turns == 0:
                    print('The answer was {}.'.format(answer))
    print('\nYour score was: {0}/{1}.\nGame over.'.format(correct,attempts))
    play_again()

if __name__ == '__main__':
    start()
