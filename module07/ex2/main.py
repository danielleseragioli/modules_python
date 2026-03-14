from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

def main():
    print("\n=== DataDeck Ability System ===")

    card = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack=5,
        health=10,
        mana=4
    )

    card_methods = []
    for method in dir(Card):
        if not method.startswith('_'):
            card_methods.append(method)
    
    magic_methods = []
    for method in dir(Magical):
        if not method.startswith('_'):
            magic_methods.append(method)

    expected_combat_methods = ['attack', 'defend', 'get_combat_stats']
    combat_methods = []
    for method in dir(card):
        if not method.startswith('_') and callable(getattr(card, method)):
            if method in expected_combat_methods:
                combat_methods.append(method)
    
    print("\nEliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")


    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    attack_result = card.attack("Enemy")
    print("Attack result:", attack_result)

    defense_result = card.defend(5)
    print("Defense result:", defense_result)

    print("\nMagic phase:")
    spell_result = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)

    mana_result = card.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
