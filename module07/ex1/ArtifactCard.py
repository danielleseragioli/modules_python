from ex0.Card import Card


class ArtifactCard(Card):
    """Artifact card with reusable durability-based effect."""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """Initialize artifact properties."""
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Play the artifact and activate its passive effect."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Permanent: " + self.effect
        }

    def activate_ability(self) -> dict:
        """Use one durability charge of the artifact."""
        if self.durability > 0:
            self.durability -= 1
            return {
                "ability": "activated",
                "remaining_durability": self.durability,
                "effect_status": self.effect
            }
        return {"ability": "failed", "reason": "broken"}
