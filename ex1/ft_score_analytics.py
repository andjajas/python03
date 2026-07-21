#!/usr/bin/env python3
import sys
scores: list[int] = []
for arg in sys.argv[1:]:
    try:
        scores += [int(arg)]
    except Exception as e:
        print("Caught arg error", e)
players: int = len(scores)
print(f"Total players: {players}")
tot_score: int = 0
for score in scores[0:]:
    tot_score += score
print(f"Total score: {tot_score}")
if players > 0:
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

