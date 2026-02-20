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
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sorted_inventory = dict(
        sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    )
    for name, quantity in sorted_inventory.items():
        percetage = (quantity / total_units) * 100
        unit_str = "unit" if quantity == 1 else "units"
        print(f"{name}: {quantity} {unit_str} ({percetage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    if inventory:
        most_abundant = max(inventory, key=inventory.get)
        least_abundant = min(inventory, key=inventory.get)
        most_quantity = inventory[most_abundant]
        least_quantity = inventory[least_abundant]
        print(f"Most abundant: {most_abundant} ({most_quantity} {unit_str})")
        print(f"Least abundant: {least_abundant} ({least_quantity}"
              + f" {unit_str})")

    print("\n=== Item Categories ===")
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for item, quantity in sorted_inventory.items():
        if quantity >= 5:
            categories["Moderate"].update({item: quantity})
        else:
            categories["Scarce"].update({item: quantity})
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    print("\n=== Management Suggestions ===")
    restock = [item for item, quantity in sorted_inventory.items()
               if quantity <= 1]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    inventory_master()
