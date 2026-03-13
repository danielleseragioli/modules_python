from ex0.Card import Card
import random


class Deck():
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> None:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> None:
        if not self.cards:
            raise IndexError('Cannot draw from an empty deck')
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            if type(card).__name__ == "CreatureCard":
                creatures += 1
            elif type(card).__name__ == "SpellCard":
                spells += 1
            elif type(card).__name__ == "ArtifactCard":
                artifacts += 1
        if total_cards > 0:
            rounded_avg = (total_cost + total_cards - 1) // total_cards
            avg_cost = float(f"{rounded_avg:.1f}")
        else:
            avg_cost = 0
        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
