def transform_data() -> None:
    players = [
        {"name": "alice", "scores": 2300, "achievements": [
            "first_kill", "speed_demon", "treasure_hunter",
            "collector", "perfectionist"
            ], "regions": "north", "status": "active"},

        {"name": "bob", "scores": 1800, "achievements": [
            "first_kill", "team_player", "explorer"
        ], "regions": "east", "status": "active"},

        {"name": "charlie", "scores": 2150, "achievements": [
            "first_kill", "level_10", "boss_slayer", "speed_runner",
            "collector", "strategist", "veteran"
        ], "regions": "central", "status": "active"},

        {"name": "diana", "scores": 3890, "achievements": [
            "level_10", "boss_slayer"
        ], "regions": "north", "status": "inactive"}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [player["name"] for player in players if
                    player["scores"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled = [player["scores"] * 2 for player in players]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [player["name"] for player in players if
                      player["status"] == "active"]
    print(f"Active players: {active_players}")

    print("")


if __name__ == "__main__":
    transform_data()
