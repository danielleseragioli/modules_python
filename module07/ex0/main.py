from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(dragon.get_card_info())

    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    game_state: dict = {"active_creatures": []}
    print(f"Play result: {dragon.play(game_state)}")

    goblin = {
        "name": "Goblin Warrior",
        "health": 3
    }
    print(f"\n{dragon.name} attaks {goblin['name']}:")
    attack_result = dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
