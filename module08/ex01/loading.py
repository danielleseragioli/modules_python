from importlib import metadata
import importlib
import sys


def check_dependencies():
    required_pkgs = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready"
    }
    optional_pkgs = {
        "requests": "Network access ready"
    }
    versions = {}
    missing_required = []
    print("\nChecking dependencies:")
    for pkg_name, description in required_pkgs.items():
        try:
            importlib.import_module(pkg_name)
            version = metadata.version(pkg_name)
            versions[pkg_name] = version
            print(f"[OK] {pkg_name} ({version}) - {description}")
        except Exception:
            print(f"[MISSING] {pkg_name}")
            missing_required.append(pkg_name)
    for pkg_name, description in optional_pkgs.items():
        try:
            importlib.import_module(pkg_name)
            version = importlib.metadata.version(pkg_name)
            versions[pkg_name] = version
            print(f"[OK] {pkg_name} ({version}) - {description}")
        except Exception:
            print(f"[MISSING] {pkg_name} (optional)")
    return missing_required, versions


def show_pip_vs_poetry():
    print("\nDependency management:")
    print("- pip uses requirements.txt with a package list.")
    print("- Poetry uses pyproject.toml and resolves "
          + "dependencies automatically.")
    print("- Poetry also creates an isolated "
          + "environment for reproducible runs.")


def analyze_matrix_data():
    import numpy as np
    import pandas as pd

    data_points = 1000
    print("\nAnalyzing Matrix data...")
    print(f"Processing {data_points} data points...")
    time_axis = np.arange(data_points)
    signal = np.sin(time_axis / 30.0) + np.random.normal(0, 0.2, data_points)
    df = pd.DataFrame({
        "time": time_axis,
        "signal": signal
    })
    metrics = {
        "mean": float(df["signal"].mean()),
        "std": float(df["signal"].std()),
        "min": float(df["signal"].min()),
        "max": float(df["signal"].max()),
    }
    print(
        "Metrics -> "
        f"mean: {metrics['mean']:.4f}, "
        f"std: {metrics['std']:.4f}, "
        f"min: {metrics['min']:.4f}, "
        f"max: {metrics['max']:.4f}"
    )

    return df, metrics


def create_visualization(df, output_file="matrix_analysis.png"):
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

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main():
    print("LOADING STATUS: Loading programs...")

    missing_required, _versions = check_dependencies()
    show_pip_vs_poetry()

    if missing_required:
        print("\nMissing required dependencies:", ", ".join(missing_required))
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("Install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)

    df, _metrics = analyze_matrix_data()
    create_visualization(df)


if __name__ == "__main__":
    main()
