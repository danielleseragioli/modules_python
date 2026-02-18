import sys

def inventory_master() -> None:
    args = sys.argv[1:]
    inventory = {}

    print("=== Inventory System Analysis ===")
    try:
        for arg in args:
            name, quantity = arg.split(":")
            inventory[name] = int(quantity)
    except ValueError:
        print("Error: output invalid")
    total_units = sum(inventory.values())
    print(f"Total items in inventory: {total_units}")


if __name__ == "__main__":
    inventory_master()