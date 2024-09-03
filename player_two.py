from player import Player


class PlayerTwo(Player):
    @property
    def player_symbol(self) -> str:
        return "O"
