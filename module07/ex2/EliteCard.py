from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health
        self.mana = mana
    
    """ implementation abstractmethods from Card """
    def play(self, game_state: dict) -> dict:

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield"
        }

    """ implementation abstractmethods from Combatable """
    def attack(self, target) -> dict:

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:

        damage_taken = max(0, incoming_damage - 3)

        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": incoming_damage - damage_taken,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:

        return {
            "attack": self.attack_power,
            "health": self.health
        }

    """ implementation abstractmethods from Magical """
    def cast_spell(self, spell_name: str, targets: list) -> dict:

        mana_used = 4
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:

        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:

        return {
            "mana": self.mana
        }


