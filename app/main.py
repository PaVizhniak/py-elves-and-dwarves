from app.players import player
from app.players.elves import elf, elf_ranger, druid
from app.players.dwarves import dwarf, dwarf_warrior, dwarf_blacksmith


def calculate_team_total_rating(players: list[player.Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[elf.Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[dwarf.Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
