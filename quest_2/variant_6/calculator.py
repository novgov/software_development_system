from typing import Callable, Optional


class Calculator:
    def __init__(self):
        self.accumulator: float = 0.0
        self.current_input: str = "0"
        self.pending_operator: Optional[str] = None
        self._reset_input: bool = False

    @property
    def display(self) -> str:
        return self.current_input

    def _flush_current(self) -> float:
        try:
            return float(self.current_input)
        except ValueError:
            # В случае некорректного ввода сбрасываем значение.
            self.current_input = "0"
            return 0.0

    def input_digit(self, digit: str) -> str:
        if self._reset_input:
            self.current_input = digit
            self._reset_input = False
            return self.display

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        return self.display

    def set_operator(self, operator: str) -> str:
        number = self._flush_current()
        if self.pending_operator is None:
            self.accumulator = number
        else:
            self.accumulator = self._apply_operator(self.accumulator, number, self.pending_operator)

        self.pending_operator = operator
        self.current_input = self._format(self.accumulator)
        self._reset_input = True
        return self.display

    def equal(self) -> str:
        number = self._flush_current()
        if self.pending_operator is not None:
            self.accumulator = self._apply_operator(self.accumulator, number, self.pending_operator)
            self.pending_operator = None
        else:
            self.accumulator = number
        self.current_input = self._format(self.accumulator)
        self._reset_input = True
        return self.display

    def apply_unary(self, func: Callable[[float], float], name: str) -> str:
        # Применяем функцию к текущему числу (если вводим) или к аккумулятору.
        target = self._flush_current() if not self._reset_input else self.accumulator
        try:
            result = func(target)
        except ZeroDivisionError:
            self.clear()
            self.current_input = "Ошибка: деление на 0"
            return self.display
        except ValueError:
            self.clear()
            self.current_input = f"Ошибка: {name}"
            return self.display

        self.accumulator = result
        self.current_input = self._format(result)
        self.pending_operator = None
        self._reset_input = True
        return self.display

    def clear(self) -> str:
        self.accumulator = 0.0
        self.current_input = "0"
        self.pending_operator = None
        self._reset_input = False
        return self.display

    @staticmethod
    def _apply_operator(left: float, right: float, operator: str) -> float:
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            if right == 0:
                raise ZeroDivisionError("Деление на ноль")
            return left / right
        raise ValueError(f"Неизвестный оператор: {operator}")

    @staticmethod
    def _format(value: float) -> str:
        # Убираем .0 для целых.
        if value.is_integer():
            return str(int(value))
        return f"{value:.8g}"

