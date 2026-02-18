class GardenError(Exception):
    """Base exception for garden management errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-specific errors."""
    pass


class WaterError(GardenError):
    """Exception for water management errors."""
    pass


class GardenManager:
    """Manages garden plants and water resources."""

    def __init__(self):
        """Initialize garden with empty plants and full water tank."""
        self.plants = {}
        self.water_tank = 100

    def water_plants(self) -> None:
        """Water all plants with cleanup in finally block."""
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                self.plants[plant]["water"] += 5
                self.water_tank -= 5
                print(f"Watering {plant} - success")
        except WaterError as error:
            print(f"Caught GardenError: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def add_plant(self, name) -> str:
        """Add a new plant to the garden."""
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plants[name] = {"water": 0, "sun": 0}
        return f"Added {name} successfully"

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        """Check and validate plant health parameters."""
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             + "is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             + " is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             + "is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             + "is too high (max 12)")
        return (f"{plant_name}: healthy (water: {water_level}, "
                + f"sun: {sunlight_hours})")


def test_garden_management():
    """Test the complete garden management system."""
    print("=== Garden Management System ===\n")

    manager = GardenManager()
    print("Adding plants to garden...")
    try:
        print(manager.add_plant("tomato"))
        print(manager.add_plant("lettuce"))
        print(manager.add_plant(""))
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")
    manager.water_plants()
    print("\nChecking plant health...")
    try:
        result = manager.check_plant_health("tomato", 5, 8)
        print(result)
    except (PlantError, WaterError, ValueError) as e:
        print(f"Error: {e}")

    try:
        result = manager.check_plant_health("lettuce", 15, 8)
        print(result)
    except (PlantError, WaterError, ValueError) as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_tank = 2
        manager.water_plants()
    except WaterError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
