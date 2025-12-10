#!/usr/bin/env python3
"""
Minimal bootloader-style BIG6 for educational purposes.
Simulates a bootloader environment with minimal I/O.

This demonstrates how the game WOULD work in a bootloader,
but actual bootloader requires assembly/C.
"""

import random

# Simulated "bootloader" mode - minimal output
def boot_print(s: str) -> None:
    """Minimal print for bootloader simulation."""
    print(s)


def boot_input(prompt: str) -> str:
    """Minimal input for bootloader simulation."""
    boot_print(prompt)
    return input()


def main() -> None:
    boot_print("BIG6 BOOT")
    boot_print("Bet 1-6, $1-500")
    boot_print("Enter 0 to quit")
    
    rng = random.Random()
    winnings = 0
    
    while True:
        try:
            raw = boot_input("Num? ")
            num = int(raw)
            if num == 0:
                break
            if not 1 <= num <= 6:
                continue
                
            raw = boot_input("Bet? ")
            bet = int(raw)
            if not 1 <= bet <= 500:
                continue
            
            # Roll 3 dice
            rolls = [rng.randint(1, 6) for _ in range(3)]
            matches = rolls.count(num)
            
            boot_print(f"Dice: {rolls[0]} {rolls[1]} {rolls[2]}")
            
            if matches > 0:
                win = bet * matches
                winnings += win
                boot_print(f"WIN ${win}")
            else:
                winnings -= bet
                boot_print("LOSE")
            
            boot_print(f"Total: ${winnings}")
            
        except ValueError:
            continue
        except EOFError:
            break
    
    boot_print(f"Final: ${winnings}")


if __name__ == "__main__":
    main()
