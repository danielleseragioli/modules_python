from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Run the tournament platform demo flow."""
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()
    fire_dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=50,
        health=100
    )
    ice_wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=40,
        health=80
    )
    ice_wizard.base_rating = 1150

    print("\nRegistering Tournament Cards...")
    platform.register_card(fire_dragon)
    platform.register_card(ice_wizard)

    for card in [fire_dragon, ice_wizard]:
        print(f"\n{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.base_rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", match_result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, start=1):
        leaderboard_line = (
            f"{i}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['record']})"
        )
        print(leaderboard_line)

    report = platform.generate_tournament_report()
    print("Platform Report:")
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
