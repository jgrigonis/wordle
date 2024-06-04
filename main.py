import os
import sys

from game import Game


def main():
    if len(sys.argv) > 1:
        answer = sys.argv[1]
    else:
        answer = None
    while True:
        x = Game(answer)
        x.play_game()


if __name__ == "__main__":
    main()
