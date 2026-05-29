#alphabeta

def alphabeta(game, depth, alpha, beta, maximizing):

    winner = game.winner()

    if winner == 'X':
        return 1

    if winner == 'O':
        return -1

    if game.is_full():
        return 0

    if maximizing:

        value = -float("inf")

        for move in game.available_moves():

            game.make_move(move, 'X')

            value = max(
                value,
                alphabeta(game, depth+1,
                          alpha, beta, False)
            )

            game.undo_move(move)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = float("inf")

        for move in game.available_moves():

            game.make_move(move, 'O')

            value = min(
                value,
                alphabeta(game, depth+1,
                          alpha, beta, True)
            )

            game.undo_move(move)

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


def best_move_ab(game):

    best = -float("inf")
    best_move = None

    for move in game.available_moves():

        game.make_move(move, 'X')

        score = alphabeta(
            game,
            0,
            -float("inf"),
            float("inf"),
            False
        )

        game.undo_move(move)

        if score > best:
            best = score
            best_move = move

    return best_move