from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)

def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        print(elf.play_elf_song())