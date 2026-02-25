import random
import time

# A kerék elemei
wheel = [
    "Nyeremény 1000 Ft",
    "Semmi",
    "Nyeremény 500 Ft",
    "Bónusz pörgetés",
    "Nyeremény 2000 Ft",
    "Semmi",
    "Ajándék",
    "Jackpot"
]

print("🎡 Pörgetés indul...")
time.sleep(1)

# Animáció
for i in range(15):
    print(random.choice(wheel))
    time.sleep(0.1)

result = random.choice(wheel)
print("\n👉 Eredmény:", result)