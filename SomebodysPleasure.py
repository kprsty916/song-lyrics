import sys
import time
import os

def print_lyrics():
    lines = [
            ("\nSoul try to figure it out", 0.12),
            ("From where I've been escapin'", 0.12),
            ("Running to end all the sin", 0.12),
            ("Get away from the pressure", 0.12),
            ("Wondering to get a love", 0.14),
            ("That is so pure", 0.18),
            ("Gotta have to always make sure", 0.12),
            ("That I'm not just somebody's pleasure", 0.08),
    ]

    delays = [ 0.4, 0.8, 0.6, 0.4, 0.4, 1.4, 0.4, 0.4]

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