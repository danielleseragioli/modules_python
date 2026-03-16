from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")

    result = engine.simulate_turn()
    hand = engine.last_hand
    hand_str = ", ".join(f"{c.name} ({c.cost})" for c in hand)
    print(f"Hand: [{hand_str}]")
    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", result)

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: "
          + "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
