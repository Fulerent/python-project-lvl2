import argparse
from gendiff.diff_files import generate_diff
from gendiff.parser_files import pars


def parsing_cli():
    parser = argparse.ArgumentParser(
        description="Compares two configuration\
    files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", nargs="?", help="set format of output")
    args = parser.parse_args()

    if "-h" in args:
        parser.print_help()
    else:
        result = generate_diff(pars(args.first_file), pars(args.second_file))

        return result
