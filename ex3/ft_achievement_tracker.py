#!/usr/bin/env python3
import random


all_achievements: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
    'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
    'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer']


def gen_player_achievements() -> set[str]:
    count = random.randint(0, len(all_achievements))
    player_achievements = set(random.sample(all_achievements, k=count))
    return player_achievements


if __name__ == "__main__":
    set_alice: set[str] = gen_player_achievements()
    set_bob: set[str] = gen_player_achievements()
    set_charlie: set[str] = gen_player_achievements()
    set_dylan: set[str] = gen_player_achievements()
    print(f"Player Alice: {set_alice}")
    print(f"Player Bob: {set_bob}")
    print(f"Player Charlie: {set_charlie}")
    print(f"Player Dylan: {set_dylan}")
    print(
        "\nAll distinct achievements: "
        f"{set.union(set_alice, set_bob, set_charlie, set_dylan)}"
    )
    print(
        "\nCommon achievements: "
        f"{set.intersection(set_alice, set_bob, set_charlie, set_dylan)}\n"
    )
    print(
        "Only Alice has: "
        f"{set.difference(set_alice, set_bob, set_charlie, set_dylan)}"
    )
    print(
        "Only Bob has: "
        f"{set.difference(set_bob, set_charlie, set_dylan, set_alice)}"
    )
    print(
        "Only Charlie has: "
        f"{set.difference(set_charlie, set_dylan, set_alice, set_bob)}"
    )
    print(
        "Only Dylan has: "
        f"{set.difference(set_dylan, set_alice, set_bob, set_charlie)}"
    )
    print()
    print(
        "Alice is missing: "
        f"{set.difference(set(all_achievements), set_alice)}"
    )
    print(
        "Bob is missing: "
        f"{set.difference(set(all_achievements), set_bob)}"
    )
    print(
        "Charlie is missing: "
        f"{set.difference(set(all_achievements), set_charlie)}"
    )
    print(
        "Dylan is missing: "
        f"{set.difference(set(all_achievements), set_dylan)}"
    )
