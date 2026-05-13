def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    mapped = list(map(lambda spell: "* " + spell + " *", spells))
    return mapped


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    avg_power = round(
        sum(map(lambda x: x["power"], mages)) / len(mages), 2
    )
    dict_result = {'max_power': max_power["power"],
                   'min_power': min_power["power"],
                   'avg_power': avg_power
                   }
    return dict_result


def main() -> None:

    artifacts = [
        {'name': 'Water Chalice', 'power': 91, 'type': 'relic'},
        {'name': 'Earth Shield', 'power': 120, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 65, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 120, 'type': 'accessory'}
    ]
    mages = [{'name': 'Storm', 'power': 77, 'element': 'shadow'},
             {'name': 'Storm', 'power': 76, 'element': 'fire'},
             {'name': 'River', 'power': 78, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 66, 'element': 'earth'},
             {'name': 'Storm', 'power': 83, 'element': 'fire'}]

    spells = ['tornado', 'shield', 'earthquake', 'heal']

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']}"
          + f" ({sorted_artifacts[0]['power']} power)"
          + f" comes before {sorted_artifacts[1]['name']}"
          + f" ({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTetng power filter...")
    filtered = power_filter(mages, 42)
    print(f"{len(filtered)} mages with power >= 42")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']}, Min: {stats['min_power']},"
        f" Avg: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
