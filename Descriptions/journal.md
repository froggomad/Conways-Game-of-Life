## Day 1: 

* imported pygame
* Created board (grid containing "cells")
* Created Automata class

- Biggest challenge so far has been figuring out how everything scales and is positioned relatively (avoiding magic numbers)

## Day 2:

* created Size and Position classes
* made everything scale dynamically so in the future, the user can select a window height and number of cells, and things will scale nicely, including automata
* exploring pygame surfaces rather than drawing directly to the screen (allows for adding subviews)
* imported draw_message method from another project and modified it so it draws text at a position passed in or 0,0 if nothing is passed in

- Biggest challenge so far has been getting everything to scale dynamicaly