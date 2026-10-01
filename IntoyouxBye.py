import os
import sys
import time
from threading import Thread, Lock

lock = Lock()

def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def animate_text(text, speed):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nBefore I make a move", 0.09),
        ("(Ooh-ooh-ooh-ooh-ooh)", 0.11),
        ("So baby, come light me up", 0.07),
        ("And maybe I'll let you on it", 0.07),
        ("A little bit dangerous", 0.07),
        ("But baby, that's how I want it", 0.07),
        ("A little less conversation, and", 0.06),
        ("A little more touch my body", 0.08),
        ("'Cause I'm so into you, into you, into you", 0.10),
    ]

    delays = [0.3, 2.7, 5.4, 8.0, 10.0, 12.4, 14.0, 15.5, 19.0,
    ]

    os.system("cls" if os.name == "nt" else "clear")
    hide_cursor()

    try:
        threads = [
            Thread(
                target=sing_lyric,
                args=(lyric, delays[i], speed)
            )
            for i, (lyric, speed) in enumerate(lyrics)
        ]

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    finally:
        show_cursor()


if __name__ == "__main__":
    sing_song()