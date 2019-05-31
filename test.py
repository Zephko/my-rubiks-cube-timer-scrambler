from scram_sol_fcns import *
from array import *
import numpy as np
from helpers import *
from moves import *

def main():

    scramble = generate_scramble(15)
    printmoves(scramble)

    scrambled = exec_scramble(scramble)
    printcube(scrambled)


if __name__ == '__main__':
    main()