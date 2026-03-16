from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    """Orchestrates factory creation and strategy execution."""

    def __init__(self) -> None:
        """Initialize engine state counters and dependencies."""
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns = 0
        self.total_damage = 0
        self.last_hand: list[Card] = []

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        """Attach the selected factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict[str, object]:
        """Simulate one turn and return action results."""
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine is not configured.")

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

    def get_engine_status(self) -> dict[str, object]:
        """Return the current engine simulation summary."""
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": 3
        }
