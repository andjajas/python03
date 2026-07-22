#!/usr/bin/env python3
import sys

def score_analytics():
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if arg <= 0:
        try:
            scores += [int(arg)]
            if 

        except ValueError:
            print(f"Invalid parameter: ' '{arg}', Value has to be more than 0")
    print(f"Scores processed: {scores}")
    players: int = len(scores)
    if players > 0:
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
            f"No scores provided. Usage: python3 "
            f"ft_score_analytics.py <score1> <score2> ..."
        )


if __name__ == "__main__":
    score_analytics()
