import sys


def command_quest() -> None:
    """
    Parses command-line arguments and prints program name and argument details.
    Demonstrates argument counting and formatting.
    """
    args: list[str] = sys.argv
    print("=== Command Quest ===")
    if len(args) < 2:
        print("No arguments provided!")
    program_name = args[0].replace('_', r'\_')
    print(f"Program name: {program_name}")
    if len(args) > 1:
        print(f"Arguments received: {len(args) - 1}")
    for i, arg in enumerate(args[1:], start=1):
        print(f"Argument {i}: {arg}")
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    """
    Entry point for command quest demonstration.
    """
    command_quest()
