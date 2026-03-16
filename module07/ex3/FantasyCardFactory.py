from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> Card:
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Epic", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)

    def create_spell(self, name_or_power=None) -> Card:
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power=None) -> Card:
        return ArtifactCard("Mana Ring", 1, "Uncommon", 5, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            deck.append(self.create_creature())
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
