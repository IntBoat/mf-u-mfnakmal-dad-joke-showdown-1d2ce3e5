#!/usr/bin/env python3
"""Dad Joke Showdown (make.fun).

Writes the entry -- one dad joke, told out loud -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = "I told my Wi-Fi a joke, but it kept dropping the punchline — I guess the connection just wasn't strong enough."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
