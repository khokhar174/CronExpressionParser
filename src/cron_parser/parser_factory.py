from src.cron_parser.constants import ParserTypes
from src.cron_parser.expression_parser import SimpleExpressionParser


PARSER_MAP = {
    ParserTypes.Simple.value: SimpleExpressionParser,
    ParserTypes.Default.value: SimpleExpressionParser
}


class ExpressionParserFactory():
    @staticmethod
    def get_parser(raw_expression, parser_type):
        if parser_type and parser_type in PARSER_MAP.keys():
            return PARSER_MAP[parser_type](raw_expression)
        return PARSER_MAP[ParserTypes.Default.value](raw_expression)

