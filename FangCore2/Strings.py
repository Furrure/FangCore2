"""
All String related FangCore2 tools
"""
from typing import *


def extract_string_arguments(*args: Union[str, list[Union[str, any]]]) -> list[str]:
    """
    When given strings, a list of strings, or a combination of both, will extract all of these strings into one list
    """
    string_arguments = []
    for arg in args:
        if isinstance(arg, list):
            for sub_arg in arg:
                string_arguments.append(str(sub_arg))
        else:
            string_arguments.append(str(arg))

    return string_arguments


def split(string: str, *args: Union[str, list[Union[str, any]]]) -> list[str]:
    """
    Separate a string by specified strings are characters
    """

    string = str(string)
    split_strings = extract_string_arguments(*args)






