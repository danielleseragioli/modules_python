import sys


def score_analyze() -> None:
    """
    Parses command-line arguments as player scores and prints analytics.
    Handles invalid input gracefully and computes statistics.
    """
    args: list[str] = sys.argv[1:]
    scores: list[int] = []

    print("=== Player Score Analytics ===")

    if len(args) < 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              + "<score1> <score2> ...")
        return

    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Warning: {arg} is not a valid score and will be ignored.")

    if len(scores) == 0:
        print("No valid scores provided.")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    score_analyze()
