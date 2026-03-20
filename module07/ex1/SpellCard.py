from ex0.Card import Card
from typing import Any


class SpellCard(Card):
    """Spell card that resolves a one-time effect."""

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """Initialize spell card attributes."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def resolve_effect(self, targets: list[str] | None = None) -> str:
        """Resolve and return the spell effect text."""
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 5 health to player",
            "buff": "Give +2/+2 to a creature",
            "debuff": "Reduce enemy attack by 2"
        }
        return effects.get(self.effect_type, "Generic magic effect")

    def play(self, game_state: dict[str, Any]) -> dict[str, str | int]:
        """Play the spell and report the resolved effect."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect()
        }
