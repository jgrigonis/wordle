import copy
import os
import random
import string

from colors import color


class Letter:
    """Represents a single letter in a word. Has a value, which is
    just simply the character, and a color which is the color of the
    letter.
    """

    def __init__(self, value, color="GREEN"):
        self.value = value
        self.color = color

    def __eq__(self, other):
        if isinstance(other, str):
            if self.value == other:
                return True
        else:
            if self.value == other.value:
                if self.color == other.color:
                    return True
        return False

    def __str__(self):
        output = color(self.color).color
        output = output + self.value
        output = output + color("END").color
        return output

    def squared(self):
        """The special 'square' characters for outputting results."""
        output = color(self.color).color
        output = output + "\u25A0"
        output = output + color("END").color
        return output


class Word:
    """A list of Letters, comprising a Word."""

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
        """The special 'square' characters for outputting results."""
        output = ""
        for letter in self.letters:
            output = output + letter.squared()
        return output


class Wordle:
    def __init__(self, answer=None):
        DATA_DIR = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "data",
        )
        ANSWER_WORDS_FILE = os.path.join(DATA_DIR, "answer_words.txt")
        self.answer_words_list = self.setup_word_list(ANSWER_WORDS_FILE)
        GUESS_WORDS_FILE = os.path.join(DATA_DIR, "guess_words.txt")
        self.guess_words_list = self.setup_word_list(GUESS_WORDS_FILE)
        self.set_answer(answer)
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
            self.answer = random.choice(self.answer_words_list)
        else:
            self.answer = answer

    def first_pass(self, guess):
        """Do the first pass with the guess.
        Return the output with green letters for exact matches.
        Return a remainder that has all the letters in answer
        that were not matched exactly and positionally.
        """
        remainder = []
        output = ["", "", "", "", ""]
        for counter in range(5):
            if self.answer[counter] == guess[counter]:
                output[counter] = Letter(guess[counter], "GREEN")
                self.greenlight(guess[counter])
            else:
                remainder.append(self.answer[counter])
        return output, remainder

    def output_letter_list(self, output):
        """Create a list of just the raw letters in the list of
        Letters in output.
        """
        letter_list = []
        for letter in output:
            if letter:
                letter_list.append(letter.value)
        return letter_list

    def second_pass(self, guess, output, remainder):
        """Do the second pass on the guess.
        All the characters in output that aren't blank are guaranteed
        to not be perfect matches.
        """
        # create a list of just the raw letter values in output
        letter_list = self.output_letter_list(output)
        for counter in range(5):
            # if the output is not yet filled
            if output[counter] == "":
                # if the letter in the remainder
                if guess[counter] in remainder:
                    output[counter] = Letter(guess[counter], "YELLOW")
                    remainder.remove(guess[counter])
                    # if it's not already green, set it yellow in the alphabet
                    if guess[counter] not in letter_list:
                        self.yellowlight(guess[counter])
                    letter_list.append(guess[counter])
                # if it's not in the remainder, turn it red in the output
                else:
                    output[counter] = Letter(guess[counter], "RED")
                    # if it's not already green or yellow, turn it red
                    if guess[counter] not in letter_list:
                        self.redlight(guess[counter])
        return output

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
        # first pass, look for exact positional matches only
        # put other characters from the answer into the remainder
        output, remainder = self.first_pass(guess)
        # second pass
        output = self.second_pass(guess, output, remainder)
        value = Word(output)
        self.guess_list.append(value)
        return value

    def greenlight(self, letter):
        """Turn a letter green when it is in correct position."""
        if letter in self.alphabet:
            self.alphabet = [
                Letter(letter, "GREEN") if x == letter else x for x in self.alphabet
            ]

    def yellowlight(self, letter):
        """Turn a letter yellow when it is in the word, but somewhere else."""
        if letter in self.alphabet:
            self.alphabet = [
                Letter(letter, "YELLOW") if x == letter else x for x in self.alphabet
            ]

    def redlight(self, letter):
        """Turn the letter red if it's missing from the answer."""
        if letter in self.alphabet:
            self.alphabet = [
                Letter(letter, "RED") if x == letter else x for x in self.alphabet
            ]

    def validate_guess(self, guess):
        """Verify a guess is in the guess words list."""
        if guess not in self.guess_words_list:
            self.bad_guess(guess)

    def bad_guess(self, guess):
        """Throw an error when the guess is bad."""
        print("{} is not a valid guess".format(guess))
        raise ValueError


def main():
    print("Try running main.py")


if __name__ == "__main__":
    main()
