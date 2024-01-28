from abc import ABC
from src.cron_parser.constants import (MinuteLimits, HourLimits, MonthLimits, DayOfMonthLimits, DayOfWeekLimits, FORMATS)
from src.cron_parser.utils import get_values_from_expression


class BaseExpressionPart(ABC):
    def __init__(self,expression, limits):
        self.limits = limits
        self.expression = expression
        self.values = []

    def _validate(self):
        if min(self.values) < self.limits.START_LIMIT.value or max(self.values) > self.limits.END_LIMIT.value:
            raise Exception(f"Expression: {self.expression} exceeding limits")

    def parse_values(self):
        self.values = get_values_from_expression(expression=self.expression, limits=self.limits)
        self._validate()
        return self.values


class MinuteExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.MINUTES.value
        super().__init__(expression, MinuteLimits)


class HourExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.HOUR.value
        super().__init__(expression, HourLimits)


class MonthExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.MONTH.value
        super().__init__(expression, MonthLimits)


class DayOfMonthExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.DAY_OF_MONTH.value
        super().__init__(expression, DayOfMonthLimits)


class DayOfWeekExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.DAY_OF_WEEK.value
        super().__init__(expression, DayOfWeekLimits)


class CommandExpression(BaseExpressionPart):
    def __init__(self, expression):
        self.key = FORMATS.COMMAND.value
        self.expression = expression

    def parse_values(self):
        return self.expression

    def _validate(self):
        pass
