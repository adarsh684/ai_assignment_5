# minimax

def minimax(game, maximizing):

    winner = game.winner()

    if winner == 'X':
        return 1

    if winner == 'O':
        return -1

    if game.is_full():
        return 0

    if maximizing:

        best = -float("inf")

        for move in game.available_moves():

            game.make_move(move, 'X')
            score = minimax(game, False)
            game.undo_move(move)

            best = max(best, score)

        return best

    else:

        best = float("inf")

        for move in game.available_moves():

            game.make_move(move, 'O')
            score = minimax(game, True)
            game.undo_move(move)

            best = min(best, score)

        return best


def best_move_minimax(game):

    best_score = -float("inf")
    move_choice = None

    for move in game.available_moves():

        game.make_move(move, 'X')

        score = minimax(game, False)

        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice