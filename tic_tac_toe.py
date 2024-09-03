from collections import deque


class TicTacToe:
    SIZE_OF_BOARD = 3

    starting_indecies_mapper = {
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
        self.players = deque([])
        self.turns = 0

        self.board = []
        for r in range(1, self.SIZE_OF_BOARD ** 2 + 1, self.SIZE_OF_BOARD):
            row = []
            for c in range(self.SIZE_OF_BOARD):
                row.append(str(r + c))
            self.board.append(row)

    def display_board(self):
        res = []
        for row in self.board:
            res.append(f"| {' | '.join(el for el in row)} |")

        return '\n'.join(res)

    def check_position_valid_index(self, row, col):

        if row < self.SIZE_OF_BOARD and col < self.SIZE_OF_BOARD:
            return True
        return False

    def take_row_and_col_from_position(self, position):
        r = (position - 1) // self.SIZE_OF_BOARD
        c = (position - 1) % self.SIZE_OF_BOARD

        return r, c

    def place_symbol(self, position) -> None:
        r, c = self.take_row_and_col_from_position(position)
        self.board[r][c] = self.current_player.player_symbol
        self.turns += 1
        print(self.display_board())

    def start_game(self):
        self.print_start_game_message()

    def print_start_game_message(self):
        print(f"Let's start! Here is the numeration of the board:\n{self.display_board()}")

    @property
    def current_player(self):
        return self.players[0]

    def check_for_draw(self):
        if self.turns == self.SIZE_OF_BOARD ** 2:
            return True
        return False

    def check_for_first_horizontal_win(self):
        r, c = self.starting_indecies_mapper["first_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_second_horizontal_win(self):
        r, c = self.starting_indecies_mapper["second_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_third_horizontal_win(self):
        r, c = self.starting_indecies_mapper["third_horizontal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for c in range(self.SIZE_OF_BOARD)])

    def check_for_first_vertical_win(self):
        r, c = self.starting_indecies_mapper["first_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_second_vertical_win(self):
        r, c = self.starting_indecies_mapper["second_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_third_vertical_win(self):
        r, c = self.starting_indecies_mapper["third_vertical_win"]
        symbol = self.board[r][c]

        return all([self.board[r][c] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_first_diagonal_win(self):
        r, c = self.starting_indecies_mapper["first_diagonal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][r] == symbol for r in range(self.SIZE_OF_BOARD)])

    def check_for_second_diagonal_win(self):
        r, c = self.starting_indecies_mapper["second_diagonal_win"]
        symbol = self.board[r][c]

        return all([self.board[r][r] == symbol for r in range(self.SIZE_OF_BOARD - 1, -1, -1)])

    def check_win(self):
        possible_wins = [self.check_for_first_horizontal_win(), self.check_for_second_horizontal_win(),
                         self.check_for_third_horizontal_win(), self.check_for_first_vertical_win(),
                         self.check_for_second_vertical_win(), self.check_for_third_vertical_win(),
                         self.check_for_first_diagonal_win(), self.check_for_second_diagonal_win()]

        if any(possible_wins):
            return True
        return False

    def print_win_message(self):
        print(f"Congratulations, {self.current_player}! You won!")

    @staticmethod
    def print_draw_message():
        print("Draw!")
