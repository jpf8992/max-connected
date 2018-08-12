import random
import operator
import sys
import unittest

# __version__ = "0.3"

# Adopted from:
# http://code.activestate.com/recipes/578131-a-simple-matrix-class/

class MatrixError(Exception):
    """ An exception class for Matrix """
    pass

class Matrix(object):
    """ A simple Python matrix class with
    basic operations and operator overloading """
    
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0]*n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n
        # print("-- New Matrix Initialised --")
        
    def __getitem__(self, idx):
        return self.rows[idx]
    

    def __setitem__(self, idx, item):
        print("Set-item")
        self.rows[idx] = item
        
        
    def __str__(self):
        s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s=str(self.rows)
        rank = str(self.getRank())
        rep="Matrix: \"%s\", rank: \"%s\"" % (s,rank)
        return rep

    def getRank(self):
        return (self.m, self.n)

    def __eq__(self, mat):
        """ Test equality """
        return (mat.rows == self.rows)

    def getValidNeighbours(self,current_row,current_col):
        print("current_row: " + str(current_row), "Current_col: " + str(current_col))
        # print(self.getRank())


        # dict to store return val
        valid_neighbours = {"above":False, "right":False, "below":False, "left":False}

        # set upper/lower limits of matrix
        lower_row = 0
        lower_col = 0
        (m_rank,n_rank) = self.getRank()

        upper_row = (m_rank - 1) #offet -1
        upper_col = (n_rank - 1) #offet -1


        # If there is a neighbouring tile,
        # not outside the matrix limits, update dict

        # tile above
        if(current_row -1 >= lower_row):
            print("above")
            valid_neighbours["above"] = True

        # tile right
        if(current_col +1 <= upper_col):
            print("right")
            valid_neighbours["right"] = True

        # tile below
        if(current_row +1 <= upper_row):
            print("below")
            valid_neighbours["below"] = True

        # tile left
        if(current_col -1 >= lower_col):
            print("left")
            valid_neighbours["left"] = True

        return valid_neighbours
        
    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        """ Make a random matrix with elements in range (low-high) """
        
        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def makeZero(cls, m, n):
        """ Make a zero-matrix of rank (mxn) """

        rows = [[0]*n for x in range(m)]
        return cls.fromList(rows)
    

    @classmethod
    def readGrid(cls, fname):
        """ Read a matrix from a file """

        rows = []
        for line in open(fname).readlines():
            row = [int(x) for x in line.split()]
            rows.append(row)

        return cls._makeMatrix(rows)

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError, "inconsistent row length"
        mat = Matrix(m,n, init=False)
        mat.rows = rows

        return mat

    @classmethod
    def fromList(cls, listoflists):
        """ Create a matrix by directly passing a list
        of lists """

        # E.g: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)

    






if __name__ == "__main__":
    print("Not a main file! \n proper usage <python main.py>")
