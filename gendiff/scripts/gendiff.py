#!/usr/bin/env python
from gendiff import cli
import sys


def main():
    r = cli.parsing_cli()
    sys.stdout.write(r)


if __name__ == "main":
    main()
