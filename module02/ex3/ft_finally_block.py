def water_plants(plant_list) -> None:
    """Water plants with guaranteed cleanup in finally block."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test watering system with normal and error conditions."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)

    print("\nTesting with error...")
    bad_plants = ["tomato", None, "lett"]
    water_plants(bad_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
