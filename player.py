from abc import ABC, abstractmethod


class Player(ABC):
    valid_players_letters = ["x", "o"]

    def __init__(self, name):
        self.name = name
        self.symbol = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Dear Player, the name cannot be empty. Please enter a valid name")

        self.__name = value

    @property
    @abstractmethod
    def player_symbol(self) -> str:
        pass

    def assign_symbol_to_player(self) -> None:
        self.symbol = self.player_symbol

    def __repr__(self):
        return self.name
