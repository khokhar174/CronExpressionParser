import pytest
from src.cron_parser.expression import MinuteExpression, MonthExpression, HourExpression
from src.cron_parser.expression_parser import SimpleExpressionParser


def test_interval_exp_part_parse_valid():
    exp = MinuteExpression("*/15")
    exp.parse_values()
    print(exp.values)
    assert exp.values == [0, 15, 30, 45]


def test_base_minute_exp_part_parse_valid():
    exp = MinuteExpression("*")
    exp.parse_values()
    print()
    assert exp.values == list(range(0,60))


def test_base_hour_exp_part_parse_valid():
    exp = HourExpression("*")
    exp.parse_values()
    assert exp.values == list(range(0,24))


def test_range_exp_part_parse_valid():
    exp = MinuteExpression("1-7")
    exp.parse_values()
    assert exp.values == [1, 2, 3, 4, 5,  6, 7]


def test_list_exp_part_parse_valid():
    exp = MinuteExpression("1,2,3,7")
    exp.parse_values()
    assert exp.values == [1, 2, 3,7]


def test_month_exp_limit_valid():
    exp = MonthExpression("*/32")
    assert exp.parse_values() == [1]


def test_minute_exp_limit_valid():
    exp = MinuteExpression("*/32")
    exp.parse_values()
    print(exp.values)
    assert exp.values == [0, 32]


def test_hour_exp_limit_invalid():
    exp = HourExpression("1-34")
    with pytest.raises(Exception):
        exp.parse_values()

def test_hour_exp_limit_invalid_2():
    exp = HourExpression("1$3")
    with pytest.raises(Exception):
        exp.parse_values()


def test_expression_parse_invalid():
    cron_expression = "*-/15 0 1,15 * 1-5 /usr/bin/find extra_field"
    with pytest.raises(Exception):
        expression = SimpleExpressionParser(cron_expression)
        expression.parse()


def test_expression_parse_output_valid():
    cron_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
    expression = SimpleExpressionParser(cron_expression)
    expression.parse()
    output = expression.get_runtime_info()
    expected_output = """minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find
"""
    print(output)
    print(expected_output)
    assert output == expected_output