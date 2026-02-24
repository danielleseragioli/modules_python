def create_file(filename: str, content: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    file = None
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
        print(f"Un unexpected error ocurred: {e}")
    finally:
        if file:
            file.close()


def main() -> None:
    filename = "new_discovery.txt"
    content = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    create_file(filename, content)


if __name__ == "__main__":
    main()
