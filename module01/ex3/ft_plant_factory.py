class Plant:
    """
    Stores information about a plant

    Attributes
    ----------
        name (str): name of the plant
        height (int): height of the plant in centimeters
        age (int): age of the plant in days

    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age_days = age
        self.initial_height = height


def ft_plant_factory():

    """
    Creates and displays multiple plant objects.
    
    Returns
    -------
    None
        This function does not return any value.
        It only prints information to the standard output.
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
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age_days} days)")
        len += 1

    print(f"\nTotal plants created: {len}")


if __name__ == "__main__":
    ft_plant_factory()
