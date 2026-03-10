import alchemy.transmutation
import alchemy.transmutation.basic as basic
import alchemy.transmutation.advanced as advanced


def main() -> None:
    """Compare absolute and relative imports in the transmutation package."""
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    philosophers_str = advanced.philosophers_stone()
    print(f"philosophers_stone(): {philosophers_str}")
    elixir_str = advanced.elixir_of_life()
    print(f"elixir_of_life(): {elixir_str}")

    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():",
          alchemy.transmutation.philosophers_stone())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
