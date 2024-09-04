class CheckWinMixin:

    starting_indecies_mapper = None
    board = None
    SIZE_OF_BOARD = None


    def check_for_first_horizontal_win(self) -> bool:
        r, c = self.starting_indecies_mapper["first_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_second_horizontal_win(self) -> bool:
        r, c = self.starting_indecies_mapper["second_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_third_horizontal_win(self) -> bool:
        r, c = self.starting_indecies_mapper["third_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_first_vertical_win(self) -> bool:
        r, c = self.starting_indecies_mapper["first_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_second_vertical_win(self) -> bool:
        r, c = self.starting_indecies_mapper["second_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_third_vertical_win(self) -> bool:
        r, c = self.starting_indecies_mapper["third_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_first_diagonal_win(self) -> bool:
        r, c = self.starting_indecies_mapper["first_diagonal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][r] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_second_diagonal_win(self) -> bool:
        r, c = self.starting_indecies_mapper["second_diagonal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][r] == symbol for r in range(self.SIZE_OF_BOARD - 1, -1, -1)])

    def check_win(self) -> bool:
        possible_wins = [self.check_for_first_horizontal_win(), self.check_for_second_horizontal_win(),
                         self.check_for_third_horizontal_win(), self.check_for_first_vertical_win(),
                         self.check_for_second_vertical_win(), self.check_for_third_vertical_win(),
                         self.check_for_first_diagonal_win(), self.check_for_second_diagonal_win()]

        if any(possible_wins):
            return True
        return False