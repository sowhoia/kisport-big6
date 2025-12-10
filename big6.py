#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
BIG6 - Dice Wheel Game
Port from More BASIC Computer Games (Creative Computing)

Compatible with Python 2.7+ and Plan9
"""
import os
import random


def print_intro():
    """Выводит вступительный текст, повторяя оформление версии на BASIC."""
    print(" " * 26 + "BIG6")
    print(" " * 19 + "CREATIVE COMPUTING")
    print(" " * 17 + "MORRISTOWN, NEW JERSEY")
    print()
    print()
    print()
    print("  THIS PROGRAM IS A DICE WHEEL GAME IN WHICH")
    print("YOU CAN BET ON ANY NUMBER BETWEEN ONE AND SIX")
    print("AND UP TO THREE NUMBERS.")
    print("  THE HOUSE LIMIT IS FROM $1 TO $500!!")
    print("TO END THIS PROGRAM TYPE THE WORD 'STOP'.")
    print("GOOD LUCK!")
    print()
    print()


def make_rng_from_env():
    """Создаёт генератор, используя BIG6_SEED при наличии для детерминизма."""
    seed = os.environ.get("BIG6_SEED")
    if seed is None:
        return random.Random()

    try:
        seed_value = int(seed)
    except ValueError:
        return random.Random()

    return random.Random(seed_value)


def prompt_bet_count():
    """
    Запрашивает количество чисел для ставки.

    Возвращает None, если пользователь ввёл STOP.
    """
    while True:
        raw = input("HOW MANY NUMBERS DO YOU WANT TO BET ON? ").strip()
        if raw.upper() == "STOP":
            return None
        try:
            count = int(raw)
        except ValueError:
            print("YOU CANNOT BET ON LESS THAN ONE OR MORE THAN THREE NUMBERS.")
            continue

        if count in (1, 2, 3):
            return count

        print("YOU CANNOT BET ON LESS THAN ONE OR MORE THAN THREE NUMBERS.")


def prompt_single_bet():
    """
    Запрашивает число и ставку для одиночной ставки.

    В проверках сохраняется семантика условий из исходного BASIC
    (использовались OR, которые фактически пропускают любое число/ставку).
    """
    while True:
        raw_number = input("WHAT NUMBER? ")
        try:
            number = int(raw_number)
        except ValueError:
            print("YOU CAN ONLY BET ON AN INTEGER FRON ONE TO SIX.")
            continue

        if number <= 6 or number >= 1:
            break

        print("YOU CAN ONLY BET ON AN INTEGER FRON ONE TO SIX.")

    while True:
        raw_wager = input("WAGER? ")
        try:
            wager = int(raw_wager)
        except ValueError:
            print("THE HOUSE LIMIT IS FROM $1 TO $500")
            continue

        if wager <= 500 or wager >= 1:
            return number, wager

        print("THE HOUSE LIMIT IS FROM $1 TO $500")


def prompt_two_numbers():
    """Запрашивает два числа для ставки, сохраняя исходную «широкую» проверку."""
    while True:
        raw = input("WHAT TWO NUMBERS? ")
        parts = raw.replace(",", " ").split()
        if len(parts) != 2:
            print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")
            continue

        try:
            first, second = (int(part) for part in parts)
        except ValueError:
            print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")
            continue

        if (first <= 6 or first >= 1) and (second <= 6 or second >= 1):
            return first, second

        print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")


def prompt_two_wagers():
    """Запрашивает две ставки; ограничения дома сохраняются как в BASIC (OR)."""
    while True:
        raw = input("WAGER ON BOTH? ")
        parts = raw.replace(",", " ").split()
        if len(parts) != 2:
            print("THE HOUSE LIMIT IS FROM $1 TO $500.")
            continue

        try:
            first, second = (int(part) for part in parts)
        except ValueError:
            print("THE HOUSE LIMIT IS FROM $1 TO $500.")
            continue

        if (first <= 500 or first >= 1) and (second <= 500 or second >= 1):
            return first, second

        print("THE HOUSE LIMIT IS FROM $1 TO $500.")


def prompt_three_numbers():
    """Запрашивает три числа для ставки, отражая исходные проверки через OR."""
    while True:
        raw = input("WHAT THREE NUMBERS? ")
        parts = raw.replace(",", " ").split()
        if len(parts) != 3:
            print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")
            continue

        try:
            first, second, third = (int(part) for part in parts)
        except ValueError:
            print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")
            continue

        if (
            first <= 6
            or first >= 1
            or second <= 6
            or second >= 1
            or third <= 6
            or third >= 1
        ):
            return first, second, third

        print("YOU CAN ONLY BET ON AN INTEGER FROM ONE TO SIX.")


def prompt_three_wagers():
    """Запрашивает три ставки, оставляя оригинальные границы с OR."""
    while True:
        raw = input("WAGER ON EACH OF THE THREE? ")
        parts = raw.replace(",", " ").split()
        if len(parts) != 3:
            print("THE HOUSE LIMIT IS FROM $1 TO $500.")
            continue

        try:
            first, second, third = (int(part) for part in parts)
        except ValueError:
            print("THE HOUSE LIMIT IS FROM $1 TO $500.")
            continue

        if (
            first <= 500
            or first >= 1
            or second <= 500
            or second >= 1
            or third <= 500
            or third >= 1
        ):
            return first, second, third

        print("THE HOUSE LIMIT IS FROM $1 TO $500.")


def roll_lucky_numbers(rng):
    """Генерирует три броска кубика и возвращает отсортированный список."""
    rolls = sorted(rng.randint(1, 6) for _ in range(3))
    print("THE LUCKY NUMBERS ARE: %d %d %d" % (rolls[0], rolls[1], rolls[2]))
    return rolls


def resolve_single_bet(number, wager, rolls, winnings):
    """Применяет одиночную ставку к текущему балансу выигрыша."""
    matches = sum(1 for roll in rolls if roll == number)
    if matches > 0:
        wager *= matches
        print("YOU WIN %d TIMES ON:%d" % (matches, number))
    else:
        wager *= -1
        print("YOU LOSE ON: %d" % number)

    return winnings + wager


def print_running_total(winnings):
    """Выводит текущий итоговый баланс после раунда."""
    if winnings == 0:
        print("YOU'RE EVEN!!")
    elif winnings > 0:
        print("YOU'RE AHEAD $%d" % winnings)
    else:
        print("YOU'RE BEHIND $%d" % winnings)
    print()


def cash_out(winnings):
    """Завершает игру и выводит финальное сообщение при STOP."""
    print()
    print()
    print("SO YOU WANT TO CASH IN YOUR CHIPS, I SEE!!")
    if winnings > 0:
        print("YOU WON EXACTLY $%d!! NOT BAD !!!" % winnings)
    else:
        print("YOU DIDN'T WIN ANY MONEY, BUT I'M WILLING TO CALL IT EVEN!!")


def main():
    print_intro()
    rng = make_rng_from_env()
    winnings = 0

    while True:
        bet_count = prompt_bet_count()
        if bet_count is None:
            cash_out(winnings)
            return

        if bet_count == 1:
            number, wager = prompt_single_bet()
            rolls = roll_lucky_numbers(rng)
            winnings = resolve_single_bet(number, wager, rolls, winnings)
            print_running_total(winnings)
            continue

        if bet_count == 2:
            first_number, second_number = prompt_two_numbers()
            first_wager, second_wager = prompt_two_wagers()
            rolls = roll_lucky_numbers(rng)
            winnings = resolve_single_bet(first_number, first_wager, rolls, winnings)
            winnings = resolve_single_bet(second_number, second_wager, rolls, winnings)
            print_running_total(winnings)
            continue

        first_number, second_number, third_number = prompt_three_numbers()
        first_wager, second_wager, third_wager = prompt_three_wagers()
        rolls = roll_lucky_numbers(rng)
        winnings = resolve_single_bet(first_number, first_wager, rolls, winnings)
        winnings = resolve_single_bet(second_number, second_wager, rolls, winnings)
        winnings = resolve_single_bet(third_number, third_wager, rolls, winnings)
        print_running_total(winnings)


if __name__ == "__main__":
    main()
