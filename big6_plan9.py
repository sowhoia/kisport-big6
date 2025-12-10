#!/usr/bin/env python3
"""
BIG6 for Plan9 environment.
Uses only basic I/O compatible with Plan9's Python port.
"""

import random
import sys


def main():
    # No fancy output - Plan9 compatible
    sys.stdout.write("BIG6 - CREATIVE COMPUTING\n")
    sys.stdout.write("Bet on 1-6, up to 3 numbers. STOP to quit.\n\n")
    sys.stdout.flush()
    
    rng = random.Random()
    winnings = 0
    
    while True:
        sys.stdout.write("How many numbers (1-3)? ")
        sys.stdout.flush()
        
        try:
            line = sys.stdin.readline().strip()
        except:
            break
            
        if line.upper() == "STOP":
            break
        
        try:
            count = int(line)
            if count < 1 or count > 3:
                sys.stdout.write("Enter 1, 2, or 3\n")
                continue
        except ValueError:
            sys.stdout.write("Enter 1, 2, or 3\n")
            continue
        
        numbers = []
        wagers = []
        
        for i in range(count):
            sys.stdout.write("Number? ")
            sys.stdout.flush()
            try:
                n = int(sys.stdin.readline().strip())
                numbers.append(n)
            except:
                numbers.append(1)
            
            sys.stdout.write("Wager? ")
            sys.stdout.flush()
            try:
                w = int(sys.stdin.readline().strip())
                wagers.append(w)
            except:
                wagers.append(1)
        
        # Roll dice
        rolls = sorted([rng.randint(1, 6) for _ in range(3)])
        sys.stdout.write("Lucky numbers: %d %d %d\n" % (rolls[0], rolls[1], rolls[2]))
        
        # Calculate results
        for i, (num, wager) in enumerate(zip(numbers, wagers)):
            matches = rolls.count(num)
            if matches > 0:
                winnings += wager * matches
                sys.stdout.write("Win %dx on %d\n" % (matches, num))
            else:
                winnings -= wager
                sys.stdout.write("Lose on %d\n" % num)
        
        if winnings > 0:
            sys.stdout.write("Ahead $%d\n\n" % winnings)
        elif winnings < 0:
            sys.stdout.write("Behind $%d\n\n" % winnings)
        else:
            sys.stdout.write("Even\n\n")
        sys.stdout.flush()
    
    sys.stdout.write("\nCashing out: $%d\n" % winnings)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
