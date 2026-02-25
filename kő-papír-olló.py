import random

choices = ["ko", "papir", "ollo"]

print("✊ KŐ - PAPÍR - OLLÓ")

player = input("Válassz (ko/papir/ollo): ").lower()
computer = random.choice(choices)

print("Gép választása:", computer)

if player == computer:
    print("🤝 Döntetlen!")
elif (player == "ko" and computer == "ollo") or \
        (player == "papir" and computer == "ko") or \
        (player == "ollo" and computer == "papir"):
    print("🎉 Nyertél!")
else:
    print("❌ Vesztettél!")