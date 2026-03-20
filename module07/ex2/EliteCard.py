from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """Elite card implementing combat and magic interfaces."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int) -> None:
        """Initialize elite card stats."""
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """Play the elite card."""

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield"
        }

    def attack(self, target) -> dict:
        """Attack a target with melee damage."""

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""

        damage_taken = max(0, incoming_damage - 3)

        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": incoming_damage - damage_taken,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        """Return current combat stats."""

        return {
            "attack": self.attack_power,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell using mana."""

        mana_used = 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        """Increase available mana by amount."""

        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        """Return current magic stats."""

        return {
            "mana": self.mana
        }
