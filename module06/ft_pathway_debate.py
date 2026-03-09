import alchemy.transmutation as transmutation
import alchemy

def main() -> None:
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {transmutation.basic.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    philosophers_str = transmutation.advanced.philosophers_stone()
    print(f"philosophers_stone(): {philosophers_str}")
    elixir_str = transmutation.advanced.elixir_of_life()
    print(f"elixir_of_life(): {elixir_str}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold():",
    alchemy.transmutation.lead_to_gold()
    )
    print(f"alchemy.transmutation.philosophers_stone():",
    alchemy.transmutation.philosophers_stone()
    )

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()