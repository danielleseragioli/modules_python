def recover_data(filename: str) -> None:
    """Recover and display data from an archive file."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file: None | object = None
    try:
        file = open(filename, "r")
        print(f"\nAccessing Storage Vault: {filename}")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        content = file.read()
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"Error: Vault '{filename}' not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
