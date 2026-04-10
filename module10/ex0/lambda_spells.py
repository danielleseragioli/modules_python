"""
    artifacts: list[dict] = [
        {name: str, power: 6, type: str}
    ]
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)
    return sorted_artifacts