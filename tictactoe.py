# single player mode:
#   User chooses to play as X or O, and plays against computer that randomly
#   chooses free coordinates while user is prompted to enter coordinates.

# double player mode:
#   Player one chooses to play as X or O, second player plays opposite of
#   player one's choice. Program prompts both players for coordinates
#   altnernatively.

# Prompt for single player mode or double player mode
#  If single player mode,
#   1. Ask for user coordinate.
#   2. Wait one second, computer picks a coordinate.
#   3. While no winner exists, repeat steps 1 and 2.
#  If double player mode,
#   1. Ask for player one coordinate.
#   2. Ask for player two coordinate.
#   3. While no winner exists, repeat steps 1 and 2.

from random import randint
from time import sleep

def print_board(board):
    for row in board:
        print(*row, sep = ' ')

def find_winner(board):
    # returns 'x' or 'o' depending on whether three marks have been found in a row
    x_count, o_count = 0
    for row in board:
        for coord in row:
            if coord == 'X': x_count += 1
            elif coord == 'O': o_count += 1
        if x_count == 3: return 'x'
        elif o_count == 3: return 'o'

       if board[0][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X': return 'x'
       if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X': return 'x'
       if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X': return 'x'

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

mode = input('For single player mode, enter "s"\n\
For double player mode, enter "d"\n\
Choose a mode: ').lower()

# single player mode

if mode == 's':
    user_piece = input('Choose a piece to play as: ').upper()
    computer_piece = 'X' if user_piece == 'O' else 'O'

    winner = None

    while winner == None:
        print_board(board)
        
        # obtain user's coordinates
        
        user_coords = list(map(int, input('Enter X and Y coordinates: ').split(',')))

        while board[user_coords[1] - 1][user_coords[0] - 1] != '-':
            print('Coordinates are occupied!')

            user_coords = list(map(int, input('Enter X and Y coordinates: ').split(',')))

        # update the board

        board[user_coords[1] - 1][user_coords[0] - 1] = user_piece

        sleep(1)

        # generate computer's coordinates

        computer_coords = [randint(1, 3), randint(1, 3)]

        while board[computer_coords[1] - 1][computer_coords[0] - 1] != '-':
            computer_coords = [randint(1, 3), randint(1, 3)]

        # debug print statements

        print('User coords: ' + ', '.join(map(str, user_coords)))
        print('Computer coords: ' + ', '.join(map(str, computer_coords)))

        # update the board

        board[computer_coords[1] - 1][computer_coords[0] - 1] = computer_piece

        # check for a winner
