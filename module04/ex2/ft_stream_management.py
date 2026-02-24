import sys


def stream_manager() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    try:
        input_id: str = input("Input Stream active. Enter archivist ID: ")
        status: str = input("Input Stream active. Enter status report: ")
    except (KeyboardInterrupt, EOFError):
        print("\n[System] An error occured, try again", file=sys.stderr)
    else:
        sys.stdout.write(
            f"\n[STANDARD] Archive status from {input_id}: "
            f"{status}\n"
        )
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels "
            "verified\n"
        )
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.write("\nThree-channel communication test successful.")


if __name__ == "__main__":
    stream_manager()
