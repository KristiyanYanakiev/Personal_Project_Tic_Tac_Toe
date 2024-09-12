from typing import List, Dict


class Board:
    SIZE_OF_BOARD = 3

    starting_indecies_mapper: Dict[str, tuple] = {
        "first_horizontal_win": (0, 0),
        "second_horizontal_win": (1, 0),
        "third_horizontal_win": (2, 0),

        "first_vertical_win": (0, 0),
        "second_vertical_win": (0, 1),
        "third_vertical_win": (0, 2),

        "first_diagonal_win": (0, 0),
        "second_diagonal_win": (2, 2)

    }

    def __init__(self):
        self.board: List[List[str]] = []
        for r in range(1, self.SIZE_OF_BOARD ** 2 + 1, self.SIZE_OF_BOARD):
            row = []
            for c in range(self.SIZE_OF_BOARD):
                row.append(str(r + c))
            self.board.append(row)

    def display_board(self) -> str:
        res = []
        for row in self.board:
            res.append(f"| {' | '.join(el for el in row)} |")

        return '\n'.join(res)

    def check_position_valid_index(self, row, col) -> bool:

        if row < self.SIZE_OF_BOARD and col < self.SIZE_OF_BOARD:
            return True
        return False

    def take_row_and_col_from_position(self, position) -> tuple:
        r = (position - 1) // self.SIZE_OF_BOARD
        c = (position - 1) % self.SIZE_OF_BOARD

        return r, c
