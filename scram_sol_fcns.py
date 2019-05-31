import random
from moves import *


def generate_scramble(length):
    # have list for R moves, L moves, etc. then ensure each move comes from a diff set each time.
    moves = [
        ['R', 'R\'', 'R2'],
        ['L', 'L\'', 'L2'],
        ['U', 'U\'', 'U2'],
        ['D', 'D\'', 'D2'],
        ['F', 'F\'', 'F2'],
        ['B', 'B\'', 'B2'],
    ]
    scramble = []
    prev_num = -1
    for x in range(length):
        num = random.randint(0, 5)
        while num == prev_num:
            num = random.randint(0, 5)
        prev_num = num
        index = random.randint(0, 2)
        scramble.append(moves[num][index])

    return scramble

# produces the scrambled cube layout


def exec_scramble(scramble):

    cube = {
        'front': [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
        'right': [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
        'back': [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
        'left': [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
        'top': [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
        'bottom': [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
    }

    for move in scramble:
        if move[0] == 'R':
            if move == 'R':
                cube = r(cube)
            elif move[1] == '2':
                cube = r(cube)
                cube = r(cube)
            else:
                cube = rprime(cube)

        if move[0] == "L":
            if move == 'L':
                cube = l(cube)
            elif move[1] == '2':
                cube = l(cube)
                cube = l(cube)
            else:
                cube = lprime(cube)

        if move[0] == "F":
            if move == 'F':
                cube = f(cube)
            elif move[1] == '2':
                cube = f(cube)
                cube = f(cube)
            else:
                cube = fprime(cube)

        if move[0] == "U":
            if move == 'U':
                cube = u(cube)
            elif move[1] == '2':
                cube = u(cube)
                cube = u(cube)
            else:
                cube = uprime(cube)

        if move[0] == "B":
            if move == 'B':
                cube = b(cube)
            elif move[1] == '2':
                cube = b(cube)
                cube = b(cube)
            else:
                cube = bprime(cube)

        if move[0] == "D":
            if move == 'D':
                cube = d(cube)
            elif move[1] == '2':
                cube = d(cube)
                cube = d(cube)
            else:
                cube = dprime(cube)

    return cube


# generates solution to scramble (not included in webpage)
def generate_sol(scramble):
    flipped = list.reverse(scramble)
    solution = []
    for move in scramble:
        if len(move) == 2 and move[1] != '2':
            solution.append(move[0])
        elif len(move) == 1:
            solution.append(move[0] + '\'')
        else:
            solution.append(move)
    return solution


# written for purpose of checking if scramble is correct (not included in webpage)
def solve(scramble, scrambled_cube):
    print("NOW SOLVING")
    solution = generate_sol(scramble)
    solved = exec_scramble(solution, scrambled_cube)

    return solved


if __name__ == '__main__':
    generate_scramble()