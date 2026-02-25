def crisis_response(files: list[str]) -> None:

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    for filename in files:
        file = None
        if filename == "standard_archive.txt":
            print("\nROUTINE ACCESS: Attempting access to "
                  + "'standard_archive.txt'...")
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
            print(f"Un unexpected error ocurred: {e}")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


def main():
    files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    crisis_response(files)


if __name__ == "__main__":
    main()
