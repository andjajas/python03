#!/usr/bin/env python3
import sys

class NegativeNumber(ValueError):
    def __init__(self, msg: str = "value cannot be negative") -> None:
        super().__init__(msg)


def sc_analytics() -> None:
    for arg in sys.argv[1:]:
        temp = int(arg)
        try:
            arg
            if temp < 0:
                raise NegativeNumber()
        except NegativeNumber as e:
            print(e)


if __name__ == "__main__":
    sc_analytics()
