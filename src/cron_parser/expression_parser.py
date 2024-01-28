from abc import ABC, abstractmethod
from src.cron_parser.expression import (MinuteExpression, HourExpression, DayOfWeekExpression,
                                        DayOfMonthExpression, MonthExpression)
from src.cron_parser.constants import (Delimiters, FORMATS, MinuteLimits, HourLimits, MonthLimits,
                                       DayOfMonthLimits, DayOfWeekLimits, VALID_EXPRESSION_PARTS, COMMAND_INDEX, FORMAT_PADDING_SIZE)


class BaseExpressionParser(ABC):
    @abstractmethod
    def parse(self):
        raise NotImplementedError("parse function is not implemented")

    @abstractmethod
    def _validate(self):
        raise NotImplementedError("validate function is not implemented")


class SimpleExpressionParser(BaseExpressionParser):
    def __init__(self, raw_expression):
        self.raw_expression = raw_expression
        self.raw_expression_list = self.raw_expression.split(Delimiters.EXP_PART_DELIMITER.value)

        if len(self.raw_expression_list) != VALID_EXPRESSION_PARTS :
            raise Exception(f"raw_expression : {raw_expression} ,doesn't have {VALID_EXPRESSION_PARTS} parts")

        self.minute_expression = MinuteExpression(self.raw_expression_list[MinuteLimits.INDEX.value])
        self.hour_expression = HourExpression(self.raw_expression_list[HourLimits.INDEX.value])
        self.day_of_month_expression = DayOfMonthExpression(self.raw_expression_list[DayOfMonthLimits.INDEX.value])
        self.month_expression = MonthExpression(self.raw_expression_list[MonthLimits.INDEX.value])
        self.day_of_week_expression = DayOfWeekExpression(self.raw_expression_list[DayOfWeekLimits.INDEX.value])

        self.command = self.raw_expression_list[COMMAND_INDEX]

        self.all_expressions = [self.minute_expression,self.hour_expression, self.day_of_month_expression,
                                self.month_expression, self.day_of_week_expression]
        self.values = {}

    def _validate(self):
        pass

    def parse(self):
        for expression in self.all_expressions:
            self.values[expression.key] = expression.parse_values()
        self._validate()

    def get_runtime_info(self):
        output_string = ""
        for expression in self.all_expressions:
            output_string = output_string + f'{expression.key.ljust(FORMAT_PADDING_SIZE)}{" ".join([str(x) for x in self.values[expression.key]])}' + "\n"
            #print(f'{expression.key.ljust(FORMAT_PADDING_SIZE)}{" ".join([str(x) for x in self.values[expression.key]])}')
        output_string = output_string + f'{FORMATS.COMMAND.value.ljust(FORMAT_PADDING_SIZE)}{self.command}' + "\n"
        #print(f'{FORMATS.COMMAND.value.ljust(FORMAT_PADDING_SIZE)}{self.command}')
        return output_string



