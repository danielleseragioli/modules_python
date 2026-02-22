import math


def calculate_distance(point1: tuple[int, int, int],
                       point2: tuple[int, int, int]) -> float:
    """
    Calculates the Euclidean distance between two 3D points.
    Args:
        point1: Tuple of (x, y, z) coordinates.
        point2: Tuple of (x, y, z) coordinates.
    Returns:
        Distance as a float.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return distance


def parse_coordinates(coord_string: str) -> tuple[int, int, int] | None:
    """
    Parses a string of comma-separated coordinates into a tuple.
    Args:
        coord_string: String in the format 'x,y,z'.
    Returns:
        Tuple (x, y, z) if valid, else None.
    """
    try:
        parts = coord_string.split(',')

        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        return (x, y, z)

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None

    except IndexError:
        print("Error: Expected 3 coordinates (x,y,z)")
        return None


def main() -> None:
    """
    Main function to demonstrate coordinate parsing and distance calculation.
    Prints results and error handling for invalid input.
    """
    print("=== Game Coordinate System ===")

    position1: tuple[int, int, int] = (10, 20, 5)
    print(f"\nPosition created: {position1}")

    origin: tuple[int, int, int] = (0, 0, 0)
    dist1: float = calculate_distance(origin, position1)
    print(f"Distance between {origin} and {position1}: {dist1:.2f}")

    position2: tuple[int, int, int] | None = parse_coordinates("3,4,0")
    print(f"\nParsing coordinates: {position2}")

    if position2:
        print(f"Parsed position: {position2}")
        dist2: float = calculate_distance(origin, position2)
        print(f"Distance between {origin} and {position2}: {dist2:.2f}")

    invalid_position: tuple[int, int, int] | None = parse_coordinates(
        "abc,def,ghi"
    )
    print(f"\nParsing invalid coordinates: {invalid_position}")

    if position2:
        print(f"\nUnpacking demonstration: {position2}")
        x: int = position2[0]
        y: int = position2[1]
        z: int = position2[2]
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
