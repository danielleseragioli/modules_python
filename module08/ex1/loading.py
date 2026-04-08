from importlib import metadata
import importlib
import sys


def check_dependencies() -> tuple[list[str], dict[str, str]]:
    pkgs = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    versions = {}
    missing_required = []
    print("\nChecking dependencies:")
    for pkg_name, description in pkgs.items():
        try:
            importlib.import_module(pkg_name)
            version = metadata.version(pkg_name)
            versions[pkg_name] = version
            print(f"[OK] {pkg_name} ({version}) - {description}")
        except Exception:
            print(f"[MISSING] {pkg_name}")
            missing_required.append(pkg_name)
    return missing_required, versions


def analyze_matrix_data():
    import pandas as pd
    import numpy as np

    signal = [10, 12, 11, 13, 15, 14, 16, 17, 16, 18]
    time = list(range(len(signal)))

    signal_array = np.array(signal)

    df = pd.DataFrame({"time": time, "signal": signal_array})

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(signal)} data points...")

    return df


def create_visualization(df,
                         output_file: str = "matrix_analysis.png") -> None:
    import matplotlib.pyplot as plt

    print("Generating visualization...")

    plt.figure(figsize=(10, 4))
    plt.plot(df["time"], df["signal"], linewidth=1.2, color="green")
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")

    missing_required, _versions = check_dependencies()

    if missing_required:
        print("\nMissing required dependencies:", ", ".join(missing_required))
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("Install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)

    df = analyze_matrix_data()
    create_visualization(df)


if __name__ == "__main__":
    main()
