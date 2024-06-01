import string

from wordle import Wordle
from wordle import Word
from wordle import Letter


class Game:
    def __init__(self):
        self.intro()
        self.game = Wordle()
        self.game_over = False
        self.guesses = 0
        self.special_words = [
            "quit",
            "exit",
            "help",
            "unused",
            "history",
            "qwerty",
            "alphabet",
            "hint",
            "commands",
            "squares",
        ]
        self.prompt = "What is your guess? "

    def intro(self):
        """Display the way the game works, explain the colors."""
        print("You get 6 guesses.")
        print("Each guess should be a 5 letter word.")
        print("Green letters mean your letter is in the right location")
        print("Yellow letters are in the answer, but in a different position")
        print("Red letters are not in the answer")
        print("")

    def set_prompt(self):
        """Ask the user for their guess."""
        tries = ""
        if self.guesses == 0:
            tries = "first"
        if self.guesses == 1:
            tries = "second"
        if self.guesses == 2:
            tries = "third"
        if self.guesses == 3:
            tries = "fourth"
        if self.guesses == 4:
            tries = "fifth"
        if self.guesses == 5:
            tries = "sixth and final"
        self.prompt = "What is your {} guess? ".format(tries)

    def do_guess(self):
        """Handle a single guess."""
        self.set_prompt()
        guess = input(self.prompt)
        if guess in self.special_words:
            self.handle_special(guess)
            return None
        return guess

    def play_game(self):
        """Run the game until it's over."""
        while not self.game_over:
            guess = self.game.handle_guess(self.do_guess())
            if guess:
                self.guesses += 1
                if guess == Word(a_string=self.game.answer):
                    self.end_game("You got it!")
                if not self.game_over:
                    print(guess)
            if self.guesses == 6:
                self.end_game("The answer was:")

    def show_unused(self):
        """Print the letters from a to z that don't appear in a guess."""
        print("Unused letters:")
        for letter in string.ascii_lowercase:
            found = False
            for word in self.game.guess_list:
                if letter in word:
                    found = True
            if not found:
                print(letter, end=" ")
        print()

    def show_qwerty(self):
        """Print the letters in the configuration of a qwerty keyboard
        with all the appropriate colors.
        """
        print(self.game.alphabet[16], end=" ")
        print(self.game.alphabet[22], end=" ")
        print(self.game.alphabet[4], end=" ")
        print(self.game.alphabet[17], end=" ")
        print(self.game.alphabet[19], end=" ")
        print(self.game.alphabet[24], end=" ")
        print(self.game.alphabet[20], end=" ")
        print(self.game.alphabet[8], end=" ")
        print(self.game.alphabet[14], end=" ")
        print(self.game.alphabet[15], end=" ")
        print(" ")
        print(" ", end="")
        print(self.game.alphabet[0], end=" ")
        print(self.game.alphabet[18], end=" ")
        print(self.game.alphabet[3], end=" ")
        print(self.game.alphabet[5], end=" ")
        print(self.game.alphabet[6], end=" ")
        print(self.game.alphabet[7], end=" ")
        print(self.game.alphabet[9], end=" ")
        print(self.game.alphabet[10], end=" ")
        print(self.game.alphabet[11], end=" ")
        print(" ")
        print("  ", end="")
        print(self.game.alphabet[25], end=" ")
        print(self.game.alphabet[23], end=" ")
        print(self.game.alphabet[2], end=" ")
        print(self.game.alphabet[21], end=" ")
        print(self.game.alphabet[1], end=" ")
        print(self.game.alphabet[13], end=" ")
        print(self.game.alphabet[12], end=" ")
        print("")

    def show_alphabet(self):
        """Show the alphabet, colorized."""
        for letter in self.game.alphabet:
            print(letter, end=" ")
        print("")

    def show_color_boxes(self):
        """These are the colored squares, showing your matches."""
        if self.game.guess_list == []:
            print("No guesses made yet.")
            return
        for guess in self.game.guess_list:

            print(guess.squared())
        print("")

    def show_history(self):
        """Show the past guesses."""
        if self.game.guess_list == []:
            print("You haven't made any guesses.")
            return
        print("Previous guesses:")
        for guess in self.game.guess_list:
            print(guess)
        print("")

    def show_commands(self):
        """List out the commands for the user."""
        print("Commands:")
        print("quit - completely quit the game")
        print("exit - exit the current puzzle")
        print("help - show some helpful info")
        print("unused - show all the letters you have not used in a guess")
        print("history - show all your previous guesses")
        print("qwerty - show all the letters appropriately colored")
        print("alphabet - show all the letters appropriately colored")
        print("hint - it's like cheating")
        print("commands - show this list")
        print("")

    def handle_special(self, guess):
        """Deal with the special commands."""
        if guess == "quit":
            self.end_game("OK, bye!\nThe answer was:", False)
        if guess == "exit":
            self.end_game("The answer was:")
        if guess == "help":
            self.intro()
            print("Try `commands` to see the special commands.")
        if guess == "unused":
            self.show_unused()
        if guess == "history":
            self.show_history()
        if guess == "qwerty":
            self.show_qwerty()
        if guess == "alphabet":
            self.show_alphabet()
        if guess == "hint":
            print("There are no hints in Wordle, Get Good.")
        if guess == "commands":
            self.show_commands()
        if guess == "squares":
            self.show_color_boxes()

    def play_again(self):
        """Ask to restart the game."""
        answer = input("Do you want to play again? (y/n)")
        if answer.lower().startswith("y"):
            return True
        if answer.lower().startswith("n"):
            return False
        return self.play_again()

    def end_game(self, exit_message, ask=True):
        """End a game."""
        print(exit_message)
        print(Word(a_string=self.game.answer))
        self.game_over = True
        self.show_color_boxes()
        if ask:
            if not self.play_again():
                quit()
        else:
            quit()


def main():
    while True:
        x = Game()
        x.play_game()


if __name__ == "__main__":
    main()
