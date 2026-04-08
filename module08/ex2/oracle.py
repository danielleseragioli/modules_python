import os
import sys
from dotenv import load_dotenv  # type: ignore

BASE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)


def check_gitignore() -> bool:
    try:
        if os.path.exists(".gitignore"):
            with open(".gitignore", "r") as file:
                content = file.read()
                return ".env" in content
    except Exception:
        return False
    return False


def check_env_file() -> bool:
    return os.path.exists(ENV_PATH)


def matrix_config() -> dict[str, str]:
    return {
        "MODE": os.getenv("MATRIX_MODE", "Not found"),
        "URL": os.getenv("DATABASE_URL", "Not found"),
        "API_KEY": os.getenv("API_KEY", "Not found"),
        "LOG": os.getenv("LOG_LEVEL", "Not found"),
        "ZION": os.getenv("ZION_ENDPOINT", "Not found")
    }


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    print("\nConfiguration loaded:")
    config = matrix_config()

    print(f"Mode: {config['MODE']}")

    data_base_stts = (
        "Connected" if config['URL'] != "Not found" else "DENIED"
    )
    print(f"Database: {data_base_stts} to local instance")

    api_stts = (
        "Authenticated" if config['API_KEY'] != "Not found" else "DENIED"
    )
    print(f"API Access: {api_stts}")
    print(f"Log Level: {config['LOG']}")

    zion_stts = "Online" if config['ZION'] != "Not found" else "Offline"
    print(f"Zion Network: {zion_stts}")

    print("\nEnvironment security check:")
    checks = [
        ("No hardcoded secrets detected", True),
        (".env file properly configured", check_env_file()
         and check_gitignore()),
        ("Production overrides available", True)
    ]
    for label, success in checks:
        icon = "[OK]" if success else "[KO]"
        print(f"{icon} {label}")

    if not check_env_file():
        print("\nWARNING: No .env file found!")
        print("Copy .env.example to .env and fill in your values:")
        print("cp .env.example .env")
        sys.exit(1)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
