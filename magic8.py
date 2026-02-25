#!/usr/bin/env python3
"""Simple Magic 8-Ball CLI

Usage:
- Run without arguments for interactive mode.
- Provide a question as arguments to get a single answer: python magic8.py "Will I win?"
"""
import random
import sys

RESPONSES = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes — definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]


def ask(question: str) -> str:
    """Return a random Magic 8-Ball style answer."""
    return random.choice(RESPONSES)


def interactive():
    print("Magic 8-Ball — ask a yes/no question (blank to quit)")
    try:
        while True:
            q = input("Your question: ").strip()
            if not q:
                print("Goodbye!")
                break
            print(ask(q))
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


def main(argv):
    if len(argv) > 1:
        question = " ".join(argv[1:])
        print(f"Question: {question}")
        print(ask(question))
    else:
        interactive()


if __name__ == "__main__":
    main(sys.argv)
