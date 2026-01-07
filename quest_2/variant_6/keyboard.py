"""Invoker: клавиатура, которая исполняет назначенные команды."""
from __future__ import annotations

from typing import Dict

from variant_6.commands import (
    ClearCommand,
    Command,
    DigitCommand,
    EqualCommand,
    OperatorCommand,
)
from .calculator import Calculator


class Keyboard:
    def __init__(self, calculator: Calculator):
        self.calculator = calculator
        self._fixed_buttons: Dict[str, Command] = {}
        self._custom_buttons: Dict[str, Command] = {}
        self._create_default_layout()

    def _create_default_layout(self):
        # Фиксированные цифровые клавиши.
        for digit in "0123456789":
            self._fixed_buttons[digit] = DigitCommand(self.calculator, digit)

        # Фиксированные арифметические операции.
        for op in ["+", "-", "*", "/"]:
            self._fixed_buttons[op] = OperatorCommand(self.calculator, op)

        self._fixed_buttons["="] = EqualCommand(self.calculator)
        self._fixed_buttons["C"] = ClearCommand(self.calculator)

    def assign_custom_button(self, name: str, command: Command):
        """Переназначить пользовательскую кнопку."""
        self._custom_buttons[name] = command

    def press(self, button: str) -> str:
        if button in self._fixed_buttons:
            return self._safe_execute(self._fixed_buttons[button])
        if button in self._custom_buttons:
            return self._safe_execute(self._custom_buttons[button])
        return f"Кнопка {button} не назначена"

    @staticmethod
    def _safe_execute(command: Command) -> str:
        try:
            return command.execute()
        except Exception as exc:  # noqa: BLE001
            return f"Ошибка: {exc}"

