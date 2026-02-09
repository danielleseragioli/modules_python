class Plant:
    """Base class for plants."""

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Plant that produces flowers."""

    def __init__(self, name: str, height: int, flower_color: str, is_blooming: bool):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = is_blooming

    def __str__(self) -> str:
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
        super().__init__(name, height, flower_color, is_blooming)
        self.prize_points = prize_points

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    """Garden containing multiple plants."""

    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant}")


class GardenManager:
    """Manages multiple gardens and analytics."""

    def __init__(self):
        self.gardens: dict[str, Garden] = {}

    # ---------- instance methods ----------

    def add_garden(self, owner: str) -> None:
        self.gardens[owner] = Garden(owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        if owner in self.gardens:
            self.gardens[owner].add_plant(plant)

    def grow_garden(self, owner: str) -> None:
        if owner in self.gardens:
            self.gardens[owner].grow_all()

    def report_garden(self, owner: str) -> None:
        if owner in self.gardens:
            self.gardens[owner].report()

    def report_all(self) -> None:
        for garden in self.gardens.values():
            garden.report()

    # ---------- nested helper ----------

    class GardenStats:
        """Helper class for garden statistics."""

        @staticmethod
        def calculate_total_plants(garden: Garden) -> int:
            return len(garden.plants)

        @staticmethod
        def calculate_total_growth(garden: Garden) -> int:
            return sum(plant.height for plant in garden.plants)

        @staticmethod
        def count_plant_types(garden: Garden) -> dict[str, int]:
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
            score = 0
            for plant in garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return score

    # ---------- class method ----------

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    # ---------- static utility ----------

    @staticmethod
    def validate_plant_height(plant: Plant) -> bool:
        return plant.height > 0


# MAIN ======================

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

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

    print(f"Height validation test: {GardenManager.validate_plant_height(sunflower)}")

    alice_score = stats.calculate_garden_score(alice_garden)

    manager.add_plant_to_garden("Bob", Plant("Cactus", 92))
    bob_garden = manager.gardens["Bob"]
    bob_score = stats.calculate_total_growth(bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {len(manager.gardens)}")
