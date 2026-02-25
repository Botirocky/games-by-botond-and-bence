import random
import sys

RESPONSES = [
    "Anna",
    "Lili",
    "Luca",
    "Kitti",
    "Panna",
    "Hanna",
    "Hédi",
    "Judit",
    "Kincső",
    "Edina",
    "Kira",
    "Mira",
    "Flóra",
    "Nóra",
    "Hella",
]


def ask(question: str) -> str:
    """Ki legyen a barátnőd?"""
    return random.choice(RESPONSES)


def interactive():
    print("Akarsz egyet? I/N (Q = kilépés)")
    try:
        while True:
            q = input("válaszod: ").strip()
            if not q:
                print("Szija te szépfiú!")
                break
            print(ask(q))
    except (EOFError, KeyboardInterrupt):
        print("\nSzija te szépfiú!")


def main(argv):
    if len(argv) > 1:
        question = " ".join(argv[1:])
        print(f"Válaszod: {question}")
        print(ask(question))
    else:
        interactive()


if __name__ == "__main__":
    main(sys.argv)

