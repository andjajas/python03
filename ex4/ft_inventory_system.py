#!/usr/bin/env python3
import sys
inventory = {}
for i in sys.argv[1:]:
    if ":" in i:
        try:
            key, value = i.split(":", 1)
            inventory[key] = value
        except ValueError:
            print(f"Redundant item '{key}' - discarding")
    else:
        print(f"Error - invalid parameter '{i}")


# inventory.update({
#     "sword":1,
#     "potion":5,
#     "shield":2,
#     "armor":3,
#     "helmet":1,
#     # "sword":2,
#     # "hello",
#     # "key":value
# })


def ft_show_dict() -> None:
    print(f"{inventory}")


if __name__ == "__main__":
    ft_show_dict()
