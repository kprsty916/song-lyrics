import sys
import time
import os

def print_lyrics():
    lines = [
            ("\nRhythms of the night", 0.07),
            ("Consume my body", 0.12),
            ("Just let the music", 0.07),
            ("Confiscate my soul", 0.08),
            ("You think I'm lost", 0.08),
            ("But that's just how", 0.06),
            ("You found me", 0.09),
            ("Well, maybe I'm the stranger", 0.07),
            ("After all", 0.15),
    ]

    delays = [ 0.8, 1.1, 0.5, 1.5, 0.3, 0.3, 1.9, 0.8, 0.3]

    os.system('cls' if os.name == 'nt' else 'clear')

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        BOLD_WHITE = "\033[1;37m"
        RESET = "\033[0m"

        for i, (line, char_delay) in enumerate(lines):
            sys.stdout.write(BOLD_WHITE)
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(char_delay)
            sys.stdout.write(RESET + "\n")
            sys.stdout.flush()

            if i < len(delays):
                time.sleep(delays[i])
    finally:
        time.sleep(1)
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    print_lyrics()






