import random

words = ["python", "programozas", "szamitogep", "linux", "jatek"]
word = random.choice(words)
guessed = []
tries = 6

print("🪢 AKASZTÓFA JÁTÉK")

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nSzó:", display)

    if "_" not in display:
        print("🎉 Nyertél!")
        break

    guess = input("Adj meg egy betűt: ").lower()

    if guess in word:
        guessed.append(guess)
    else:
        tries -= 1
        print("❌ Rossz tipp! Hátralévő próbák:", tries)

if tries == 0:
    print("💀 Vesztettél! A szó ez volt:", word)