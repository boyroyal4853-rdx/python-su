import random

def dice_roll():
    print("🎲 Dice Rolling Simulator 🎲")
    while True:
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")
        again = input("Roll again? (y/n): ")
        if again.lower() != "y":
            break

dice_roll()
