import pygame
import random
import messages
from public_UI import Position, Size, WHITE, BLACK, SCREEN
from automata import GridCell
from copy import copy

class Board:
    """A square grid of `num_cells` size
       ;param board_style: 0: empty, 1: full, None or no choice: Random
    """
    def __init__(self, generation, window_width, window_height, board_style=0, num_cells=25):        
        self._generation = generation
        self._is_user_interaction_enabled = True
        self._num_cells = num_cells
        self.status_bar_height = 80
        self.__size = Size(window_width, window_height-self.status_bar_height)
        self.active_grid = 0
        self.__init_grids__()
        #TODO: always random - allow user to pick
        self.set_active_grid(board_style)
        self.draw_grid(self.active_grid)

    def __str__(self):
        return(f"board#: {self.active_grid}, width: {self.size().width}, height: {self.size().height}, with number of cells(sq): {self._num_cells}")

    def __init_grids__(self):
        """init grids[0] (active) and grids[1] (inactive)"""
        # initialize array in memory
        self.grids = [
            [None for x in range(self._num_cells*self._num_cells)],
            [None for x in range(self._num_cells*self._num_cells)]
        ]        
        # fill array with cells        
        for x in range(self._num_cells):            
            for y in range(self._num_cells):
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                rect = GridCell(x*self.cell_size().width, y*self.cell_size().height, self.cell_size().width, self.cell_size().height)
                self.grids[0][(self._num_cells*x)+y] = rect
                #self.grids[1][(self._num_cells*x)+y] = rect

    def size(self):
        return self.__size

    def cell_size(self):
        return Size(self.__size.width//self._num_cells, self.__size.height//self._num_cells)

    def get_generation(self):
        return self._generation

    def inactive_grid(self):
        # since the board is either 1 or 0, active_grid+1%2 will always return the inverse
        return (self.active_grid +1) %2

    def get_cell_for_pos(self, grid_num, position=Position(0,0)):
        """ given a `Position`, returns the cell and cell's index at that position in a tuple
            :return (cell,index):
        """
        column = position.x//self.cell_size().width
        row = position.y//self.cell_size().height
        cell_index = (self._num_cells*column)+row
        try: 
            cell = self.grids[grid_num][cell_index]
            if cell.is_alive():
                pass
        except IndexError:
            cell = None  
        
        return (cell, cell_index)

    def check_cell_neighbors(self, cell):
        """get count of a cell's alive neighbors"""

        cell_index = self.get_cell_for_pos(self.active_grid, Position(cell.x, cell.y))[1]
        
        neighbor_list = []
        cell.neighbors = 0

        north = Position(cell.x, cell.y - self.cell_size().height)
        south = Position(cell.x, cell.y + self.cell_size().height)
        east = Position(cell.x + self.cell_size().width, cell.y)
        west = Position(cell.x - self.cell_size().width, cell.y)

        north_east = Position(east.x, north.y)
        north_west = Position(west.x, north.y)
        south_east = Position(east.x, south.y)
        south_west = Position(west.x, south.y)

        north_neighbor = self.get_cell_for_pos(self.active_grid, north)[0]        
        south_neighbor = self.get_cell_for_pos(self.active_grid, south)[0]
        east_neighbor = self.get_cell_for_pos(self.active_grid, east)[0]
        west_neighbor = self.get_cell_for_pos(self.active_grid, west)[0]
        north_east_neighbor = self.get_cell_for_pos(self.active_grid, north_east)[0]
        north_west_neighbor = self.get_cell_for_pos(self.active_grid, north_west)[0]
        south_east_neighbor = self.get_cell_for_pos(self.active_grid, south_east)[0]
        south_west_neighbor = self.get_cell_for_pos(self.active_grid, south_west)[0]

        neighbor_list.append(north_neighbor)
        neighbor_list.append(south_neighbor)
        neighbor_list.append(east_neighbor)
        neighbor_list.append(west_neighbor)

        neighbor_list.append(north_east_neighbor)
        neighbor_list.append(north_west_neighbor)
        neighbor_list.append(south_east_neighbor)
        neighbor_list.append(south_west_neighbor)
        
        for neighbor in neighbor_list:
            if neighbor is not None and neighbor.is_alive():
                cell.neighbors += 1

        #assign cell to inactive grid (copying the value)
        self.grids[self.inactive_grid()][cell_index] = copy(cell)

        #modify on inactive grid
        if cell.is_alive():            
            if cell.neighbors == 2 or cell.neighbors == 3:                                
                self.grids[self.inactive_grid()][cell_index].revive()           
            else:  # alive with 0, 1, or 4+ neighbors
                self.grids[self.inactive_grid()][cell_index].kill()
        #cell is dead
        else:
            if cell.neighbors == 3:
                self.grids[self.inactive_grid()][cell_index].revive()

    def increase_generation(self):
        """update the game state to reflect the rules of life"""
        # TODO: animate position based on this value?
        self._generation += 1
        for index in range(self._num_cells*self._num_cells):
            cell = self.grids[self.active_grid][index]

            self.check_cell_neighbors(cell)
        self.active_grid = self.inactive_grid()

    def is_interactable(self):
        return self._is_user_interaction_enabled                
        
    def set_active_grid(self, choice=None):
        """Create the grid using the current size and generation
            set_grid(0, 0) grids[0] - all dead
            set_grid(1, 1) grids[1] - all alive
            set_grid(0) grids[0] - random
            set_grid(1, None) grids[1] - random 
        """ 
        for grid in self.grids[self.active_grid]:
                grid.draw()

        if choice == None:
            for grid in self.grids[self.active_grid]:
                draw = random.choice([0,1])
                if draw == 1:
                    grid._draw_circle()
        elif choice == 1:
            for grid in self.grids[self.active_grid]:
                grid._draw_circle()
        else:
            for grid in self.grids[self.active_grid]:
                grid._clear_circle()          


    def draw_grid(self, grid_num):                
        self._is_user_interaction_enabled = False
        
        for grid in self.grids[grid_num]:
            grid.draw()
            if grid.is_alive():
                grid._draw_circle()
            else: 
                grid._clear_circle()
                
        self.draw_status_bar(SCREEN)

    def draw_status_bar(self, screen):
        """draw user options (window size, num cells, etc)"""
        """draw the current generation in the lower right corner"""
        
        from messages import Button
        
        pygame.display.set_caption(f"Conway's Game of Life")
        status_bar = pygame.Surface((self.__size.width, self.status_bar_height))        
        status_bar.fill(WHITE)
        
        messages.message_display(f"Generation: {self._generation}", status_bar, Position(status_bar.get_rect().width, status_bar.get_rect().height))
        test_button = Button("test", (0,0), status_bar, (255,0,0), fill_color=(255,0,0), text_color = WHITE)
        screen.blit(status_bar, (0, self.__size.height))        
        #TODO: Create options allowing user to change window size, number of cells, etc