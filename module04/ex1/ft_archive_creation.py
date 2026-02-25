def create_file(filename: str, content: str) -> None:
    """Create a new archive file with the specified content."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    file: None | object = None
    try:
        file = open(filename, "w")
        print(f"\nInitializing new storage unit: {filename}")
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")
        file.write(content)
        print(content)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError:
        print(f"Error: Vault '{filename}' not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            file.close()


def main() -> None:
    """Execute the archive creation workflow."""
    filename: str = "new_discovery.txt"
    content: str = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    create_file(filename, content)


if __name__ == "__main__":
    main()
