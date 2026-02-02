class Plant:
    """
    Base class representing a plant with common attributes.

    Attributes
    ----------
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def base_info(self) -> str:
        """Return formatted string with height and age information."""
        return f"{self.height}cm, {self.age} days"

class Flower(Plant):
    """
    Represents a flower, inheriting from Plant.

    Attributes
    ----------
        color (str): The color of the flower.
    """
    def __init__(self, color: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def get_flower_info(self):
        """Display formatted information about the flower."""
        print(f"\n{self.name} (Flower): {self.base_info()}, {self.color} color")

class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.

    Attributes
    ----------
        trunk_diameter (int): The diameter of the tree trunk in centimeters.
    """
    def __init__(self,  trunk_diameter: int, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.trunk_diameter =  trunk_diameter

    def produce_shade(self):
        """Display the amount of shade the tree provides."""
        pi = 3.14159
        radius = self.trunk_diameter / 2
        shade_cm2 = pi * (radius ** 2)
        shade_m2 = shade_cm2 / 10000
        print(f"{self.name} provides {shade_m2:.0f} square meters of shade")
    
    def get_tree_info(self):
        """Display formatted information about the tree."""
        print(f"\n{self.name} (Tree): {self.base_info()}, {self.trunk_diameter} diameter")
    
class Vegetable(Plant):
    """
    Represents a vegetable, inheriting from Plant.

    Attributes
    ----------
        harvest_season (str): The season when the vegetable is harvested.
        nutritional_value (str): The primary nutritional value of the vegetable.
    """
    def __init__(self, harvest_season: str, nutritional_value: str, name: str, height: int, age: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_info(self):
        """Display the nutritional information of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")
    
    def get_veget_info(self):
        """Display formatted information about the vegetable."""
        print(f"\n{self.name} (Vegetable): {self.base_info()}, {self.harvest_season} harvest")

if __name__== "__main__":

    print("=== Garden Plant Types ===")

    rose = Flower("red", "Rose", 25, 30)
    rose.get_flower_info()
    rose.bloom()

    tulip = Flower("white", "tulip", 25, 30)
    tulip.get_flower_info()
    tulip.bloom()

    oak = Tree(50, "Oak", 500, 1825)
    oak.get_tree_info()
    oak.produce_shade()

    maple = Tree(80, "Maple", 600, 3500)
    maple.get_tree_info()
    maple.produce_shade()

    tomato = Vegetable("summer", "Vitamina C", "Tomato", 80, 90)
    tomato.get_veget_info()
    tomato.nutri_info()

    carrot = Vegetable("summer", "Vitamina A", "Tomato", 80, 90)
    carrot.get_veget_info()
    carrot.nutri_info()
