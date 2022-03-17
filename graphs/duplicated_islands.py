#!/bin/python3
"""
Thos problen is solve how many islenad forms are repited
In a matrix 1 means land and 0 is water.
In a matrix
[[1,1,1,0,1,1],
 [ 1,1,0,0,0,1],
 [1,0,0,0,0,0],
 [0,0,1,0,0,1],
 [1,0,0,0,1,1]

Exists 3 different kinds of lands, from 5 lands

Lands looks like graphs and similitude of lands can be
kind of complicated
but what about use a matrix multiplication, for example a land
matrix agains a vector ?
"""

import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

matrix_island = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1]
]
matrix_unity = [1, 1, 1, 1, 1]


class Position():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.tuple = (i, j)

    def __eq__(self, other):
        if(isinstance(other, Position)):
            if other.i == self.i and other.j == self.j:
                return True
        return False


def is_valid_position(matrix: list, position: Position, current_path:set):
    i_max = len(matrix) - 1
    j_max = len(matrix[0]) - 1
    if (
        (   
            not position.i > i_max
            and
            not position.j > j_max
        )
        and
        position.i >= 0
        and 
        position.j >= 0
    ):
        return True
    return False


def get_connections(matrix: list, position: Position, currentpath: set):
    if is_valid_position(matrix, position, currentpath):
        if matrix[position.i][position.j] == 1:
            currentpath.add(position.tuple)
            right_position = Position(position.i, position.j + 1)
            get_connections(matrix, right_position, currentpath)
            down_position = Position(position.i+1, position.j)
            get_connections(matrix, down_position, currentpath)
    return currentpath


def get_islands(matrix):
    paths = defaultdict(set)
    discovered_land = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i, j) not in discovered_land:
                current_path = set()
                _ = get_connections(matrix, Position(i, j), current_path)
                if _:
                    paths[(i, j)] = _ 
                    discovered_land = set.union(discovered_land, _)
    return join_paths(paths)


def join_paths(paths):
    path_keys = list(paths.keys())
    final_paths = list()
    joined_paths = set()
    # pp.pprint(paths)
    # print(path_keys)
    while path_keys:
        current_key = path_keys.pop()
        # print('Current key: {}'.format(current_key))
        current_path = paths[current_key]
        current_path_len = len(current_path)
        for next_path_key in path_keys:
            if next_path_key not in joined_paths:
                next_path = paths[next_path_key]
                next_path_len = len(next_path)
                _ = set.union(current_path, next_path)
                # print(_)
                if len(_) < (current_path_len + next_path_len):
                    joined_paths.add(next_path_key)
                    current_path =_
        final_paths.append(current_path)
    return final_paths                



pp.pprint(matrix_island)                    
_ = get_islands(matrix_island)
pp.pprint(_)

