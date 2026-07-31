#!/usr/bin/env python3
import typing
import random


players_list: list[str] = [
    'alice', 'bob', 'charlie', 'dylan']


actions_list: list[str] = [
    'climb', 'eat', 'grab', 'move', 'release', 'run', 'sleep',
    'swim', 'use']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players_list)
        action = random.choice(actions_list)
        yield (name, action)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        idx = random.randrange(len(event_list))
        yield (event_list[idx])
        event_list[idx:idx+1] = []


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")
    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event: tuple[str, str] = next(gen)
        event_list += [event]
    print(f"Built list of {len(event_list)} events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
    print(f"Remains in list: {event_list}")
