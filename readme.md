# Conway's Game of Life with pygame/Python

<a href="https://conways-game-of-life.webflow.io/">"Marketing" Page</a>

### Conway's Game of Life is a simulation of what happens when a certain cell:

* is overpopulated
* is underpopulated
* is dead
* is revived/reproduced

Several interesting variations can take place, some making large stable structures, some that slowly decay, some that continuously transform. All of this based on simple rules that each cell must obey

<hr>

As cells age, their color changes subtly. However, at various life stages, their color changes drastically. This is meant to mimic human life and it's various stages.

* Youth: green
* Prime: red
* Middle Age: deep blue
* Old Age: bright blue

When a cell reaches a certain age, it dies and a new cell is immediately born in its place, continuing the circle of life.

<hr>

### Geek Stuff

#### Draw circle method (and accessing grid squares)

* each grid square has a method to draw a circle in it
* square can be accessed directly (`grids[0][0]`) to get the first square, then it's arranged by column, so `grids[0][1]` would be the square under the first one
* squares can also be accessed by  coordinates (preferred) to get a particular grid square in the array 
    * note: lookup is using math and subscripting to find the square rather than searching the array for a square between those coordinates
    * note**: coordinate lookup is preferred not for speed (since it's a moot point) but for scalability - if the user changes the number of cells, we want their current cells to appear in the same coordinate space

###### Reference/Unused
```
animation x value wrap around - x is an iterator
     x = cell_size.width//2
     if x >= board_size.width:
         x = cell_size.width//2
     else:
         x += cell_size.width
 ```
