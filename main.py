from wordle import Wordle
from wordle import Word

class game():
    def __init__(self):
        self.intro()
        self.game = Wordle()
        self.game_over = False
        self.guesses = 0
        self.play_game()

    def intro(self):
        print("You get 6 guesses.")
        print("Each guess should be a 5 letter word.")
        print("Green letters mean your letter is in the right location")
        print("Yellow letters are in the answer, but in a different position")
        print("Red letters are not in the answer")
        print("")

    def guess(self):
        guess = input("What is your guess? ")
        return guess

    def play_game(self):
        while not self.game_over:
            guess = self.game.handle_guess(self.guess())
            if guess:
                print(guess)
                self.guesses += 1
                if guess == Word(a_string=self.game.answer):
                    print("You got it!")
                    quit()
            if self.guesses == 6:
                self.end_game()

    def end_game(self):
        print("The answer was:")
        print(Word(a_string=self.game.answer))
        quit()

x = game()
quit()
