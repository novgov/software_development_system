"""Команды для настраиваемого калькулятора.

Реализуется паттерн Command: каждая кнопка клавиатуры инкапсулирует
собственное действие и знает, как вызвать его у получателя (Calculator).
"""
from abc import ABC, abstractmethod
from typing import Callable, Optional

from variant_6.calculator import Calculator


class Command(ABC):
    """Базовая команда."""

    @abstractmethod
    def execute(self) -> str:
        """Выполнить действие и вернуть отображаемое значение."""


class DigitCommand(Command):
    """Команда ввода цифры."""

    def __init__(self, calculator: Calculator, digit: str):
        self.calculator = calculator
        self.digit = digit

    def execute(self) -> str:
        return self.calculator.input_digit(self.digit)


class OperatorCommand(Command):
    """Команда выбора бинарного оператора (+, -, *, /)."""

    def __init__(self, calculator: Calculator, operator: str):
        self.calculator = calculator
        self.operator = operator

    def execute(self) -> str:
        return self.calculator.set_operator(self.operator)


class EqualCommand(Command):
    """Команда вычисления выражения."""

    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self) -> str:
        return self.calculator.equal()


class ClearCommand(Command):
    """Команда сброса состояния."""

    def __init__(self, calculator: Calculator):
        self.calculator = calculator

    def execute(self) -> str:
        return self.calculator.clear()


class UnaryFunctionCommand(Command):
    """Команда для настраиваемых (пользовательских) кнопок."""

    def __init__(self, calculator: Calculator, name: str, func: Callable[[float], float]):
        self.calculator = calculator
        self.name = name
        self.func = func

    def execute(self) -> str:
        return self.calculator.apply_unary(self.func, self.name)

