#!/usr/bin/env python3
import sys

class NegativeNumber(ValueError):
    def __init__(self, msg: str = "value cannot be negative") -> None:
        super().__init__(msg)


def sc_analytics() -> None:
    for arg in sys.argv[1:]:
        temp = int(arg)
        if temp < 0:
            raise NegativeNumber(f"Invalid parameter: '{arg}'")
        try:
            int(arg)
        except


if __name__ == "__main__":
    sc_analytics()
