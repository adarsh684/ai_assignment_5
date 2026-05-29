# mcts

import math
import random
from copy import deepcopy

class MCTSNode:

    def __init__(self, game, parent=None,
                 move=None, player='X'):

        self.game = deepcopy(game)
        self.parent = parent
        self.move = move

        self.player = player

        self.children = []

        self.visits = 0
        self.wins = 0

    def fully_expanded(self):

        return len(self.children) == len(
            self.game.available_moves()
        )

    def best_child(self, c=1.41):

        return max(
            self.children,
            key=lambda child:
            child.wins/(child.visits+1e-6)
            + c * math.sqrt(
                math.log(self.visits+1)
                /(child.visits+1e-6)
            )
        )
    
def random_playout(game, player):

    current = player

    while not game.game_over():

        move = random.choice(
            game.available_moves()
        )

        game.make_move(move, current)

        current = 'O' if current == 'X' else 'X'

    return game.winner()


def mcts(root_game, iterations=1000):

    root = MCTSNode(root_game)

    for _ in range(iterations):

        node = root

        while node.children:
            node = node.best_child()

        if not node.game.game_over():

            moves = node.game.available_moves()

            for move in moves:

                g = deepcopy(node.game)

                g.make_move(move, node.player)

                next_player = (
                    'O'
                    if node.player == 'X'
                    else 'X'
                )

                child = MCTSNode(
                    g,
                    node,
                    move,
                    next_player
                )

                node.children.append(child)

            node = random.choice(node.children)

        winner = random_playout(
            deepcopy(node.game),
            node.player
        )

        while node:

            node.visits += 1

            if winner == 'X':
                node.wins += 1

            node = node.parent

    best = max(
        root.children,
        key=lambda n: n.visits
    )

    return best.move