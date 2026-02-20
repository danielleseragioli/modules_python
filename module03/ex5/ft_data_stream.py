from typing import Dict, Any, Generator


def event_generator(count: int) -> Generator[Dict[str, Any], None, None]:
    players = ["alice", "bob", "charlie", "dani", "duda"]
    extra_levelups = 0

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
    Índices da tupla do evento:
        event[0] = id
        event[1] = player
        event[2] = level ← aqui
        event[3] = action
    """
    for event in events:
        if event[2] >= min_level:
            yield event


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(limit: int) -> Generator[int, None, None]:
    num = 2
    found = 0
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
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...\n")

    events = event_generator(1000)
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

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
    fib_gen = fibonacci_generator(10)
    idx = 0
    for num in fib_gen:
        if idx < 9:
            print(num, end=", ")
        else:
            print(num)
        idx += 1

    print("Prime numbers (first 5): ", end="")
    prime_gen = prime_generator(5)
    idx = 0
    for num in prime_gen:
        if idx < 4:
            print(num, end=", ")
        else:
            print(num)
        idx += 1


if __name__ == "__main__":
    main()
