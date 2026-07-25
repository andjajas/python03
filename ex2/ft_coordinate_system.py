#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates: str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        separated_coords: list[str] = coordinates.split(",")
        if len(separated_coords) != 3:
            print("Invalid syntax")
            continue
        results: list[float] = []
        for coord in separated_coords:
            try:
                results += [float(coord)]
            except ValueError:
                print(
                    f"Error on parameter '{coord}': "
                    f"could not convert string to float: '{coord}'"
                )
                break
        else:
            x, y, z = results
            tuple_coords: tuple[float, float, float] = (x, y, z)
            return tuple_coords
        continue


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_coords: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first_coords}")
    x1, y1, z1 = first_coords
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_to_cen: float = math.sqrt((x1)**2 + (y1)**2 + (z1)**2)
    print(f"Distance to center: {round(distance_to_cen, 4)}")
    print("\nGet a second set of coordinates")
    second_coords: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = second_coords
    distance_between_sets: float = math.sqrt(
        (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2
    )
    print(
        "Distance between the 2 sets "
        f"of coordinates: {round(distance_between_sets, 4)}"
    )
