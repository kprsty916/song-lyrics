import sys
import time
import os

def print_lyrics():
    lines = [
            ("\nRight now", 0.11),
            ("I wish you were here with me", 0.07),
            ("(Ooh)", 0.11),
            ("Cause right now", 0.09),
            ("Everything is new to me", 0.09),
            ("(Ooh)", 0.11),
            ("You know I can't fight the feeling", 0.10),
            ("And every night I feel it", 0.09),
            ("Right now", 0.11),
            ("I wish you were here with me", 0.07),
    ]


    delays = [0.3, 2, 1.2, 1, 1.5, 1.7, 1.2, 1, 1, 0.3]

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






