#Conway's Game of Life

Stolen from [Wikipedia](http://en.wikipedia.org/wiki/Conway's_Game_of_Life):

> The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
> 
* Any live cell with fewer than two live neighbours dies, as if caused by under-population.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overcrowding.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
* The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a pure function of the preceding one). The rules continue to be applied repeatedly to create further generations.  

Possible ways of visualising this using Python include (but are not limited to):

* the *curses* module [Unix text console tool]
* Pygame
* one of the GUI libraries - e.g. PyGtk, PyQt, TkInter, WxPython
* in a web page

The underlying calculations can be done with the help of the NumPy library - although other approaches are doubtless possible.

As an example of it's use, you can have a look at some code I wrote to check solutions of the [Eight Queens puzzle](https://github.com/dgh--/EightQueens).

Further reading:
http://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
