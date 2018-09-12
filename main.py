from a_star import a_star
from iddfs import iddfs
from constants import *
import globals
import psutil
import time
import gc
import os

def print_board(users_board):
    """
    Prints the board.
    :return:
    """
    board = ""
    count = 0
    for num in users_board:
        if count % EDGE_LENGTH == 0 and count != 0:
            board += '\n'
        if len(num) == 1:
            if num == '0':
                board += '   '
            else:
                board += num + '  '
        else:
            board += num + ' '
        count += 1
    print(board)

def main():
    users_board = BOARD_ONE.split(' ')

    # iddfs time
    iddfs_start_time = time.time()
    iddfs(users_board)
    iddfs_time = time.time() - iddfs_start_time
    gc.collect()

    # Manhattan Heuristic used with A*
    manhattan_astar_start_time = time.time()
    a_star(users_board, 'M')
    manhattan_astar_time = time.time() - manhattan_astar_start_time
    gc.collect()

    print(iddfs_time * 1000, 'ms')
    print(manhattan_astar_time * 1000, 'ms')

if __name__ == "__main__":
    main()