class Plant:
    """
    Represents a plant with a name, height, and age in days.

    Attributes:
        name (str): The name of the plant (capitalized).
        height (int): The current height of the plant in centimeters.
        age_days (int): The current age of the plant in days.
        initial_height (int): The height of the plant at creation.

    Methods:
        grow(): Increases the plant's height by 1 cm.
        age(): Increases the plant's age by 1 day.
        get_info(): Returns a string with the plant's name, height, and age.
    """

    def __init__(self, name: str, height: int, age: int):
        """Initialize plant with name, height, and age."""
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.initial_height = height

    def grow(self):
        """Increase height by 1 cm."""
        self.height += 1

    def age(self):
        """Increase age by 1 day."""
        self.age_days += 1

    def get_info(self) -> str:
        """Return plant's name, height, and age."""
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def ft_plant_growth() -> None:
    """
    Simulate a week of growth for three different plants:
    Rose, Sunflower, and Cactus.

    For each day, each plant grows by 1 cm and ages by 1 day.
    The function prints
    the initial and final state of each plant, as well as the total growth of
    the rose.
    """
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print(cactus.get_info())

    for day in range(6):
        rose.grow()
        rose.age()
        sunflower.grow()
        sunflower.age()
        cactus.grow()
        cactus.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print(cactus.get_info())

    print(f"Growth this week: +{rose.height - rose.initial_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
