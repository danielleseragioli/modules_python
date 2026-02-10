
def garden_operations(error_type: str) -> None:
    try:
        if error_type == "value":
            int("abc")
        elif error_type == "division":
            _ = 42 / 0
        elif error_type == "file":
            open("missing.txt", "r")
        elif error_type == "key":
            plants = {"tulip": "white", "rose": "red"}
            _ = plants["missing_plant"]
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    try:
        if error_type == "mutiple":
            raise TypeError("multiple error")
    except (NameError, PermissionError, ReferenceError, TypeError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:

    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("value")

    print("\nTesting ZeroDivisionError...")
    garden_operations("division")

    print("\nTesting FileNotFoundError...")
    garden_operations("file")

    print("\nTesting KeyError...")
    garden_operations("key")

    print("\nTesting multiple errors together...")
    garden_operations("mutiple")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
