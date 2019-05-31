import numpy as np
from moves import *
#do not enter column numbers as zero indexed!

#extract col from face
def column(face, colnum):
    col = []
    for i in range(3):
        col.append(face[i][colnum])
    return col

#takes one col of face and stores in buffer
def copycoltotemp(face, col):
    temp = []
    for i in range(3):
        temp.append(face[i][col - 1])
    return temp

#takes from buffer and assigns to face
def copycolfromtemp(temp, dest, col):
    for i in range(3):
        dest[i][col - 1] = temp[i]
    return dest

def rev_copycolfromtemp(temp, dest, col):
    for i in range(3):
        dest[i][col - 1] = temp[2 - i]
    return dest

#moves col from one face to another
def col_facetoface(face1, face2, col):
    for i in range(3):
        face2[i][col - 1] = face1[i][col - 1]
    return face2

# moves col from one face to another in reverse
def col_rev_facetoface(face1, face2, col):
    for i in range(3):
        face2[i][col - 1] = face1[2 - i][col - 1]
    return face2

def copyrowtotemp(face, rownum):
    temp = []
    for i in range(3):
        temp.append(face[rownum - 1][i])
    return temp

def row_facetoface(face1, face2, row):
    for i in range(3):
        face2[row - 1][i] = face1[row - 1][i]
    return face2

def row_rev_facetoface(face1, face2, row):
    for i in range(3):
        face2[row - 1][i] = face1[row - 1][2 - i]
    return face2

def copyrowfromtemp(temp, face, row):
    for i in range(3):
        face[row - 1][i] = temp[i]
    return face

def rev_copyrowfromtemp(temp, face, row):
    for i in range(3):
        face[row - 1][i] = temp[2 - i]
    return face

def coltorow(face1, colnum, face2, rownum):
    buff = copycoltotemp(face1, colnum)
    face2 = copyrowfromtemp(buff, face2, rownum)

    return face2

def rowtocol(face1, rownum, face2, colnum):
    buff = copyrowtotemp(face1, rownum)
    face2 = copycolfromtemp(buff, face2, colnum)

    return face2

def rev_coltorow(face1, colnum, face2, rownum):
    buff = copycoltotemp(face1, colnum)
    face2 = rev_copyrowfromtemp(buff, face2, rownum)

    return face2

def rev_rowtocol(face1, rownum, face2, colnum):
    buff = copyrowtotemp(face1, rownum)
    face2 = rev_copycolfromtemp(buff, face2, colnum)

    return face2


def printcube(cube):
    for face in cube:
        print(np.matrix(cube[face]))
        print('\n')
    print("-------------------")

def stringtoscram(string):
    scramble = []
    moves = string.split()
    for move in moves:
        scramble.append(move)
    return scramble

def printmoves(moves):
    for move in moves:
        print (move, end=' ')
    print('\n\n')

def promptuserscram():
    string = input()
    scramble = stringtoscram(string)
    print(scramble)

