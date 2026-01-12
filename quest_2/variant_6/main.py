"""Демонстрация паттерна Команда для настраиваемой клавиатуры калькулятора."""
from __future__ import annotations

import math
from typing import Iterable

from quest_2.variant_6.calculator import Calculator
from quest_2.variant_6.commands import UnaryFunctionCommand
from quest_2.variant_6.keyboard import Keyboard


def _print_sequence(title: str, keyboard: Keyboard, sequence: Iterable[str]):
    print(f"\n{title}")
    for button in sequence:
        value = keyboard.press(button)
        print(f"'{button}' -> {value}")


def build_keyboard() -> Keyboard:
    calc = Calculator()
    keyboard = Keyboard(calc)

    # Настраиваемые кнопки.
    keyboard.assign_custom_button("F1", UnaryFunctionCommand(calc, "квадрат", lambda x: x * x))
    keyboard.assign_custom_button("F2", UnaryFunctionCommand(calc, "корень", math.sqrt))
    keyboard.assign_custom_button("F3", UnaryFunctionCommand(calc, "смена знака", lambda x: -x))
    keyboard.assign_custom_button("F4", UnaryFunctionCommand(calc, "обратное число", lambda x: 1 / x))
    return keyboard


def demo():
    keyboard = build_keyboard()

    _print_sequence(
        "Суммирование 10 + 5 =",
        keyboard,
        ["1", "0", "+", "5", "="],
    )

    _print_sequence(
        "Кнопка F1 (квадрат) применена к результату",
        keyboard,
        ["F1"],
    )

    _print_sequence(
        "Кнопка F2 (корень) затем смена знака (F3)",
        keyboard,
        ["F2", "F3"],
    )

    _print_sequence(
        "Очистка и деление 8 / 2 =",
        keyboard,
        ["C", "8", "/", "2", "="],
    )

    # Переназначение пользовательской кнопки на лету.
    calc = keyboard.calculator
    keyboard.assign_custom_button("F3", UnaryFunctionCommand(calc, "куб", lambda x: x**3))
    _print_sequence(
        "После переназначения F3 выполняет возведение в куб",
        keyboard,
        ["F3"],
    )


if __name__ == "__main__":
    demo()

