# BIG6 - Dice Wheel Game

Порт классической игры BIG6 из сборника "More BASIC Computer Games" (Creative Computing, Morristown, New Jersey).

## Описание игры

BIG6 — это азартная игра с игральными костями. Игрок может делать ставки на числа от 1 до 6, выбирая от 1 до 3 чисел за раунд. Бросаются три кости, и если выпадает загаданное число, игрок выигрывает ставку, умноженную на количество совпадений. Если число не выпало — ставка проиграна.

Лимит ставок: от $1 до $500.

Для выхода из игры введите `STOP`.

## Платформы

- **Linux** — Python 3.10+
- **Windows** — Python 3.10+
- **Web** — браузер с поддержкой JavaScript (через Pyodide)

## Сборка и запуск

### Linux / Windows

```bash
# Запуск игры
make run
# или
python3 big6.py

# Запуск тестов
make test
```

### Web-версия

```bash
make web
```

Откройте в браузере: http://localhost:8000

## Автоматическое тестирование

Тесты проверяют соответствие поведения портированной версии оригиналу на BASIC. Каждый тест содержит:
- `tests/*.input` — входные данные (диалог игрока)
- `tests/*.expected` — эталонный вывод

Для детерминированного тестирования используется переменная окружения `BIG6_SEED`:

```bash
BIG6_SEED=42 python3 big6.py < tests/test1.input
```

## Структура проекта

```
.
├── big6.bas          # Оригинал на BASIC
├── big6.py           # Порт на Python
├── test_big6.py      # Автотесты
├── index.html        # Web-версия (Pyodide)
├── Makefile          # Сборка
├── tests/            # Тестовые данные
│   ├── test1.input
│   ├── test1.expected
│   └── ...
└── README.MD
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
