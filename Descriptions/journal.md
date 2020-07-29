## Day 1 (Saturday): 

* imported pygame
* Created board (grid containing "cells")
* Created Automata class

**Biggest challenge so far has been figuring out how everything scales and is positioned relatively (avoiding magic numbers)**

## Day 2 (Sunday):

* created Size and Position classes
* made everything scale dynamically so in the future, the user can select a window height and number of cells, and things will scale nicely, including automata
* exploring pygame surfaces rather than drawing directly to the screen (allows for adding subviews)
* imported draw_message method from another project and modified it so it draws text at a position passed in or 0,0 if nothing is passed in

TIL:

* Blit to draw, flip() to put it into memory

**Biggest challenge so far has been getting everything to scale dynamicaly**

## Day 3 (Monday):

* drawing circles previously wasn't being done in a way that they could be drawn programatically per grid square easily
    * drawing grid squares by bltting a surface then drawing a rect on it so circles can be drawn on top of the blitted surface
    * fixed grid cell coordinate system
    * fixed method to draw circle (it was always drawing at 0,0)
    * moved things around to be more organized in an OOP fashion.
    * made public_UI file to avoid circular references

## Day 4 (Tuesday):
* Spent a good portion of the day debugging erratic behavior

## Day 5 (Wednesday):
* Debug neighbors
* Buttons
* App is close to a minimally working state, and close to MVP (need to figure out cell neighbors and implement buttons)