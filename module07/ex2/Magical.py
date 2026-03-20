from abc import ABC, abstractmethod


class Magical(ABC):
    """Interface for magic-capable cards."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on one or more targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana and return mana state."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return magic-related stats."""
        pass
