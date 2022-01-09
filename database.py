from os import popen
import chess
import chess.syzygy

def evaluate(position, turn):
    tablebase = chess.syzygy.open_tablebase("data/syzygy/regular")
    board = chess.Board(position)
    board.turn = turn
    score = tablebase.get_dtz(board)
    tablebase.close()
    return score

