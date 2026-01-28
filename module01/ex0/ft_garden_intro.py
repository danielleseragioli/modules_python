def ft_garden_intro() -> None:
    """
        Prints a welcome header followed by information
        about a plant (name, height, and age),
        and then displays a closing message.

        Returns
        -------
        None
            This function does not return any value.
            It only outputs text to the standard output.
    """
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
