from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        """Initialize an empty tournament platform."""
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its identifier."""
        card_id = card.card_id
        if card_id in self.cards:
            raise ValueError(f"Card with id {card_id} already registered")
        self.cards[card_id] = card
        return card_id

    def create_match(
        self,
        card1_id: str,
        card2_id: str
    ) -> dict[str, int | str]:
        """Create a match and return the result payload."""

        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if not card1 or not card2:
            raise ValueError("One or both card IDs not found")

        if card1.attack_power > card2.attack_power:
            winner = card1
            loser = card2
        elif card2.attack_power > card1.attack_power:
            winner = card2
            loser = card1
        elif card1.health >= card2.health:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        winner.calculate_rating()
        loser.calculate_rating()

        self.matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list[dict[str, int | str]]:
        """Return cards ordered by rating."""

        cards_list = list(self.cards.values())
        cards_list.sort(key=lambda c: c.calculate_rating(), reverse=True)

        leaderboard = []
        for card in cards_list:
            leaderboard.append({
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}"
            })
        return leaderboard

    def generate_tournament_report(self) -> dict[str, int | str]:
        """Generate a summary report of platform status."""

        total_cards = len(self.cards)
        if total_cards == 0:
            avg_rating = 0
        else:
            avg_rating = (
                sum(c.calculate_rating() for c in self.cards.values())
                // total_cards
            )

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
