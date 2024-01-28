import re


def get_values_from_expression(expression, limits):
    if expression == "*":
        return list(range(limits.START_LIMIT.value, limits.END_LIMIT.value + 1))

    range_pattern_match = re.search(r"^(\d{1,2})-(\d{1,2})$", expression)
    if range_pattern_match:
        start_value, end_value = int(range_pattern_match.group(1)), int(range_pattern_match.group(2))
        return list(range(start_value, end_value + 1))

    list_pattern_match = re.search(r"^(\d{1,2})(,\d{1,2})*$", expression)
    if list_pattern_match:
        #values = [int(value) for value in list_pattern_match.group(0).split(",")]
        #print(f"expression : {expression} {list_pattern_match.group(0)} {values}")
        return [int(value) for value in list_pattern_match.group(0).split(",")]

    interval_pattern_match = re.search(r"^(\*|\d{1,2}-\d{1,2})/(\d{1,2})$", expression)
    if interval_pattern_match:
        interval = int(interval_pattern_match.group(2))
        possible_values = get_values_from_expression(
            interval_pattern_match.group(1),
            limits
        )
        return possible_values[::interval]
    raise Exception("Pattern not matching with Valid Patterns")
