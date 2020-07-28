# Conway's Game of Life with pygame/Python

### Conway's Game of Life is a simulation of what happens when a certain cell:

* is overpopulated
* is underpopulated
* is dead
* is revived/reproduced

Several interesting variations can take place, some making large stable structures, some that slowly decay, some that continuously transform. All of this based on simple rules that each cell must obey


### Geek Stuff

#### Draw circle method (and accessing grid squares)

* each grid square has a method to draw a circle in it
* square can be accessed directly (`grids[0][0]`) to get the first square, then it's arranged by column, so `grids[0][1]` would be the square under the first one
* squares can also be accessed by  coordinates (preferred) to get a particular grid square in the array 
    * note: lookup is using math and subscripting to find the square rather than searching the array for a square between those coordinates
    * note**: coordinate lookup is preferred not for speed (since it's a moot point) but for scalability - if the user changes the number of cells, we want their current cells to appear in the same coordinate space