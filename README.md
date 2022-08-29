
[![Actions Status](https://github.com/Fulerent/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Fulerent/python-project-lvl2/actions) [![Actions Status](https://github.com/Fulerent/python-project-lvl2/workflows/tests-check/badge.svg)](https://github.com/Fulerent/python-project-lvl2/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/426fe096098a4173df9e/maintainability)](https://codeclimate.com/github/Fulerent/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/426fe096098a4173df9e/test_coverage)](https://codeclimate.com/github/Fulerent/python-project-lvl2/test_coverage)

This Cli-program help you to diffent two files which have formats **.json** or **.yaml**.

Use case:

Install `pip install gendiff`

Get help `gendiff -h`

```
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
first_file
second_file

optional arguments:
-h, --help   show this help message and exit
```
Run `gendiff <file_path1> <file_path2>`

```
{
        - follow : False
        host : hexlet.io
        - int : 5
        + int : 10
        - optional : None
        timeout : 20.15
        + verbose : True
}
```
