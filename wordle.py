import os
import random
import string

from colors import color


class Letter():
    def __init__(self, value, color="GREEN"):
        self.value = value
        self.color = color

    def __eq__(self, other):
        if isinstance(other, str):
            if self.value == other:
                return True
        else:
            if self.value == other.value:
                return True
        return False    
    def __str__(self):
        output = color(self.color).color
        output = output + self.value
        output = output + color("END").color
        return output
    def squared(self):
        output = color(self.color).color
        output = output + '\u25A0'
        output = output + color("END").color
        return output


class Word():
    def __init__(self, letters=None, a_string=None):
        if letters is None:
            self.letters = []
        else:
            self.letters = letters
        if a_string is not None:
            for letter in a_string:
                self.letters.append(Letter(letter))

    def __str__(self):
        output = ""
        for letter in self.letters:
            output = output + str(letter)
        return output

    def __eq__(self, other):
        for count in range(5):
            if self.letters[count] != other.letters[count]:
                return False
        return True
    
    def __iter__(self):
        return iter(self.letters)
    
    def squared(self):
        output = ""
        for letter in self.letters:
            output = output + letter.squared()
        return output

        

class Wordle():
    def __init__(self, answer=None):
        DATA_DIR = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "data",
        )
        ANSWER_WORDS_FILE = os.path.join(DATA_DIR, "answer_words.txt")
        self.answer_words_list = self.setup_word_list(ANSWER_WORDS_FILE)
        GUESS_WORDS_FILE = os.path.join(DATA_DIR, "guess_words.txt")
        self.guess_words_list = self.setup_word_list(GUESS_WORDS_FILE)
        self.answer = self.set_answer(answer)
        self.guess_list = []
        self.alphabet = list(string.ascii_lowercase)


    def setup_word_list(self, word_file):
        """Create a word list based on a word file."""
        word_list = []
        with open(word_file) as wf:
            word_list.extend([word.strip() for word in wf.readlines()])
        return word_list


    def set_answer(self, answer=None):
        """This function will take an answer as input and set the answer to
        that, or if none is provided, it will pick a random answer from the
        allowable word list.
        """
        if answer is None:
            answer = random.choice(self.answer_words_list)
        return answer


    def handle_guess(self, guess):
        """This will handle a guess string, and determine the colors, green
        for a positional match, and yellow for a letter found elsewhere.

        The first pass, we are just looking for the exact matches. On the
        second pass we are checking which unmatched letters are in the
        other part of the answer.

        Unmatched letters should be black.

        Returns a Word
        """
        if guess is None:
            return
        try:
            self.validate_guess(guess)
        except ValueError:
            return
        remainder = []
        output = ["", "", "", "", ""]
        for counter in range(5):
            if self.answer[counter] == guess[counter]:
                output[counter] = Letter(guess[counter], "GREEN")
                self.greenlight(guess[counter])
            else:
                remainder.append(self.answer[counter])
        for counter in range(5):
            if output[counter] == "":
                if guess[counter] in remainder:
                    output[counter] = Letter(guess[counter], "YELLOW")
                    remainder.remove(guess[counter])
                    self.yellowlight(guess[counter])
                else:
                    output[counter] = Letter(guess[counter], "RED")
                    self.redlight(guess[counter])
        value = Word(output)
        self.guess_list.append(value)
        return value

    def greenlight(self, letter):
        if letter in self.alphabet:
            self.alphabet = [Letter(letter, "GREEN") if x==letter else x for x in self.alphabet]
            #self.alphabet.replace(letter, Letter(letter, "GREEN"))
    
    def yellowlight(self, letter):
        if letter in self.alphabet:
            self.alphabet = [Letter(letter, "YELLOW") if x==letter else x for x in self.alphabet]
            
    
    def redlight(self, letter):
        if letter in self.alphabet:
            self.alphabet = [Letter(letter, "RED") if x==letter else x for x in self.alphabet]
            

    def validate_guess(self, guess):
        if guess not in self.guess_words_list:
            self.bad_guess(guess)


    def bad_guess(self, guess):
        print("{} is not a valid guess".format(guess))
        raise ValueError
