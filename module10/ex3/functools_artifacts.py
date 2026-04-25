from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if not spells:
        return 0

    if operation not in operations:
        raise ValueError("not valid operation")
    
    func = operations[operation]
    return reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    
    fire_version = partial(base_enchantment, 50, "fire")
    ice_version = partial(base_enchantment, 50, "ice")
    lightning_version = partial(base_enchantment, 50, "lightning")
    
    return {
        "fire": fire_version,
        "ice": ice_version,
        "lightning": lightning_version
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    
    @singledispatch
    def cast_spell(spell):
        return "Unknown spell type"
    
    @cast_spell.register(int)
    def _(spell):
        return f"{spell} damage"

    @cast_spell.register(str)
    def _(spell):
        return spell
    
    @cast_spell.register(list)
    def _(spell):
        return f"{len(spell)} spells"
    
    return cast_spell


 
def main() -> None:

    print("\nTesting spell reducer...")
    print("Sum:",     spell_reducer([10, 20, 30, 40], "add"))
    print("Product:", spell_reducer([10, 20, 30, 40], "multiply"))
    print("Max:",     spell_reducer([10, 40, 20, 30], "max"))
    print("Min:",     spell_reducer([10, 40, 20, 30], "min"))
    print("Empty:",   spell_reducer([], "add"))

    try:
        spell_reducer([1, 2], "unknown")
    except ValueError as e:
        print(f"ValueError caught: {e}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Casting {element} spell with power {power} on {target}!"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"](target="goblin"))
    print(enchants["ice"](target="dragon"))
    print(enchants["lightning"](target="troll"))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}):", memoized_fibonacci(n))
    print("Cache info:", memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Damage spell:",  dispatcher(42))
    print("Enchantment:",   dispatcher("fireball"))
    print("Multi-cast:",    dispatcher([1, 2, 3]))
    print("Unknown spell type:", dispatcher(3.14))


if __name__ == "__main__":
    main()
