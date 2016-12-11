from PyDictionary import PyDictionary
import random
import time
import os

# Python 2
# Description: This game quizzes you on your knowledge of GRE words, providing the definition
# and multiple choices for the answer. If you answer incorrectly in the advanced
# version, you are prompted to type the word 3x correctly.

# To download the PyDictionary module go to
# https://pypi.python.org/pypi/PyDictionary/1.5.2

class Data(object):
    """Contains all the data functions to display the answer, definition, and
    choices"""

    def __init__(self, words=None):
        if not words:
            self.words = self.collect_words()
        else:
            self.words = self.words
        self.lookup = PyDictionary()

    def collect_words(self, word_file="gre_game/gre_word_file.txt"):
        """Builds the word database"""
        with open(word_file) as wordlist:
            wordlist = wordlist.read().splitlines()
            return wordlist

    def display_words(self):
        """Test function to make sure self.collect_words() function worked correctly."""
        for word in self.words:
            print(word)

    def get_answer(self):
        """Chooses a random word from the wordlist and removes the word
        from the list to prevent repeats"""
        while True:
            try:
                answer_idx = random.randint(0, len(self.words) - 1)
            except Exception:
                print('Error retrieving word. Trying again...')
                continue
            break
        return self.words.pop(answer_idx).lower()


    def definition(self, answer):
        """Queries the definition of the answer"""
        while True:
            try:
                query = self.lookup.meaning(answer)
                break
            # If there's no result (NoneType)
            except TypeError:
                continue
        print('\nDefinition: \n')
        for definition in query:
            print(definition, '\n', ', '.join(query[definition]))
        print('-' * 75 + '\n')

    def choices(self,answer, num=False):
        """Builds a list consisting of the answer and 3 other random words"""
        my_choices = [answer]
        while len(my_choices) < 4:
            choice = random.choice(self.words)
            if choice not in my_choices:
                my_choices.append(choice)
        random.shuffle(my_choices)
        answer_idx = my_choices.index(answer)
        print('Choices:\n')
        if num:
            return enumerate(my_choices, start=1), answer_idx
        else:
            return my_choices

    def practice(self, answer):
        """Prompts user to type the answer 3x if the guess is incorrect within
        the hard version of the game"""
        print('Please type the answer 3x, each on its own line.\n')
        count = 0
        while count < 3:
            word = input('> ').lower()
            if word == answer:
                count += 1
            else:
                print('Make sure your spelling is correct.')
        print('\nExcellent!')


class Game(object):
    """This is the game engine that determines the workflow of the game"""
    def __init__(self):
        self.wins = 0
        self.attempts = 0
        self.data = Data()

    def clear_screen(self):
        """Clears the screen"""
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')
        else:
            # Fallback for other operating systems.
            print('\n' * numlines)

    def pretty_print(self, collection):
        for i in range(len(collection)):
            if i != len(collection) - 1:
                print(collection[i], end=', ')
            else:
                print(collection[i])

    def start(self):
        """Prompt to choose easy = number version or hard = word version."""
        self.clear_screen()
        self.game_on = True
        while self.game_on:
            self.reset_score()
            choice = input('Would you like the easy or hard version? \n').lower()
            if choice == 'easy':
                self.num_game()
            elif choice == 'hard':
                self.word_game()
            else:
                print('I don\'t know what that means.')

    def num_questions(self):
        """Prompts the user for the number of questions"""
        while True:
            try:
                num = int(input('How many questions would you like? (1-50) '))
            except Exception:
                print("That is not a valid number.")
                continue
            if num not in list(range(1,51)):
                print("Please choose a number between 1 and 50.")
            else:
                break
        return num

    def word_game(self):
        """Word game initializes"""
        num = self.num_questions()
        print('\nGiven the definition, type the correct word. You have one try', end=' ')
        'for each word.'
        input('\nPress Enter to start...')
        for i in range(num):
            time.sleep(2)
            self.clear_screen()
            answer = self.data.get_answer()
            self.data.definition(answer)
            # print(self.data.choices(answer))
            choices = self.data.choices(answer)
            self.pretty_print(choices)

            turns = 0
            while turns < 1:
                guess = input('\nAnswer: ')
                if guess.isdigit():
                    print("Please type the correct word as written.")
                elif guess == answer:
                    self.response(True)
                    self.wins += 1
                    break
                else:
                    self.response(False)
                    turns += 1
                    if turns == 1:
                        print('The answer was %s.' % answer)
                        self.data.practice(answer)
            self.attempts += 1
        self.end()

    def num_game(self):
        """Num game initalizes"""
        print('Given the definition, choose the correct number that', end=' ')
        print('corresponds to the word. \nYou have two tries.')
        num = self.num_questions()
        input('Press Enter to start...')
        for i in range(num):
            time.sleep(2)
            self.clear_screen()
            answer = self.data.get_answer()
            self.data.definition(answer)
            choices, answer_idx = self.data.choices(answer, num)
            for choice in choices:
                print(choice)

            turns = 0
            while turns < 2:
                try:
                    guess = int(input('\nAnswer: '))
                except Exception:
                    print('That is not a valid number.')
                    continue
                if guess == answer_idx + 1:
                    self.response(True)
                    self.wins += 1
                    break
                elif guess not in list(range(1, 5)):
                    print('Please choose a number between 1 and 4.')
                else:
                    self.response(False)
                    turns += 1
            if turns == 2:
                print('The answer was %s.' % answer)
            self.attempts += 1
        self.end()

    def end(self):
        """Game summary"""
        print('\nGame Over.\nYour score: %d/%d.' % (self.wins, self.attempts))
        if self.wins == self.attempts:
            print('Perfect!')
        print('-' * 10)
        self.game_on = False
        self.restart()

    def response(self, is_correct):
        if is_correct:
            print('Correct!')
            if os.name == 'posix':
                os.system('say Correct!&')
        else:
            print('Incorrect.')
            if os.name == 'posix':
                os.system('say Do not pass go!&')


    def restart(self):
        choice = ''
        while choice != 'Y' and choice != 'N':
            choice = input('Play again: Y or N? ').upper()
        if choice == 'Y':
            self.clear_screen()
            self.start()
        else:
            pass

    def reset_score(self):
        """Resets the score"""
        self.wins, self.attempts = 0, 0

game = Game()
if __name__=='__main__':
    game.start()
