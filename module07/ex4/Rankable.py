from abc import ABC, abstractmethod


class Rankable(ABC):
    """Interface for ranking-capable tournament entities."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Compute and return the current ranking score."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Increase the total number of wins."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Increase the total number of losses."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return rating and record information."""
        pass
