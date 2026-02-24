def recover_data(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file = None
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
        print(f"Un unexpected error ocurred: {e}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
