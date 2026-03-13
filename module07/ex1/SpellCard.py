from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def resolve_effect(self, targets: list = None) -> str:
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 5 health to player",
            "buff": "Give +2/+2 to a creature",
            "debuff": "Reduce enemy attack by 2"
        }
        return effects.get(self.effect_type, "Generic magic effect")

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect()
        }
