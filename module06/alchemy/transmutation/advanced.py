from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the philosopher's stone from transmuted gold and a healing
    potion."""
    lead_to_gold_result: str = lead_to_gold()
    healing_potion_result: str = healing_potion()
    return (
        f"Philosopher's stone created using {lead_to_gold_result}"
        f" and {healing_potion_result}"
    )


def elixir_of_life() -> str:
    """Produce the elixir of life granting eternal youth."""
    return "Elixir of life: eternal youth achieved!"
