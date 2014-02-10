import numpy

class Board:

  def __init__(self, rows=8, columns=8, board_layout=None):
    ''' Creating a new Board instance with no arguments
        creates an 8x8 array of zeroes.
        Alternatively, you can create a specific board layout by inputting
        a Numpy array.

        A dead cell is denoted by a 0;
        a live cell is denoted by a 1.
    '''
    if board_layout == None:
      self.board = numpy.zeros(shape=(rows, columns), dtype=numpy.int)
    else:
      print board_layout
      self.board = board_layout
    self.board_transposed = self.board.transpose()
    self.board_flipped = numpy.fliplr(self.board)

  def printboard(self):
    ''' print board layout '''
    print self.board












