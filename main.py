from collections import deque
from pprint import pprint
class ValidSymbolsError():
    pass
def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def print_game_state():
    print("This is the numeration of the board: ")
    print_board()

    for row in range(SIZE):
        for col in range(SIZE):
            board[row][col] = " "

def get_players_data():
    players = deque()
    player_one_name = input("Please, enter your name: ")
    player_two_name = input("Please, enter your name: ")
    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with X or O? ").upper()
        if player_one_symbol not in ("X", "O"):
            print(f"{player_one_name}, please select a valid symbol")
            continue
        else:
            break
    player_two_symbol = "O" if player_one_symbol == "X" else "X"
    print_game_state()

    players.extend([[player_one_name, player_one_symbol], [player_two_name, player_two_symbol]])


    return players


def check_for_win():
    player_name, player_symbol = players[0][0], players[0][1]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(SIZE)]) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit

def place_symbol_on_pos(r, c):
    board[r][c] = players[0][1]
    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def print_select_a_valid_position_message():
    print(f"{players[0][0]}, please select a valid position!")


def start():
    global turns
    while True:
        try:
            current_player_pos = int(input(f"{players[0][0]}, choose a free position between 1 - {SIZE * SIZE}: "))
            r = (current_player_pos - 1) // SIZE
            c = (current_player_pos - 1) % SIZE
        except ValueError:
            print_select_a_valid_position_message()
            continue

        if current_player_pos in range(1, SIZE * SIZE + 1) and board[r][c] == " ":
            turns += 1
            place_symbol_on_pos(r, c)

        else:
            print_select_a_valid_position_message()


SIZE = 3
turns = 0

board = []

for r in range(1, SIZE * SIZE + 1, SIZE):
    row = []
    for c in range(SIZE):
        row.append(str(r + c))
    board.append(row)

players = get_players_data()
start()




