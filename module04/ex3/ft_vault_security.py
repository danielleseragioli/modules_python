def vault_security(file_classified: str, file_security: str) -> None:
    """Securely read and write classified vault data using context managers."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")

    try:
        print("Vault connection established with failsafe protocols")
        with open(file_classified, "r") as file:
            print("\nSECURE EXTRACTION:")
            content: str = file.read()
            print(content)

        new_info: str = "[CLASSIFIED] New security protocols archived"
        with open(file_security, "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write(new_info)
            print(new_info)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main() -> None:
    """Execute the vault security protocol."""
    file_classified: str = "classified_data.txt"
    file_security: str = "security_protocols.txt"
    vault_security(file_classified, file_security)


if __name__ == "__main__":
    main()
