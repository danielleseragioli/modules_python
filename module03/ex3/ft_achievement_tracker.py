def analyze_achievements() -> None:
    """
    Analyzes and prints achievement statistics for three players.
    Demonstrates set operations: union, intersection, difference, and
    rare achievements.
    """

    print("=== Achievement Tracker System ===")

    alice: set[str] = {"first_kill", "level_10", "treasure_hunter",
                       "speed_demon"}
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {"level_10", "treasure_hunter", "boss_slayer",
                         "speed_demon", "perfectionist"}
    print(f"\nPlayer alice achievments: {alice}")
    print(f"Player bob achievments: {bob}")
    print(f"Player charlie achievments: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_achivements: set[str] = alice.union(bob, charlie)
    len_achivements: int = len(all_achivements)
    print(f"All unique achievements: {all_achivements}")
    print(f"Total unique achievements: {len_achivements}")

    common_archiv: set[str] = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common_archiv}")

    rare: set[str] = (
        (alice - bob - charlie) |
        (bob - alice - charlie) |
        (charlie - alice - bob)
    )
    print(f"Rare achievements (1 player): {rare}")

    common_alicebob: set[str] = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {common_alicebob}")

    unique_alice: set[str] = alice.difference(bob)
    print(f"Alice unique: {unique_alice}")

    unique_bob: set[str] = bob.difference(alice)
    print(f"Bob unique: {unique_bob}")


if __name__ == "__main__":
    """
    Entry point for achievement tracker demonstration.
    """
    analyze_achievements()
