# Python 2
from PyDictionary import PyDictionary
import random, time, os

class Data(object):

    # Builds the word database
    def collect_words(word_file="gre_word_file.txt"):
        wordlist = open(word_file).read().splitlines()
        return wordlist

    def __init__(self, words=collect_words()):
        self.words = words
        self.lookup = PyDictionary()

    def display_words(self):
        for word in self.words:
            print word
    # Chooses a random word from the wordlist
    def answer(self):
        answer_idx = random.randint(0, len(self.words) - 1)
        answer = self.words[answer_idx]
        del self.words[answer_idx]
        return answer
    # Queries the definition of the answer
    def definition(self, answer):
        query = self.lookup.meaning(answer)
        print '\nDefinition: \n'
        for definition in query:
            print definition, '\n', query[definition]
        print '-' * 75 + '\n'
    # Builds a list consisting of the answer and 3 other random words
    def choices(self,answer):
        my_choices = [answer]
        while len(my_choices) < 4:
            choice = random.choice(self.words)
            if choice not in my_choices:
                my_choices.append(choice)
        random.shuffle(my_choices)
        print my_choices
    # Prompts user to type the answer 3x if the guess is incorrect
    def practice(self, answer):
        print 'Please type the answer 3x, each on its own line.\n'
        count = 0
        while count < 3:
            word = raw_input('> ')
            if word == answer:
                count += 1
            else:
                print 'Make sure your spelling is correct.'
        game_on = False


class Main(object):

    def __init__(self):
        self.wins = 0
        self.attempts = 0

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

    def game_type(self):
        game_on = True
        while game_on:
            choice = raw_input('\nWould you like the easy or hard version? \n').lower()
            if choice.startswith('h'):
                self.reset_score()
                self.word_game()
                print 'Given the definition, type the correct word. You have one try.'
            elif choice.startswith('e'):
                self.reset_score()
                self.clear_screen()
                self.num_game()
                print 'Given the definition, choose the correct number that',
                'corresponds to the word. You have two tries.'
            else:
                print 'I don\'t know what that means.'

    def num_questions(self):
        while True:
            try:
                num = int(raw_input('How many questions would you like? (1-20) '))
            except:
                print "That is not a valid number."
                continue
            else:
                break
        return num

    def word_game(self):
        num = self.num_questions()
        for i in range(num):
            time.sleep(2)
            self.clear_screen()
            answer = data.answer()
            data.definition(answer)
            data.choices(answer)

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
                        print 'The answer was %s.' % (answer)
                        data.practice(answer)
            self.attempts += 1
        print 'Your score is %d/%d.' % (self.wins, self.attempts)
        print '-' * 10
        game_on = False



    def num_game(self):
        pass

    def reset_score(self):
        self.wins, self.attempts = 0, 0


data = Data()
g = Main()
