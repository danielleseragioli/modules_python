from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Invalid attack value")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Invalid health value")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target: dict) -> dict:
        if 'health' not in target:
            raise ValueError("Target must have a 'health' attribute.")

        target['health'] -= self.attack

        return {
            'attacker': self.name,
            'target': target.get('name', 'Unknown'),
            'damage_dealt': self.attack,
            'combat_resolver': target['health'] <= 0
        }
