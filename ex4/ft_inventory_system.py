#!/usr/bin/env python3
import sys


def create_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for i in sys.argv[1:]:
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        key, value = i.split(":", 1)
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    return inventory


def item_representation() -> None:
    for key in inventory.keys():
        value = inventory[key]
        pct = value / total_items * 100
        print(f"Item {key} represents {pct:0.1f}%")


def most_abundant(inventory: dict[str, int]) -> tuple[str, int]:
    if not inventory:
        return "", 0
    keys = list(inventory.keys())
    most_key = keys[0]
    most_value = inventory[most_key]
    for key in keys:
        if inventory[key] > most_value:
            most_key = key
            most_value = inventory[key]
    return (most_key, most_value)


def least_abundant(inventory: dict[str, int]) -> tuple[str, int]:
    if not inventory:
        return "", 0
    keys = list(inventory.keys())
    least_key = keys[0]
    least_value = inventory[least_key]
    for key in keys:
        if inventory[key] < least_value:
            least_key = key
            least_value = inventory[key]
    return (least_key, least_value)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = create_inventory()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total_items: int = sum(inventory.values())
    print(
        f"Total quantity of the {len(inventory)} "
        f"items: {total_items}")
    item_representation()
    name1, quantity1 = most_abundant(inventory)
    name2, quantity2 = least_abundant(inventory)
    print(f"Item most abundant: {name1} with quantity {quantity1}")
    print(f"Item most abundant: {name2} with quantity {quantity2}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


# command line input:
# sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
