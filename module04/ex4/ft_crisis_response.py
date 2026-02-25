def crisis_response(files: list[str]) -> None:
    """Handle crisis scenarios in archive access with
    comprehensive error management."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    for filename in files:
        file: None | object = None
        if filename == "standard_archive.txt":
            print("\nROUTINE ACCESS: Attempting access to "
                  + f"'{filename}'...")
        else:
            print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
        try:
            with open(filename, "r") as file:
                content = file.read()
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed")

        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


def main() -> None:
    """Execute the crisis response protocol."""
    files: list[str] = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    crisis_response(files)


if __name__ == "__main__":
    main()
