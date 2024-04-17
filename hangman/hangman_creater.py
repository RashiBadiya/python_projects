import random
import re

class Hangman:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.attempts_remaining = 6
        self.current_letter = ''
        self.chosen_word = ''
        self.guessed_letters = []

    def choose_the_word(self):
        with open(self.wordlist) as file:
            words = file.read().split('\n')
        word_count = len(words)
        self.chosen_word = random.choice(words)
        print(self.chosen_word)
        self.word_status = '-' * len(self.chosen_word)

    def fill_the_word_status(self):
        nos = random.randrange(1, 3)
        for i in range(nos):
            position = random.randrange(0, len(self.chosen_word))
            self.word_status = self.word_status[:position] + self.chosen_word[position] + self.word_status[position + 1:]

    def guess_the_letter(self):
        letter = input("Guess a letter: ")
        if letter in self.guessed_letters:
            print("You have already guessed the letter. Your guesses so far: {}".format(''.join(self.guessed_letters)))
            return
        self.guessed_letters.append(letter)
        occurrences = []
        occurrence = re.finditer(letter, self.chosen_word)
        for m in occurrence:
            occurrences.append(m.start())
        if len(occurrences) == 0:
            self.attempts_remaining -= 1
            print("Oops! Your guess was wrong. Attempts remaining: {}".format(self.attempts_remaining))
        else:
            for position in occurrences:
                self.word_status = self.word_status[:position] + self.chosen_word[position] + self.word_status[position + 1:]
            print("Correct guess!")

    def get_word_status(self):
        print("Current status: {}".format(self.word_status))
