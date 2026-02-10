
class Plant:
    """
    Class that stores information about a plant.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int):
        """
        Initializes a new instance of Plant.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in centimeters.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """
    Displays the data of the registered garden plants.

    Creates Plant objects with predefined values and prints
    the name, height, and age of each plant.

    Returns:
        None: This function only prints information to standard output.
    """
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, "
          + f"{sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    ft_garden_data()
