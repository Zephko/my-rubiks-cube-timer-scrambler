from helpers import *
import numpy as np

# letter indicates which face to turn (clockwise)
# if prime then rotate face counter-clockwise


def rprime(cube):
    temp = copycoltotemp(cube['bottom'], 3)
    cube['bottom'] = col_facetoface(cube['front'], cube['bottom'], 3)
    cube['front'] = col_facetoface(cube['top'], cube['front'], 3)
    cube['top'] = col_rev_facetoface(cube['back'], cube['top'], 3)
    cube['back'] = rev_copycolfromtemp(temp, cube['back'], 3)
    cube['right'] = np.rot90(cube['right'], k=1)

    return cube


def u(cube):
    temp = copyrowtotemp(cube['front'], 1)
    cube['front'] = row_facetoface(cube['right'], cube['front'], 1)
    cube['right'] = row_rev_facetoface(cube['back'], cube['right'], 1)
    cube['back'] = row_rev_facetoface(cube['left'], cube['back'], 1)
    cube['left'] = copyrowfromtemp(temp, cube['left'], 1)
    cube['top'] = np.rot90(cube['top'], k=3)

    return cube


def r(cube):
    temp = copycoltotemp(cube['top'], 3)
    cube['top'] = col_facetoface(cube['front'], cube['top'], 3)
    cube['front'] = col_facetoface(cube['bottom'], cube['front'], 3)
    cube['bottom'] = col_rev_facetoface(cube['back'], cube['bottom'], 3)
    cube['back'] = rev_copycolfromtemp(temp, cube['back'], 3)
    cube['right'] = np.rot90(cube['right'], k=3)

    return cube


def uprime(cube):
    temp = copyrowtotemp(cube['front'], 1)
    cube['front'] = row_facetoface(cube['left'], cube['front'], 1)
    cube['left'] = row_rev_facetoface(cube['back'], cube['left'], 1)
    cube['back'] = row_rev_facetoface(cube['right'], cube['back'], 1)
    cube['right'] = copyrowfromtemp(temp, cube['right'], 1)
    cube['top'] = np.rot90(cube['top'], k=1)

    return cube


def lprime(cube):
    temp = copycoltotemp(cube['top'], 1)
    cube['top'] = col_facetoface(cube['front'], cube['top'], 1)
    cube['front'] = col_facetoface(cube['bottom'], cube['front'], 1)
    cube['bottom'] = col_rev_facetoface(cube['back'], cube['bottom'], 1)
    cube['back'] = rev_copycolfromtemp(temp, cube['back'], 1)
    cube['left'] = np.rot90(cube['left'], k=1)

    return cube


def l(cube):
    temp = copycoltotemp(cube['bottom'], 1)
    cube['bottom'] = col_facetoface(cube['front'], cube['bottom'], 1)
    cube['front'] = col_facetoface(cube['top'], cube['front'], 1)
    cube['top'] = col_rev_facetoface(cube['back'], cube['top'], 1)
    cube['back'] = rev_copycolfromtemp(temp, cube['back'], 1)
    cube['left'] = np.rot90(cube['left'], k=3)

    return cube


def d(cube):
    temp = copyrowtotemp(cube['front'], 3)
    cube['front'] = row_facetoface(cube['left'], cube['front'], 3)
    cube['left'] = row_rev_facetoface(cube['back'], cube['left'], 3)
    cube['back'] = row_rev_facetoface(cube['right'], cube['back'], 3)
    cube['right'] = copyrowfromtemp(temp, cube['right'], 3)
    cube['bottom'] = np.rot90(cube['bottom'], k=3)

    return cube


def dprime(cube):
    temp = copyrowtotemp(cube['front'], 3)
    cube['front'] = row_facetoface(cube['right'], cube['front'], 3)
    cube['right'] = row_rev_facetoface(cube['back'], cube['right'], 3)
    cube['back'] = row_rev_facetoface(cube['left'], cube['back'], 3)
    cube['left'] = copyrowfromtemp(temp, cube['left'], 3)
    cube['bottom'] = np.rot90(cube['bottom'], k=1)

    return cube


def f(cube):
    temp = copyrowtotemp(cube['top'], 3)
    cube['top'] = rev_coltorow(cube['left'], 3, cube['top'], 3)
    cube['left'] = rowtocol(cube['bottom'], 1, cube['left'], 3)
    cube['bottom'] = rev_coltorow(cube['right'], 1, cube['bottom'], 1)
    cube['right'] = copycolfromtemp(temp, cube['right'], 1)
    cube['front'] = np.rot90(cube['front'], k=3)

    return cube


def fprime(cube):
    temp = copyrowtotemp(cube['top'], 3)
    cube['top'] = coltorow(cube['right'], 1, cube['top'], 3)
    cube['right'] = rev_rowtocol(cube['bottom'], 1, cube['right'], 1)
    cube['bottom'] = coltorow(cube['left'], 3, cube['bottom'], 1)
    cube['left'] = rev_copycolfromtemp(temp, cube['left'], 3)
    cube['front'] = np.rot90(cube['front'], k=1)

    return cube


def b(cube):
    temp = copyrowtotemp(cube['top'], 1)
    cube['top'] = coltorow(cube['right'], 3, cube['top'], 1)
    cube['right'] = rev_rowtocol(cube['bottom'], 3, cube['right'], 3)
    cube['bottom'] = coltorow(cube['left'], 1, cube['bottom'], 3)
    cube['left'] = rev_copycolfromtemp(temp, cube['left'], 1)
    cube['back'] = np.rot90(cube['back'], k=1)

    return cube


def bprime(cube):
    temp = copyrowtotemp(cube['top'], 1)
    cube['top'] = rev_coltorow(cube['left'], 1, cube['top'], 1)
    cube['left'] = rowtocol(cube['bottom'], 3, cube['left'], 1)
    cube['bottom'] = rev_coltorow(cube['right'], 3, cube['bottom'], 3)
    cube['right'] = copycolfromtemp(temp, cube['right'], 3)
    cube['back'] = np.rot90(cube['back'], k=3)

    return cube