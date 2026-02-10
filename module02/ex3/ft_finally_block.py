def water_plants(plant_list) -> None:
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
        # se der erro ou nao ele faz isso
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    try:
        water_plants()
    
