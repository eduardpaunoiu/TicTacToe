from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print('    |   |')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |   |')
    print('--------------')
    print('    |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |   |')
    print('--------------')
    print('    |   |')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |   |')


def player_input():
    marker = ''

    while not marker == 'X' and marker == 'O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':

        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, pos):
    board[pos] = marker


def win_check(board, mark):
    # How to win?
    # ALL ROWS? check if they all share the same marker
    # ALL COLUMNS? check if marker matches
    # DIAGONALS
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, pos):
    return board[pos] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False  # my board is not full => false

    return True


def player_choice(board):
    pos = 0

    while pos not in range(1, 10) or not space_check(board, pos):
        pos = int(input('Choose a position: (1-9)'))

    return pos


def replay():
    choice = input("Play again? Yes/No")

    return choice == 'Yes'


print('Welcome to Tic Tac Toe')

while True:

    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHO S FIRST, CHOOSE MARKERS X, 0)
    the_board = [' '] * 10  # list of 10 empty strings
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will choose first')

    play_game = input('Ready to play? Yes/No \n')

    if play_game == 'Yes':
        game_on = True
    else:
        game_on = False

    # GAME PLAY

    while game_on:

        if turn == 'Player 1':

            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                # Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    break
                else:
                    # No tie, no win? Next player's turn
                    turn = 'Player 2'

        else:
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                # Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    break
                else:
                    # No tie, no win? Next player's turn
                    turn = 'Player 1'

    if not replay():
        break
