class Plant:
    """Base class for plants."""

    def __init__(self, name: str, height: int):
        """
        Initialize a Plant instance.
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """
        Increase the plant's height by 1 cm and print a message.
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        """
        Return a string representation of the plant.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that produces flowers."""

    def __init__(self, name: str, height: int,
                 flower_color: str, is_blooming: bool):
        """
        Initialize a FloweringPlant instance.
        """
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = is_blooming

    def __str__(self) -> str:
        """
        Return a string representation of the flowering plant,
        including bloom status.
        """
        status = "blooming" if self.is_blooming else "not blooming"
        base = super().__str__()
        return f"{base}, {self.flower_color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Plant with prize-winning flowers."""

    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        is_blooming: bool,
        prize_points: int,
    ):
        """
        Initialize a PrizeFlower instance.
        """
        super().__init__(name, height, flower_color, is_blooming)
        self.prize_points = prize_points

    def __str__(self) -> str:
        """
        Return a string representation of the prize flower,
        including prize points.
        """
        base = super().__str__()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    """Garden containing multiple plants."""

    def __init__(self, owner: str):
        """
        Initialize a Garden instance.
        """
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden and print a confirmation message.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """
        Make all plants in the garden grow by 1 cm and print a message.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        """
        Print a report of all plants in the garden.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")


class GardenManager:
    """Manages multiple gardens and analytics."""

    def __init__(self):
        """
        Initialize a GardenManager instance.
        """
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, owner: str) -> None:
        """
        Add a new garden for the specified owner.
        """
        self.gardens[owner] = Garden(owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """
        Add a plant to the specified owner's garden.
        """
        if owner in self.gardens:
            self.gardens[owner].add_plant(plant)

    def grow_garden(self, owner: str) -> None:
        """
        Make all plants in the specified owner's garden grow by 1 cm.
        """
        if owner in self.gardens:
            self.gardens[owner].grow_all()

    def report_garden(self, owner: str) -> None:
        """
        Print a report for the specified owner's garden.
        """
        if owner in self.gardens:
            self.gardens[owner].report()

    def report_all(self) -> None:
        """
        Print reports for all gardens managed by the GardenManager.
        """
        for garden in self.gardens.values():
            garden.report()

    class GardenStats:
        """Helper class for garden statistics."""

        @staticmethod
        def calculate_total_plants(garden: Garden) -> int:
            """
            Calculate the total number of plants in a garden.

            Parameters
            ----------
            garden : Garden
                The garden to analyze.

            Returns
            -------
            int
                The total number of plants.
            """
            return len(garden.plants)

        @staticmethod
        def calculate_total_growth(garden: Garden) -> int:
            """
            Calculate the total height of all plants in a garden.

            Parameters
            ----------
            garden : Garden
                The garden to analyze.

            Returns
            -------
            int
                The sum of all plant heights.
            """
            return sum(plant.height for plant in garden.plants)

        @staticmethod
        def count_plant_types(garden: Garden) -> dict[str, int]:
            """
            Count the number of each plant type in a garden.

            Parameters
            ----------
            garden : Garden
                The garden to analyze.

            Returns
            -------
            dict[str, int]
                A dictionary with counts for each plant type.
            """
            counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    counts["PrizeFlower"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["FloweringPlant"] += 1
                elif isinstance(plant, Plant):
                    counts["Plant"] += 1
            return counts

        @staticmethod
        def calculate_garden_score(garden: Garden) -> int:
            """
            Calculate a score for the garden based on plant
            heights and prize points.

            Parameters
            ----------
            garden : Garden
                The garden to analyze.

            Returns
            -------
            int
                The calculated garden score.
            """
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return score

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        """
        Create a GardenManager and add gardens for each owner in the list.

        Parameters
        ----------
        owners : list[str]
            List of garden owner names.

        Returns
        -------
        GardenManager
            The initialized GardenManager instance.
        """
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    @staticmethod
    def validate_plant_height(plant: Plant) -> bool:
        """
        Validate that a plant's height is greater than zero.

        Parameters
        ----------
        plant : Plant
            The plant to validate.

        Returns
        -------
        bool
            True if the plant's height is greater than zero, False otherwise.
        """
        return plant.height > 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

    print("\n")
    manager.grow_garden("Alice")
    manager.report_garden("Alice")

    stats = GardenManager.GardenStats
    alice_garden = manager.gardens["Alice"]

    total_plants = stats.calculate_total_plants(alice_garden)
    total_height = stats.calculate_total_growth(alice_garden)
    initial_total = 100 + 25 + 50
    total_growth = total_height - initial_total
    types = stats.count_plant_types(alice_garden)

    print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
    print(
        f"Plant types: {types['Plant']} regular, "
        f"{types['FloweringPlant']} flowering, "
        f"{types['PrizeFlower']} prize flowers"
    )

    print("Height validation test: "
          + f"{GardenManager.validate_plant_height(sunflower)}")

    alice_score = stats.calculate_garden_score(alice_garden)

    manager.add_plant_to_garden("Bob", Plant("Cactus", 92))
    bob_garden = manager.gardens["Bob"]
    bob_score = stats.calculate_total_growth(bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {len(manager.gardens)}")
