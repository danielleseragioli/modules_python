from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns = 0
        self.total_damage = 0
        self.last_hand = []

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy):
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.last_hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("fireball")
        ]

        battlefield = []
        result = self.strategy.execute_turn(self.last_hand, battlefield)
        self.turns += 1
        self.total_damage += result["damage_dealt"]
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": 3
        }
