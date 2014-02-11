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
    self.rows = rows
    self.columns = columns
    self.board_transposed = self.board.transpose()
    self.board_flipped = numpy.fliplr(self.board)

  def printboard(self):
    ''' print board layout '''
    print self.board

  def count_adjacent_rows(self, x, y):
    ''' dy = -1, dx = -1, 0, 1
        dy =  0, dx = -1, 0, 1
        dy =  1, dx = -1, 0, 1 '''
    c = 0
    for dy in range(-1, 2):
      if (dy + y) < 0 or (dy + y) > (self.rows - 1):
        c = c + 0
      else:
        for dx in range(-1, 2):
          if (dx + x) < 0 or (dx + x) > (self.columns - 1):
            c = c + 0
          elif (dx == 0) and (dy == 0):
            c = c + 0
          else:
            if self.board[x+dx][y+dy] == 1:
              #print (x+dx, y+dy, self.board[x][y])
              c = c + 1
    print (x, y, c)
    return c

  def check_action_required(self, x, y):
    '''
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    c = self.count_adjacent_rows(x, y)

    if self.board[x][y] == 0 and c == 3:
      return 1
    if self.board[x][y] == 1 and c < 2:
      return 0
    if self.board[x][y] == 1 and (c == 2 or c == 3):
      return 1
    if self.board[x][y] == 1 and (c > 3):
      return 0


def generate_new_board(board):
  new_board_instance = Board()
  for x in range(0, 8):
    for y in range(0, 8):
      new_board_instance[x][y] = board.check_action_required(x, y)
  return new_board_instance


new_board = Board()

new_board.board[7][4] = 1
new_board.board[7][5] = 1
new_board.board[7][6] = 1
new_board.board[6][6] = 1
new_board.board[5][5] = 1


new_board.printboard()
new_board = generate_new_board(new_board)
new_board.printboard()

















