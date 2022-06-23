import FangCore2.Strings


def strings_extract_string_arguments():
    try:
        result = FangCore2.Strings.extract_string_arguments("hello", ["test", "test"], "hello")
    except Exception as exception:
        raise exception
    if result != ["hello", "test", "test", "hello"]:
        raise RuntimeError("Incorrect result")


test_functions = {
    "Strings.extract_string_arguments" : strings_extract_string_arguments

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
