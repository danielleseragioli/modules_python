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
        """
        Initialize a Plant instance.
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def base_info(self) -> str:
        """
        Return a formatted string with the plant's height and age information.

        Returns
        -------
        str
            A string containing the height and age of the plant.
        """
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Represents a flower, inheriting from Plant.

    Attributes
    ----------
        color (str): The color of the flower.
    """
    def __init__(self, color: str, name: str, height: int, age: int):
        """
        Initialize a Flower instance.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Print a message indicating the flower is blooming.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_flower_info(self):
        """
        Print formatted information about the flower, including
        name, height, age, and color.
        """
        print(f"\n{self.name} (Flower): "
              + f"{self.base_info()}, {self.color} color")


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.

    Attributes
    ----------
        trunk_diameter (int): The diameter of the tree trunk in centimeters.
    """
    def __init__(self,  trunk_diameter: int, name: str, height: int, age: int):
        """
        Initialize a Tree instance.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Print the amount of shade the tree provides, calculated from
        trunk diameter and height.
        """
        shade = (self.trunk_diameter * self.height) // 320
        print(f"{self.name} provides {shade:.2f} square meters of shade")

    def get_tree_info(self):
        """
        Print formatted information about the tree, including name,
        height, age, and trunk diameter.
        """
        print(f"\n{self.name} (Tree): {self.base_info()}, "
              + f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """
    Represents a vegetable, inheriting from Plant.

    Attributes
    ----------
        harvest_season (str): The season when the vegetable is harvested.
        nutritional_value (str): The primary nutritional value of
        the vegetable.
    """
    def __init__(self, harvest_season: str, nutritional_value: str,
                 name: str, height: int, age: int):
        """
        Initialize a Vegetable instance.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_info(self):
        """
        Print the nutritional information of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_veget_info(self):
        """
        Print formatted information about the vegetable, including name,
        height, age, and harvest season.
        """
        print(f"\n{self.name} (Vegetable): {self.base_info()},"
              + f"{self.harvest_season} harvest")


if __name__ == "__main__":

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

    maple = Tree(1000, "Maple", 500, 1825)
    maple.get_tree_info()
    maple.produce_shade()

    tomato = Vegetable("summer", "Vitamina C", "Tomato", 80, 90)
    tomato.get_veget_info()
    tomato.nutri_info()

    carrot = Vegetable("summer", "Vitamina A", "Tomato", 80, 90)
    carrot.get_veget_info()
    carrot.nutri_info()
