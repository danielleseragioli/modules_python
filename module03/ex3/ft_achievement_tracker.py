def analyze_achievements() -> None:

    print("=== Achievement Tracker System ===")

    alice: set[str] = {"first_kill", "level_10", "treasure_hunter",
                       "speed_demon"}
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {"level_10", "treasure_hunter", "boss_slayer",
                         "speed_demon", "perfectionist"}
    print(f"Player alice achievments: {alice}")
    print(f"Player bob achievments: {bob}")
    print(f"Player charlie achievments: {charlie}")

    print("=== Achievement Analytics ===")
    all_achivements = alice.union(bob, charlie)
    len_achivements = len(all_achivements)
    print(f"All unique achievements: {all_achivements}")
    print(f"Total unique achievements: {len_achivements}")

    common_archiv = alice.intersection(bob, charlie)
    print(f"\nCommon to all players: {common_archiv}")
    print(f"Rare achievements (1 player):")


if __name__ == "__main__":
    analyze_achievements()
