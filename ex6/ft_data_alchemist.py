#!/usr/bin/env python3
import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
        'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    capitalized_players: list[str] = [
        player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_players}")
    already_cap_players: list[str] = [
        player for player in players if player == player.capitalize()]
    print(f"New list of capitalized names only: {already_cap_players}")
    score_dict: dict[str, int] = {
        player: random.randint(1, 1000) for player in capitalized_players}
    print(f"\nScore dict: {score_dict}")
    player_no: int = len(capitalized_players)
    total_score: int = sum(score_dict.values())
    score_avg: float = total_score / player_no
    print(f"Score average is {score_avg:0.2f}")
    highscores: dict[str, int] = {
        player: score_dict[player] for player in score_dict
        if score_dict[player] > score_avg}
    print(f"High scores: {highscores}")
