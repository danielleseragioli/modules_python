class Plant:
    """
    Stores information about a plant

    Attributes
    ----------
        name (str): name of the plant
        height (int): height of the plant in centimeters
        age (int): age of the plant in days

    """
    def __init__ (self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def ft_garden_data()->None:
    """
    Display registered garden plant data.

    This function creates Plant objects with predefined values
    and prints their name, height, and age.

    Returns
    -------
    None
        This function does not return any value. It only prints
        information to the standard output.
    """
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")

if __name__ == "__main__":
    ft_garden_data()