from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy focused on fast damage."""

    def execute_turn(
        self,
        hand: list[Card],
        battlefield: list[Card]
    ) -> dict[str, object]:
        """Play low-cost cards first within a mana cap."""
        mana_limit = 5
        cards_played: list[str] = []
        mana_used = 0

        sorted_hand = sorted(hand, key=lambda card: card.cost)
        for card in sorted_hand:
            if mana_used + card.cost > mana_limit:
                continue
            cards_played.append(card.name)
            mana_used += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

    def get_strategy_name(self) -> str:
        """Return strategy identifier."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[str]) -> list[str]:
        """Keep target order unchanged for now."""
        return available_targets
