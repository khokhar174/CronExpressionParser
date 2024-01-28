# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from src.cron_parser.parser_factory import ExpressionParserFactory


if __name__ == "__main__":
    if(len(sys.argv) <=1 ):
        raise Exception("Arguments missing")
    #cron_lines = [
    #    "*/15 0 1,15 * 1-5 /usr/bin/find",
    #    "0 2 * * * /usr/bin/some_command",
    #    "0 2 * 1,2,3,4,7 * /usr/bin/some_command"
    #]
    cron_line = sys.argv[1]
    parser_type = None if len(sys.argv)==2 else sys.argv[2]
    print("expression : {}".format(cron_line))
    exp_parser = ExpressionParserFactory().get_parser(cron_line, parser_type)
    exp_parser.parse()
    print(exp_parser.get_runtime_info())
