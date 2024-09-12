from board import Board


class CheckForWin:

    def __init__(self, board_to_check: Board):
        self.board_to_check = board_to_check

    def check_for_first_horizontal_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["first_horizontal_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for c in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_second_horizontal_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["second_horizontal_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for c in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_third_horizontal_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["third_horizontal_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for c in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_first_vertical_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["first_vertical_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for r in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_second_vertical_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["second_vertical_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for r in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_third_vertical_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["third_vertical_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][c] == symbol for r in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_first_diagonal_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["first_diagonal_win"]
        symbol = self.board_to_check.board[r][c]

        return all([self.board_to_check.board[r][r] == symbol for r in range(self.board_to_check.SIZE_OF_BOARD)])

    def check_for_second_diagonal_win(self) -> bool:
        r, c = self.board_to_check.starting_indecies_mapper["second_diagonal_win"]
        symbol = self.board_to_check.board[r][c]

        return all(
            [self.board_to_check.board[r][r] == symbol for r in range(self.board_to_check.SIZE_OF_BOARD - 1, -1, -1)])

    def check_win(self) -> bool:
        possible_wins = [self.check_for_first_horizontal_win(), self.check_for_second_horizontal_win(),
                         self.check_for_third_horizontal_win(), self.check_for_first_vertical_win(),
                         self.check_for_second_vertical_win(), self.check_for_third_vertical_win(),
                         self.check_for_first_diagonal_win(), self.check_for_second_diagonal_win()]

        if any(possible_wins):
            return True
        return False
