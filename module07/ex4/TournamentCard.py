from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, card_id: str, name: str, cost: int, rarity: str,
                 attack_power: int, health: int) -> None:
        """Initialize a tournament-ready card."""
        super().__init__(name, cost, rarity)

        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("attack_power must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.max_health = health
        self.wins = 0
        self.losses = 0
        self.base_rating = 1200

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the card and return its immediate effect."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered battlefield"
        }

    def attack(
        self,
        target: "TournamentCard | dict[str, Any]"
    ) -> dict[str, Any]:
        """Attack a target and report combat details."""
        damage = self.attack_power
        if isinstance(target, TournamentCard):
            result = target.defend(damage)
            target_name = target.name
            remaining_health = result["remaining_health"]
        elif isinstance(target, dict):
            target["health"] = max(0, target["health"] - damage)
            target_name = target.get("name", "Unknown")
            remaining_health = target["health"]

        else:
            raise ValueError("Invalid target format")

        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": damage,
            "target_remaining_health": remaining_health
            }

    def defend(self, incoming_damage: int) -> dict[str, int]:
        """Take damage and return remaining health data."""
        self.health -= incoming_damage

        if self.health < 0:
            self.health = 0

        return {
            "damage_taken": incoming_damage,
            "remaining_health": self.health
        }

    def get_combat_stats(self) -> dict[str, int]:
        """Return current combat statistics."""
        return {
            "attack_power": self.attack_power,
            "current_health": self.health,
            "max_health": self.max_health
        }

    def calculate_rating(self) -> int:
        """Calculate the card rating from match record."""
        rating = self.base_rating + (self.wins * 16) - (self.losses * 16)
        return rating

    def update_wins(self, wins: int) -> None:
        """Add wins to this card record."""
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a non-negative integer")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Add losses to this card record."""
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a non-negative integer")
        self.losses += losses

    def get_rank_info(self) -> dict[str, int | str]:
        """Return rating and win/loss summary."""
        return {
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict[str, int | str]:
        """Return full tournament-related card stats."""
        return {
            "card_id": self.card_id,
            "name": self.name,
            "attack_power": self.attack_power,
            "health": self.health,
            "max_health": self.max_health,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.base_rating
        }
