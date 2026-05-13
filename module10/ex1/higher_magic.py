from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both arguments must be callable")

    def combined_spell(target: str, power: int) -> tuple[str, str]:

        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplified_spell(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence_spell(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            result = spell(target, power)
            results.append(result)
        return results
    return sequence_spell


def main() -> None:

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    multiplier = 3
    original_power = 10
    mega = power_amplifier(fireball, multiplier)
    print(f"Original: {original_power}, Amplified:"
          + f"{original_power * multiplier}")
    print(mega("Dragon", original_power))

    print("\nTesting conditional caster...")

    def is_strong(target: str, power: int) -> bool:
        return power > 0
    safe_cast = conditional_caster(is_strong, fireball)
    print(safe_cast("Dragon", 10))
    print(safe_cast("Dragon", 0))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    results = sequence("Dragon", 10)
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
