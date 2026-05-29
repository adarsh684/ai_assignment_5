from tic_tac_toe import TicTacToe
from minimax import best_move_minimax
from alphabeta import best_move_ab
from heuristic_alphabeta import heuristic_ab
from mcts import mcts


def print_board(board):
    for i in range(0, 9, 3):
        row = []
        for j in range(3):
            cell = board[i + j]
            row.append(cell if cell != " " else "_")
        print(" ".join(row))
    print()


def get_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in wins:
        a, b, c = line

        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def run_algorithm(name, move, board, expected_move):

    print(name)
    print()

    print(f"Chosen Move: {move}")
    print()

    new_board = board.copy()

    if move is not None:
        new_board[move] = 'X'

    print("Board After Move")
    print()

    print_board(new_board)

    winner = get_winner(new_board)

    if winner:
        print(f"Outcome: {winner} Wins")
    else:
        print("Outcome: Game Continues")

    if move == expected_move:
        print("Status: PASS")
    else:
        print("Status: FAIL")

    print()


def run_test(test_name, board, expected_move):

    print(test_name)
    print()

    print("Initial Board")
    print()

    print_board(board)

    print(f"Expected Move: {expected_move}")
    print()

    # Minimax
    game = TicTacToe()
    game.board = board.copy()
    move = best_move_minimax(game)

    run_algorithm(
        "Minimax",
        move,
        board,
        expected_move
    )

    # Alpha-Beta
    game = TicTacToe()
    game.board = board.copy()
    move = best_move_ab(game)

    run_algorithm(
        "Alpha-Beta Search",
        move,
        board,
        expected_move
    )

    # Heuristic Alpha-Beta
    game = TicTacToe()
    game.board = board.copy()

    best_move = None
    best_score = -float("inf")

    for move in game.available_moves():

        game.make_move(move, 'X')

        score = heuristic_ab(
            game,
            depth=0,
            alpha=-float("inf"),
            beta=float("inf"),
            maximizing=False,
            limit=4
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    run_algorithm(
        "Heuristic Alpha-Beta Search",
        best_move,
        board,
        expected_move
    )

    # MCTS
    game = TicTacToe()
    game.board = board.copy()

    move = mcts(game, iterations=5000)

    run_algorithm(
        "Monte-Carlo Tree Search",
        move,
        board,
        expected_move
    )


# winning move test case
run_test(
    "TEST CASE 1: Winning Move",
    [
        'X', 'X', ' ',
        'O', 'O', ' ',
        ' ', ' ', ' '
    ],
    2
)

# blocking move test case
run_test(
    "TEST CASE 2: Blocking Move",
    [
        'O', 'O', ' ',
        'X', ' ', ' ',
        ' ', ' ', 'X'
    ],
    2
)

# empty board test case
run_test(
    "TEST CASE 3: Empty Board",
    [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '
    ],
    4
)