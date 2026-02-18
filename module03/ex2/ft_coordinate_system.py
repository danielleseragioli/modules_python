import math


def calculate_distance(point1, point2) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return distance


def parse_coordinates(coord_string) -> tuple | None:
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
    print("=== Game Coordinate System ===")

    position1 = (10, 20, 5)
    print(f"\nPosition created: {position1}")

    origin = (0, 0, 0)
    dist1 = calculate_distance(origin, position1)
    print(f"Distance between {origin} and {position1}: {dist1:.2f}")

    position2 = parse_coordinates("3,4,0")
    print(f"\nParsing coordinates: {position2}")

    if position2:
        print(f"Parsed position: {position2}")
        dist2 = calculate_distance(origin, position2)
        print(f"Distance between {origin} and {position2}: {dist2:.2f}")

    invalid_position = parse_coordinates("abc,def,ghi")
    print(f"\nParsing invalid coordinates: {invalid_position}")

    if position2:
        print(f"\nUnpacking demonstration: {position2}")
        x, y, z = position2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
