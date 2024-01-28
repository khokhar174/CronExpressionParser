from enum import Enum

VALID_EXPRESSION_PARTS = 6
COMMAND_INDEX=-1
FORMAT_PADDING_SIZE = 14

class ParserTypes(Enum):
    Simple = "simple"
    Default = "default"


class FORMATS(Enum):
    MINUTES = "minute"
    HOUR = "hour"
    DAY_OF_MONTH = "day of month"
    MONTH = "month"
    DAY_OF_WEEK = "day of week"
    COMMAND = "command"


class Delimiters(Enum):
    FREQ_DELIMITER = "/"
    LIST_DELIMITER = ","
    RANGE_DELIMITER = "-"
    WILDCARD = "*"
    EXP_PART_DELIMITER = " "


class MinuteLimits(Enum):
    START_LIMIT=0
    END_LIMIT=59
    INDEX = 0


class HourLimits(Enum):
    START_LIMIT=0
    END_LIMIT=23
    INDEX = 1


class DayOfMonthLimits(Enum):
    START_LIMIT=1
    END_LIMIT=31
    INDEX = 2


class MonthLimits(Enum):
    START_LIMIT=1
    END_LIMIT=12
    INDEX = 3


class DayOfWeekLimits(Enum):
    START_LIMIT=1
    END_LIMIT=7
    INDEX = 4

