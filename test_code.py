from player_one import PlayerOne
from player_two import PlayerTwo
from tic_tac_toe import TicTacToe


first_player_name = input("Dear Player One, please enter your name: ")
second_player_name = input("Dear Player Two, please enter your name: ")

player_one = PlayerOne(first_player_name)
player_two = PlayerTwo(second_player_name)
game = TicTacToe()
game.players.extend([player_one, player_two])
game.start_game()

while True:  #TODO: Optimize methods to minimaze if statements: include messages inside the methods
    position = input(f"{game.current_player}, please select position: ")
    try:
        position = int(position)
    except ValueError:
        print(f"Dear {game.current_player}, you need to enter a number between 1 and {game.SIZE_OF_BOARD}")
        continue

    row, col = game.take_row_and_col_from_position(position)
    if game.check_position_valid_index(row, col):
        game.place_symbol(position)
        if game.check_win() or game.check_for_draw():
            break
        game.players.rotate()
    else:
        print(f"Dear {game.current_player}, please enter valid position between 1 and {game.SIZE_OF_BOARD ** 2}")
        continue

if game.check_for_draw():
    game.print_draw_message()

if game.check_win():
    game.print_win_message()
