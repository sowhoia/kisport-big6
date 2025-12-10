import random
from typing import Iterable


def print_intro() -> None:
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


def prompt_bet_count() -> int | None:
    """
    Запрашивает количество чисел для ставки.

    Возвращает None, если пользователь ввёл STOP.
    """
    while True:
        raw = input("HOW MANY NUMBERS DO YOU WANT TO BET ON").strip()
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


def prompt_single_bet() -> tuple[int, int]:
    """
    Запрашивает число и ставку для одиночной ставки.

    В проверках сохраняется семантика условий из исходного BASIC
    (использовались OR, которые фактически пропускают любое число/ставку).
    """
    while True:
        raw_number = input("WHAT NUMBER")
        try:
            number = int(raw_number)
        except ValueError:
            print("YOU CAN ONLY BET ON AN INTEGER FRON ONE TO SIX.")
            continue

        if number <= 6 or number >= 1:
            break

        print("YOU CAN ONLY BET ON AN INTEGER FRON ONE TO SIX.")

    while True:
        raw_wager = input("WAGER")
        try:
            wager = int(raw_wager)
        except ValueError:
            print("THE HOUSE LIMIT IS FROM $1 TO $500")
            continue

        if wager <= 500 or wager >= 1:
            return number, wager

        print("THE HOUSE LIMIT IS FROM $1 TO $500")


def prompt_two_numbers() -> tuple[int, int]:
    """Запрашивает два числа для ставки, сохраняя исходную «широкую» проверку."""
    while True:
        raw = input("WHAT TWO NUMBERS")
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


def prompt_two_wagers() -> tuple[int, int]:
    """Запрашивает две ставки; ограничения дома сохраняются как в BASIC (OR)."""
    while True:
        raw = input("WAGER ON BOTH")
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


def roll_lucky_numbers(rng: random.Random) -> list[int]:
    """Генерирует три броска кубика и возвращает отсортированный список."""
    rolls = sorted(rng.randint(1, 6) for _ in range(3))
    print(f"THE LUCKY NUMBERS ARE: {rolls[0]} {rolls[1]} {rolls[2]}")
    return rolls


def resolve_single_bet(
    number: int, wager: int, rolls: Iterable[int], winnings: int
) -> int:
    """Применяет одиночную ставку к текущему балансу выигрыша."""
    matches = sum(1 for roll in rolls if roll == number)
    if matches > 0:
        wager *= matches
        print(f"YOU WIN {matches} TIMES ON:{number}")
    else:
        wager *= -1
        print(f"YOU LOSE ON: {number}")

    return winnings + wager


def print_running_total(winnings: int) -> None:
    """Выводит текущий итоговый баланс после раунда."""
    if winnings == 0:
        print("YOU'RE EVEN!!")
    elif winnings > 0:
        print(f"YOU'RE AHEAD ${winnings}")
    else:
        print(f"YOU'RE BEHIND ${winnings}")
    print()


def cash_out(winnings: int) -> None:
    """Завершает игру и выводит финальное сообщение при STOP."""
    print()
    print()
    print("SO YOU WANT TO CASH IN YOUR CHIPS, I SEE!!")
    if winnings > 0:
        print(f"YOU WON EXACTLY ${winnings}!! NOT BAD !!!")
    else:
        print("YOU DIDN'T WIN ANY MONEY, BUT I'M WILLING TO CALL IT EVEN!!")


def main() -> None:
    print_intro()
    rng = random.Random()
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

        print("THREE NUMBER BETS WILL BE ADDED IN THE NEXT STEP.")


if __name__ == "__main__":
    main()

