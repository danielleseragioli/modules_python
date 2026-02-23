def transform_data() -> None:
    """
    Demonstrates list, dict, and set comprehensions for analytics dashboard.
    Processes player data and prints various statistics and transformations.
    """
    players: list[dict[str, any]] = [
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

        {"name": "diana", "scores": 2050, "achievements": [
            "level_10", "boss_slayer"
        ], "regions": "north", "status": "inactive"}
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scores: list[str] = [player["name"] for player in players
                              if player["scores"] > 2000]
    print(f"High scorers (>2000): {high_scores}")
    scores_doubled: list[int] = [player["scores"] * 2 for player in players]
    print(f"Scores doubled: {scores_doubled}")
    active_players: list[str] = [player["name"] for player in players
                                 if player["status"] == "active"]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {p["name"]: p["scores"]
                                     for p in players[:3]}
    print(f"Player scores: {player_scores}")

    score: list[int] = [p["scores"] for p in players]
    score_categories: dict[str, int] = {
        "high": len([p for p in score if p > 2100]),
        "medium": len([p for p in score if 1900 <= p <= 2100]),
        "low": len([p for p in score if p < 1900])
    }
    print(f"Score categories: {score_categories}")

    achiev_counts: dict[str, int] = {p["name"]: len(p["achievements"])
                                     for p in players}
    print(f"Achievement counts: {achiev_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players: set[str] = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achiev: list[str] = [achievement for p in players
                             for achievement in p["achievements"]]
    unique_achiev: set[str] = {p for p in all_achiev
                               if all_achiev.count(p) == 1}
    print(f"Unique achievements: {unique_achiev}")

    active_regions: set[str] = {p["regions"] for p in players}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players: int = len(players)
    print(f"Total players: {total_players}")
    total_uniq_achiev: int = len(unique_achiev)
    print(f"Total unique achievements: {total_uniq_achiev}")
    average_score: float = sum(score)/len(score)
    print(f"Average score: {average_score}")

    top_performer: dict[str, any] = None
    for player in players:
        if top_performer is None or player["scores"] > top_performer["scores"]:
            top_performer = player

    top_performer_str: str = (
        f"{top_performer['name']} ({top_performer['scores']} points, "
        f"{len(top_performer['achievements'])} achievements)"
    )
    print(f"Top performer: {top_performer_str}")


if __name__ == "__main__":
    """
    Entry point for analytics dashboard demonstration.
    """
    transform_data()
