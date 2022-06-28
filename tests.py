import FangCore2.Strings


def strings_extract_string_arguments():
    try:
        result = FangCore2.Strings.extract_string_arguments("hello", ["test", "test"], "hello")
    except Exception as exception:
        raise exception
    if result != ["hello", "test", "test", "hello"]:
        raise RuntimeError("Incorrect result")


def strings_split():
    try:
        result = FangCore2.Strings.split("hello there!", " ", ["e!", "hel"])
    except Exception as exception:
        raise exception
    if result != ["lo", "ther"]:
        raise RuntimeError("Incorrect result")


def strings_index_all():
    try:
        result = FangCore2.Strings.index_all("hello there!", " ", ["e!", "hel"])
    except Exception as exception:
        raise exception
    if result != [0, 5, 10]:
        raise RuntimeError("Incorrect result")


test_functions = {
    "Strings.extract_string_arguments": strings_extract_string_arguments,
    "Strings.split": strings_split,
    "Strings.index_all": strings_index_all

}

for name, function in test_functions.items():
    print(f"Testing {name}...", end="")
    try:
        function()
        print(f"SUCCESS", end="")
    except Exception as exc:
        print(f"ERROR in {name}: {exc}", end="")
    print()
    print()
