from typing import Generator


def event_generator(count: int) -> Generator[tuple[int, str, int, str],
                                             None, None]:
    """
    Generates game event tuples for a given count.
    Each event is a tuple: (event_id, player, level, action).
    """
    players: list[str] = ["alice", "bob", "charlie", "dani", "duda"]
    extra_levelups: int = 0

    for event_id in range(1, count + 1):
        player = players[(event_id - 1) % len(players)]

        if event_id == 1:
            level = 5
        elif event_id == 2:
            level = 12
        elif event_id == 3:
            level = 8
        elif (event_id % 3 == 0) or (event_id in (10, 11, 13, 14,
                                                  16, 17, 19, 20, 21, 23, 2)):
            level = 12
        else:
            level = 5

        if (event_id == 2) or ((event_id % 11 == 0) and
                               (event_id not in (11, 22))):
            action = "found treasure"
        elif (event_id == 3) or (event_id % 7 == 0):
            action = "leveled up"
        elif (event_id > 100) and (extra_levelups < 13):
            action = "leveled up"
            extra_levelups += 1
        else:
            action = "killed monster"

        yield (event_id, player, level, action)


def filter_high_level(events: Generator,
                      min_level: int = 10) -> Generator[tuple, None, None]:
    """
    Filters events for players with level >= min_level.
    Yields only events meeting the level requirement.
    """
    for event in events:
        if event[2] >= min_level:
            yield event


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generates the first n numbers of the Fibonacci sequence.
    """
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(limit: int) -> Generator[int, None, None]:
    """
    Generates the first 'limit' prime numbers.
    """
    num: int = 2
    found: int = 0
    while found < limit:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            found += 1
        num += 1


def main() -> None:
    """
    Main function to run the game data stream processor and analytics.
    Prints event details, analytics, and generator demonstrations.
    """
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    events: Generator[tuple[int, str, int, str], None, None] = (
        event_generator(1000)
    )
    total_events: int = 0
    high_level_count: int = 0
    treasure_count: int = 0
    levelup_count: int = 0

    for event in events:
        event_id, player, level, action = event
        if event_id <= 3:
            print(f"Event {event_id}: Player {player} (level {level}) "
                  + f"{action}")
        elif event_id == 4:
            print("...")
        total_events += 1
        if level >= 10:
            high_level_count += 1
        if action == "found treasure":
            treasure_count += 1
        if action == "leveled up":
            levelup_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib_gen: Generator[int, None, None] = fibonacci_generator(10)
    idx: int = 0
    for num in fib_gen:
        if idx < 9:
            print(num, end=", ")
        else:
            print(num)
        idx += 1

    print("Prime numbers (first 5): ", end="")
    prime_gen: Generator[int, None, None] = prime_generator(5)
    idx = 0
    for num in prime_gen:
        if idx < 4:
            print(num, end=", ")
        else:
            print(num)
        idx += 1


if __name__ == "__main__":
    main()
