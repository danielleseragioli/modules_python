import sys
import os
import site


def check_if_venv() -> bool:
    try:
        return sys.base_prefix != sys.prefix
    except Exception as e:
        print(f"error: {e}")
    return False


def get_paths() -> str:
    try:
        pkg_paths = site.getsitepackages()
        return pkg_paths[0]
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    in_venv: bool = check_if_venv()
    py_path: str = sys.executable
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path)
    pkg_path: str = get_paths()
    if in_venv:
        print("\nMATRIX STATUS: Welcome to the construct")

        print(f"\nCurrent Python: {py_path}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print("\nPackage installation path:")
        print(pkg_path)
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {py_path}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
