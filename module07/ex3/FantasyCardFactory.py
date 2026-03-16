from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """Concrete factory for fantasy-themed cards."""

    def create_creature(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create a fantasy creature card."""
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Epic", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    def create_spell(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create a fantasy spell card."""
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create a fantasy artifact card."""
        return ArtifactCard("Mana Ring", 1, "Uncommon", 5, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        """Build a simple creature-focused deck."""
        deck: list[Card] = []
        for _ in range(size):
            deck.append(self.create_creature())
        return {"deck": deck}

    def get_supported_types(self) -> dict[str, list[str]]:
        """Return available fantasy archetypes."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
