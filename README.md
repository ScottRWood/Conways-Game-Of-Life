# Conways-Game-Of-Life

An implementation of Conway's Game of Life in Python, the results are displayed on a simple Tkintr GUI by embedding a figure from MatPlotLib. Rules have also been implemented for a 3-dimensional interpretation (though need refining).


## Info

The Game of Life is a Cellular Automaton designed by John Conway, the rules are fairly simple. You set an initial environment, in the case of this program it is defined by an x-dimension, y-dimension and a probability of a cell being alive initially. Every cell can interact with its eight neighbouring cells. For every step through time the following can occur:

* If the cell has one or fewer alive neighbours it dies (from underpopulation)
* If the cell has four or more neighbours it dies (from overpopulation)
* If the cell is dead and has exactly three neighbours it comes to life (from reproduction)
* Any other case leaves the cell unaffected
