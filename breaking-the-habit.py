import sys
import time
import os

def print_lyrics():
    lines = [
        ("\nI don't know what's worth fighting for", 0.05),
        ("Or why I have to scream", 0.09),
        ("I don't know why I instigate", 0.09),
        ("And say what I don't mean", 0.07),
        ("I don't know how I got this way", 0.07),
        ("I know it's not alright", 0.08),
        ("So, I'm breaking the habit", 0.14),
        ("I'm breaking the habit tonight", 0.19),
    ]

    delays = [0.3, 0.3, 0.3, 0.4, 0.2, 0.2, 0.3, 1]

    os.system('cls' if os.name == 'nt' else 'clear')

    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        BOLD_WHITE = "\033[31m"
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
        time.sleep(0)
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    print_lyrics()
