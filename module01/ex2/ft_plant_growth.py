#from ft_garden_data.py import Plant

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

    def grow(self):
        self.height += 1

    def age(self):
        self.age_days += 1

    def get_info(self)->str:
        """
        Returns formatted information about the plant.
        
        Returns
        --------
            A string containing the plant's name, height, and age
        """
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def ft_plant_growth():

    """ Simulates a week of growth """

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
 