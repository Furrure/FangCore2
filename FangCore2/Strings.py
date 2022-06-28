"""
All String related FangCore2 tools
"""
from typing import *


def extract_string_arguments(*args: Union[str, list[Union[str, any]]]) -> tuple[str]:
    """
    When given strings, a list of strings, or a combination of both, will extract all of these strings into one list.
    This function is used by most `FangCore2.Strings` functions and methods.
    """
    string_arguments = []
    for arg in args:
        if isinstance(arg, list):
            for sub_arg in arg:
                string_arguments.append(str(sub_arg))
        else:
            string_arguments.append(str(arg))

    return tuple(string_arguments)


def split(string: str, *args: Union[str, list[Union[str, any]]]) -> tuple[str]:
    """
    Separate a string by specified strings or characters.

    Order of arguments is the order of character detection and splitting.
    ex: `split("Hello", "ll", "ell") => ["He", "o"]`
    """

    string = str(string)  # Input string

    split_strings = extract_string_arguments(*args)  # Strings that the input string will be split by

    output = []  # The result of the split operation

    working_word = ""  # The next word that is being appended to until a split sequence is reached

    char_index = 0  # The current character that is being read
    while not char_index >= len(string):
        for splitter in split_strings:
            if len(splitter) > len(string[char_index:]):  # Check if the length even matches
                continue
            elif string[char_index:char_index+len(splitter)] == splitter:  # Check for a match in the string and break if so
                if working_word.strip() != "":
                    output.append(working_word)
                char_index = char_index+len(splitter)
                working_word = ""
                break
        if not char_index >= len(string):
            working_word += string[char_index]
        char_index += 1

    if working_word.strip() != "":
        output.append(working_word)

    return tuple(output)


def index_all(string: str, *args: Union[str, list[Union[str, any]]]) -> tuple[int]:
    """
    Index all the occurrences of the given strings

    If there are multiple matches at one index, the index is only included once.
    """

    string = str(string)  # Input string

    index_strings = extract_string_arguments(*args)  # Strings that the input string will be indexed

    output = []  # The result of the index operation

    char_index = 0  # The current character that is being read
    while not char_index >= len(string):
        for indexer in index_strings:
            if len(indexer) > len(string[char_index:]):  # Check if the length even matches
                continue
            elif string[char_index:char_index + len(indexer)] == indexer:  # Check for a match in the string and break if so
                if char_index not in output:
                    output.append(char_index)
                break
        char_index += 1

    return tuple(output)








