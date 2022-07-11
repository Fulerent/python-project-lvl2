from yaml import Loader, load as yam_load
from json import load as json_load


def get_format(file_path):
    return file_path.split(".")[-1]


def pars(file_path):
    # give format-file
    format = get_format(file_path)

    with open(file_path) as f:
        if format == "yml" or format == "yaml":
            file = yam_load(f, Loader=Loader)
        elif format == "json":
            file = json_load(f)
            # print("file", file)
        else:
            return "I don't work with this format!"

    return file

