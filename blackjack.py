import random

def draw_card():
    return random.randint(1, 11)

print("🃏 BLACKJACK")

player = draw_card() + draw_card()
dealer = draw_card() + draw_card()

print("Lapjaid összege:", player)

while player < 21:
    choice = input("Kérsz még lapot? (i/n): ")
    if choice == "i":
        player += draw_card()
        print("Új összeg:", player)
    else:
        break

if player > 21:
    print("💀 Bust! Vesztettél.")
else:
    print("Dealer összeg:", dealer)
    while dealer < 17:
        dealer += draw_card()

    print("Dealer végső összeg:", dealer)

    if dealer > 21 or player > dealer:
        print("🎉 Nyertél!")
    elif player == dealer:
        print("🤝 Döntetlen!")
    else:
        print("❌ Vesztettél!")