from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Base interface for turn decision strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute one turn using the selected strategy."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy display name."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Order targets according to strategy preferences."""
        pass
