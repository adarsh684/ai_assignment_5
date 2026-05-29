#tic_tac_toe
import math
import random
from copy import deepcopy

class TicTacToe:

    def __init__(self):
        self.board = [" " for _ in range(9)]

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, move, player):
        if self.board[move] == " ":
            self.board[move] = player
            return True
        return False

    def undo_move(self, move):
        self.board[move] = " "

    def winner(self):

        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for line in wins:
            a,b,c = line

            if (self.board[a] ==
                self.board[b] ==
                self.board[c] != " "):
                return self.board[a]

        return None

    def is_full(self):
        return " " not in self.board

    def game_over(self):
        return self.winner() is not None or self.is_full()

    def print_board(self):
        for i in range(0,9,3):
            print(self.board[i:i+3])
        print()