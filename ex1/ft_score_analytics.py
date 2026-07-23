#!/usr/bin/env python3
import sys


class NegativeNumber(ValueError):
    pass


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            temp = int(arg)
            if temp < 0:
                raise NegativeNumber(
                    f"Invalid parameter: '{int(arg)}', "
                    f"Value cannot be negative"
                 )
            scores += [temp]
        except NegativeNumber as e:
            print(e)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    players: int = len(scores)
    if players > 0:
        print(f"Scores processed: {scores}")
        print(f"Total players: {players}")
        tot_score: int = 0
        for score in scores[0:]:
            tot_score += score
        print(f"Total score: {tot_score}")
        avg_score: float = tot_score / players
        print(f"Average score: {avg_score:0.1f}")
        high_score = max(scores)
        print(f"High score: {high_score}")
        low_score = min(scores)
        print(f"Low score: {low_score}")
        sc_range = high_score - low_score
        print(f"Score range: {sc_range}")
    else:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
         )


if __name__ == "__main__":
    score_analytics()
