def vault_security(file_classified: str, file_security: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")

    try:
        print("Vault connection established with failsafe protocols")
        with open(file_classified, "r") as file:
            print("\nSECURE EXTRACTION:")
            content: str = file.read()
            print(content)

        new_info = "[CLASSIFIED] New security protocols archived"
        with open(file_security, "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write(new_info)
            print(new_info)

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception as e:
        print(f"Un unexpected error ocurred: {e}")


def main() -> None:
    file_classified = "classified_data.txt"
    file_security = "security_protocols.txt"
    vault_security(file_classified, file_security)


if __name__ == "__main__":
    main()
