#
# :date: 2018-10-18
# :author: Andre Stephens
# :copyright: GPL v2 or later
#
#

import time
import string
import random

class WordsOfFortune():
    """Functionalities for Words of Fortune Game"""
    def __init__(self):
        self.word = set()
        self.current_word = []
        self.letter = ''
    def get_word(self):
        return self.word
    def choose_word(self):
        self.word = random.choice(self.wordlist).upper()
    def get_current_word(self):
        return(' '.join(self.current_word))
    def make_current_word(self):
        nletters = len(self.word)
        self.current_word = ['_']*nletters
        return self.current_word
    def update_current_word(self):
        n_guess = 0
        for i, le in enumerate(self.word):
            if le == self.letter:
                self.current_word[i] = le
                n_guess += 1
        return n_guess
    def update_score(self, spin, score, n_guess):
        if self.letter in 'AEIOU':
            return score - (250*n_guess)
        return score + (spin*n_guess)
    def update_available_letters(self):
        return self.available_letters.remove(self.letter)
    def computer_choose_letter(self):
        self.letter = random.choice(self.available_letters)
        return self.letter
    def choose_consonant(self):
        self.letter = input('Choose a letter...  ').upper()
        while self.letter not in self.available_letters:
            self.letter = input('You must choose among available letters...  ').upper()
        return self.letter     
    def buy_vowel(self):
        self.letter = input('Please choose a vowel... ').upper()
        while self.letter not in 'AEIOU':
            self.letter = input('You MUST choose a vowel... ').upper()
        return self.letter
    def is_solved(self):
        if set(self.current_word) == set(self.word):
            return True
        return False


class BuildWF(WordsOfFortune):
    """Build Wheel and Wordlist"""
    def __init__(self):
        WordsOfFortune.__init__(self)
        self.wheel = []
        self.word_list = []
        self.available_letters = []
        print('Welcome to Words of Fortune!!!')
    def build_wheel(self):
        numbers = [n for n in range(500,950,50)]*3
        bankrupt = ['bankrupt']*2
        lose_turn = ['lose turn']*2
        big_prize = [2500]
        self.wheel = numbers + bankrupt + lose_turn + big_prize
        return self.wheel
    def get_wheel(self):
        return self.wheel
    def load_words(self, fname):
        inFile = open(fname, 'r')
        line = inFile.readline()
        self.wordlist = line.split()
        print('Ready to play!')
        time.sleep(2)
    def make_available_letters(self):
        self.available_letters = [l for l in string.ascii_uppercase]
        return self.available_letters
    def print_header(self, player):
        print('______________________________________')
        print('\n')
        time.sleep(2)
        print("******LET'S GO*******")
        time.sleep(1)
        print("Here are the available letters:", ' '.join(self.available_letters))
        time.sleep(1)
        print("<>", player.upper(), '<>: OK... MAKE A GUESS:', ' '.join(self.current_word))
        time.sleep(1)
