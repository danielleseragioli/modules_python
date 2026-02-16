class GardenError(Exception):
    """
    Base exception class for garden-related errors.

    This is the parent class for all custom garden exceptions,
    allowing for hierarchical error handling.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related errors.

    Inherits from GardenError for hierarchical exception handling.
    """
    pass


class WaterError(GardenError):
    """
    Exception raised for water management errors.

    Inherits from GardenError for hierarchical exception handling.
    """
    pass


def test_custom_errors():
    """Test custom exception handling and hierarchy."""
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")
