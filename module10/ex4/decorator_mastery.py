import time
from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        init_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - init_time
        print(f"Spell completed in {duration:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for try_number in range(1, max_attempts+1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f"Spell failed, retrying... (attempt {try_number}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True
    
    def cast_spell(self, spell_name: str, power: int) -> str:
        if power < 10:
            return "Insufficient power for this spell"
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print()

    print("Testing retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise Exception("Spell unstable!")

    unstable_spell()
    print("Waaaaaaagh spelled !")

    print()

    print("Testing MageGuild...")

    guild = MageGuild()

    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X2"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))

if __name__ == "__main__":
    main()
        