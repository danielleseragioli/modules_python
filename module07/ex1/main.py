from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")

    print("Building deck with different card types...")
    deck = Deck()
    creature = CreatureCard("Fire Dragon", 5, "rare", 6, 5)
    spell = SpellCard("Lightning Bolt", 3, "common", "damage")
    artifact = ArtifactCard(
        "Mana Crystal", 2, "uncommon", 3, "+1 mana per turn")

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:\n")

    while True:
        try:
            card = deck.draw_card()
        except IndexError:
            break

        card_type = type(card).__name__.replace("Card", "")
        print(f"Drew: {card.name} ({card_type})")

        result = card.play({})
        print(f"Play result: {result}\n")

    print("\nPolymorphism in action: Same interface,"
          "different card behaviors!")


if __name__ == "__main__":
    main()
