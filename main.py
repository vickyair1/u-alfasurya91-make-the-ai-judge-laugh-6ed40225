#!/usr/bin/env python3
"""Write the one-line office joke to /output/entry.txt.

The entry is one sentence about burnout and HR's idea of help. It works
by a reversal: the setup asks HR for relief from burnout, and the
punchline hands back two things — a stress ball, which is the token
wellness gesture, and a deadline, which is what caused the burnout in
the first place. The "cure" is the cause, so the line bites twice: HR
means well and makes it worse at the same time.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-200 characters, not only
whitespace, a single line) before it is written.
"""

import os

# Parts of the line: the setup confesses burnout to HR, the punchline
# gives back the wellness token plus the very thing that burned you out.
SETUP = "I told HR I was burned out;"
PUNCHLINE = "they gave me a stress ball and a deadline."

LINE = " ".join((SETUP, PUNCHLINE))


def validate(text):
    """Gate check: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
