from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)
