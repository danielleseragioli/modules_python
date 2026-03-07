import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main() -> None:
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    fire_result: str = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire_result}")

    print("\nMethod 2 - Specific function import:")
    water_result: str = alchemy.elements.create_water()
    print(f"create_water(): {water_result}")

    print("\nMethod 3 - Aliased import:")
    heal_result: str = heal()
    print(f"heal(): {heal_result}")

    print("\nMethod 4 - Multiple imports:")
    earth_result: str = alchemy.elements.create_earth()
    fire_result: str = alchemy.elements.create_fire()
    strength_result: str = alchemy.potions.strength_potion()
    print(f"create_earth(): {earth_result}")
    print(f"create_fire(): {fire_result}")
    print(f"strength_potion(): {strength_result}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()