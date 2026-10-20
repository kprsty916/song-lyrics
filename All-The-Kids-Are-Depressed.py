import sys
import time
import os

def print_lyrics():
    lines = [
            ("\nFalling in love", 0.07),
            ("Like it's just nothing", 0.07),
            ("I want to know", 0.07),
            ("Where do we go", 0.08),
            ("When nothing's wrong", 0.08),
            ("Cause all the kids are depressed", 0.05),
            ("Nothing ever makes sense", 0.06),
            ("I'm not feeling alright", 0.07),
            ("Staying up 'til sunrise", 0.07),
            ("And hoping shit is okay", 0.07),
            ("Pretending we know things", 0.07),
            ("I don't know what happened", 0.07),
            ("My natural reaction", 0.06),
            ("Is that we're scared", 0.07),
    ]


    delays = [0.4, 1, 0.6, 1, 0.6, 0.7, 0.7, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.4]

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






