from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating themed cards."""

    @abstractmethod
    def create_creature(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create a creature card instance."""
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create a spell card instance."""
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: str | int | None = None
    ) -> Card:
        """Create an artifact card instance."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        """Build a themed deck with the requested size."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, list[str]]:
        """List supported card archetypes for this factory."""
        pass
