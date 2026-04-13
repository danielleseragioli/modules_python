def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return filtered
