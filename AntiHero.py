import sys
import time
import os

def print_lyrics():
    lines = [
            ("\nWill he come back to see you?", 0.1),
            ("Thinking again", 0.09),
            ("Will he come back to save you?", 0.1),
            ("Oh no", 0.1),
            ("Take him away", 0.1),
            ("Come to my life", 0.1),
            ("I will give you all", 0.15),
    ]


    delays = [1, 1, 1, 1, 1, 1, 1,]

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
