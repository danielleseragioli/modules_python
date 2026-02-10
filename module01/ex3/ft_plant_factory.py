class Plant:
    """
    Stores information about a plant.

    Attributes
    ----------
    name : str
        Name of the plant.
    height : int
        Height of the plant in centimeters.
    age_days : int
        Age of the plant in days.
    initial_height : int
        Initial height of the plant in centimeters.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant object.
        """
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.initial_height = height


def ft_plant_factory():

    """
    Creates and displays multiple Plant objects.

    This function instantiates several Plant objects, prints their details,
    and displays the total number of plants created.

    Returns
    -------
    None
        This function does not return any value. 
        It only prints information to
        the standard output.
    """
    factory = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")

    len = 0
    for plant in factory:
        print(f"Created: {plant.name} ({plant.height}cm, "
              f"{plant.age_days} days)")
        len += 1

    print(f"\nTotal plants created: {len}")


if __name__ == "__main__":
    ft_plant_factory()
