# BIG6 - Dice Wheel Game

Порт классической игры BIG6 из сборника "More BASIC Computer Games" (Creative Computing, Morristown, New Jersey).

## Описание игры

BIG6 — это азартная игра с игральными костями. Игрок может делать ставки на числа от 1 до 6, выбирая от 1 до 3 чисел за раунд. Бросаются три кости, и если выпадает загаданное число, игрок выигрывает ставку, умноженную на количество совпадений. Если число не выпало — ставка проиграна.

Лимит ставок: от $1 до $500.

Для выхода из игры введите `STOP`.

## Платформы

| Платформа | Файл | Статус |
|-----------|------|--------|
| Linux | `big6.py` | ✅ |
| Windows | `big6.py` | ✅ |
| Web (Pyodide) | `index.html` | ✅ |
| Android (Termux) | `big6.py` | ✅ |
| Plan9 | `big6_plan9.py` | ✅ |
| Bootloader (симуляция) | `big6_boot.py` | ✅ |

## Сборка и запуск

### Linux / Windows

```bash
make run        # Запуск игры
make test       # Запуск тестов
```

### Web-версия

```bash
make web        # http://localhost:8000
```

### Android (Termux)

1. Установите [Termux](https://termux.dev/) из F-Droid
2. Скопируйте проект на устройство
3. Запустите:

```bash
chmod +x termux_setup.sh
./termux_setup.sh
# или вручную:
pkg install python
python big6.py
```

### Plan9

Используйте `big6_plan9.py` — версию с базовым I/O через `sys.stdout/stdin`:

```bash
python big6_plan9.py
```

Для Plan9 с портом Python (9legacy/plan9port):
```
/bin/python big6_plan9.py
```

### Bootloader (симуляция)

`big6_boot.py` — упрощённая версия, демонстрирующая минималистичный I/O:

```bash
python big6_boot.py
```

Особенности:
- Ставка только на одно число за раз
- Минимальный вывод
- Ввод: число (1-6), ставка (1-500), 0 для выхода

## Автоматическое тестирование

```bash
make test                           # Запуск всех тестов
BIG6_SEED=42 python big6.py < tests/test1.input  # Детерминированный запуск
```

## Структура проекта

```
├── big6.bas          # Оригинал на BASIC
├── big6.py           # Основная версия (Linux/Windows)
├── big6_plan9.py     # Версия для Plan9
├── big6_boot.py      # Bootloader-симуляция
├── index.html        # Web-версия (Pyodide)
├── termux_setup.sh   # Скрипт установки для Android
├── test_big6.py      # Автотесты
├── tests/            # Тестовые данные
└── Makefile
```

## Пример работы

```
                          BIG6
                   CREATIVE COMPUTING
                 MORRISTOWN, NEW JERSEY

  THIS PROGRAM IS A DICE WHEEL GAME IN WHICH
YOU CAN BET ON ANY NUMBER BETWEEN ONE AND SIX
AND UP TO THREE NUMBERS.
  THE HOUSE LIMIT IS FROM $1 TO $500!!
TO END THIS PROGRAM TYPE THE WORD 'STOP'.
GOOD LUCK!

HOW MANY NUMBERS DO YOU WANT TO BET ON? 1
WHAT NUMBER? 3
WAGER? 100
THE LUCKY NUMBERS ARE: 1 3 5
YOU WIN 1 TIMES ON:3
YOU'RE AHEAD $100

HOW MANY NUMBERS DO YOU WANT TO BET ON? STOP

SO YOU WANT TO CASH IN YOUR CHIPS, I SEE!!
YOU WON EXACTLY $100!! NOT BAD !!!
```

## Оригинал

Оригинальный код на BASIC взят из [More BASIC Computer Games](https://www.roug.org/retrocomputing/languages/basic/morebasicgames).

