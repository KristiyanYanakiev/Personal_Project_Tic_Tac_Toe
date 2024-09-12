from collections import deque
from typing import Dict, Deque, List

from board import Board
from chech_for_win import CheckForWin
from player import Player
from player_one import PlayerOne
from player_two import PlayerTwo


class TicTacToe:

    def __init__(self):
        self.players: Deque = deque([])
        self.turns: int = 0
        self.board_obj = Board()
        self.checker_for_win = CheckForWin(self.board_obj)

    def place_symbol(self, position) -> None:
        r, c = self.board_obj.take_row_and_col_from_position(position)
        self.board_obj.board[r][c] = self.current_player.player_symbol
        self.turns += 1
        print(self.board_obj.display_board())

    def start_game(self) -> None:
        self.print_start_game_message()

    def print_start_game_message(self) -> None:
        print(f"Let's start! Here is the numeration of the board:\n{self.board_obj.display_board()}")

    @property
    def current_player(self) -> Player:
        return self.players[0]

    def check_for_draw(self) -> bool:
        if self.turns == self.board_obj.SIZE_OF_BOARD ** 2:
            return True
        return False

    def print_win_message(self) -> None:
        print(f"Congratulations, {self.current_player}! You won!")

    @staticmethod
    def print_draw_message() -> None:
        print("Draw!")

    def play_game(self) -> None:
        while True:
            position = input(f"{self.current_player}, please select position: ")
            try:
                position = int(position)
            except ValueError:
                print(
                    f"Dear {self.current_player}, you need to enter a number between 1 and {self.board_obj.SIZE_OF_BOARD}")
                continue

            row, col = self.board_obj.take_row_and_col_from_position(position)
            if self.board_obj.check_position_valid_index(row, col):
                self.place_symbol(position)
                if self.checker_for_win.check_win() or self.check_for_draw():
                    break
                self.players.rotate()
            else:
                print(
                    f"Dear {self.current_player}, please enter valid position between 1 and {self.board_obj.SIZE_OF_BOARD ** 2}")
                continue

        if self.check_for_draw():
            self.print_draw_message()

        if self.checker_for_win.check_win():
            self.print_win_message()


if __name__ == "__main__":
    first_player_name = input("Dear Player One, please enter your name: ")
    second_player_name = input("Dear Player Two, please enter your name: ")

    player_one = PlayerOne(first_player_name)
    player_two = PlayerTwo(second_player_name)
    game = TicTacToe()
    game.players.extend([player_one, player_two])
    game.start_game()
    game.play_game()
