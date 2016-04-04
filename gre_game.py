from PyDictionary import PyDictionary
import random, time, os

# Python 2
# This game quizzes you on your knowledge of GRE words, providing the definition
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

    def collect_words(self, word_file="gre_word_file.txt"):
        """Builds the word database"""
        with open(word_file) as wordlist:
            wordlist = wordlist.read().splitlines()
            return wordlist

    def display_words(self):
        for word in self.words:
            print word

    def answer(self):
        """Chooses a random word from the wordlist and removes the word
        from the list"""
        answer_idx = random.randint(0, len(self.words) - 1)
        answer = self.words[answer_idx].lower()
        del self.words[answer_idx]
        return answer

    def definition(self, answer):
        """Queries the definition of the answer"""
        query = self.lookup.meaning(answer)
        print '\nDefinition: \n'
        for definition in query:
            print definition, '\n', query[definition], '\n'
        print '-' * 75 + '\n'

    def choices(self,answer, num=False):
        """Builds a list consisting of the answer and 3 other random words"""
        my_choices = [answer]
        while len(my_choices) < 4:
            choice = random.choice(self.words)
            if choice not in my_choices:
                my_choices.append(choice)
        random.shuffle(my_choices)
        answer_idx = my_choices.index(answer)
        if num:
            return enumerate(my_choices, start=1), answer_idx
        else:
            return my_choices

    def practice(self, answer):
        """Prompts user to type the answer 3x if the guess is incorrect"""
        print 'Please type the answer 3x, each on its own line.\n'
        count = 0
        while count < 3:
            word = raw_input('> ').lower()
            if word == answer:
                count += 1
            else:
                print 'Make sure your spelling is correct.'
        print '\nExcellent!'


class Game(object):

    def __init__(self):
        self.wins = 0
        self.attempts = 0
        self.data = Data()

    def clear_screen(self):
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')
        else:
            # Fallback for other operating systems.
            print '\n' * numlines

    def start(self):
        """Prompt to choose easy = number version or hard = word version."""
        self.clear_screen()
        self.game_on = True
        while self.game_on:
            choice = raw_input('Would you like the easy or hard version? \n').lower()
            if choice == 'easy':
                self.reset_score()
                self.num_game()
            elif choice == 'hard':
                self.reset_score()
                self.word_game()
            else:
                print 'I don\'t know what that means.'

    def num_questions(self):
        """Choose the number of questions"""
        while True:
            try:
                num = int(raw_input('How many questions would you like? (1-50) '))
            except Exception:
                print "That is not a valid number."
                continue
            if num not in range(1,51):
                print "Please choose a number between 1 and 50."
            else:
                break
        return num

    def word_game(self):
        """Word game initializes"""
        num = self.num_questions()
        print '\nGiven the definition, type the correct word. You have one try',
        'for each word.'
        raw_input('\nPress Enter to start...')
        for i in range(num):
            time.sleep(2)
            self.clear_screen()
            answer = self.data.answer()
            self.data.definition(answer)
            print self.data.choices(answer)

            turns = 0
            while turns < 1:
                guess = raw_input('\nAnswer: ')
                if guess.isdigit():
                    print "Please type the correct word as written."
                elif guess == answer:
                    print 'Correct!'
                    self.wins += 1
                    break
                else:
                    print 'Incorrect.'
                    turns += 1
                    if turns == 1:
                        print 'The answer was %s.' % answer
                        self.data.practice(answer)
            self.attempts += 1
        self.end()

    def num_game(self):
        """Num game initalizes"""
        print 'Given the definition, choose the correct number that',
        print 'corresponds to the word. \nYou have two tries.'
        num = self.num_questions()
        raw_input('Press Enter to start...')
        for i in range(num):
            time.sleep(2)
            self.clear_screen()
            answer = self.data.answer()
            self.data.definition(answer)
            choices, answer_idx = self.data.choices(answer, num)
            for choice in choices:
                print choice

            turns = 0
            while turns < 2:
                try:
                    guess = int(raw_input('\nAnswer: '))
                except Exception:
                    print 'That is not a valid number.'
                    continue
                if guess == answer_idx + 1:
                    print 'Correct!'
                    self.wins += 1
                    break
                elif guess not in range(1, 5):
                    print 'Please choose a number between 1 and 4.'
                else:
                    print 'Incorrect.'
                    turns += 1
            if turns == 2:
                print 'The answer was %s.' % answer
            self.attempts += 1
        self.end()

    def end(self):
        print '\nGame Over.\nYour score: %d/%d.' % (self.wins, self.attempts)
        if self.wins == self.attempts:
            print 'Perfect!'
        print '-' * 10
        self.game_on = False

    def reset_score(self):
        self.wins, self.attempts = 0, 0


game = Game()
game.start()
