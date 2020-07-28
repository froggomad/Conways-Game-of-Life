import pygame
import random
import messages
from public_UI import Position, WHITE, BLACK
from automata import GridCell

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Board:
    """A square grid of `num_cells` size"""
    def __init__(self, generation, window_width, window_height, num_cells=25):        
        self._generation = generation
        self._is_user_interaction_enabled = True
        self._num_cells = num_cells
        self.status_bar_height = 80
        self.__size = Size(window_width, window_height-self.status_bar_height)
        self.active_grid = 0
        self.__init_grids__()
        self.draw_grid(self.active_grid)

    def inactive_grid(self):
        # since the board is either 1 or 0, active_grid+1%2 will always return the inverse
        return (self.active_grid +1) %2

    def get_cell_num_for_pos(self, grid_num, position=Position(0,0)):
        row = position.x//self.cell_size().width
        column = position.y//self.cell_size().height
        cell = self.grids[grid_num][(self._num_cells*row)+column]
        if cell.drawn == True:
            print(f"row: {row}, column: {column}, index: {(self._num_cells*row)+column}")
        # TODO: change grid to be dynamic
        return (cell, (self._num_cells*row)+column)
    
    def size(self):
        return self.__size

    def cell_size(self):
        return Size(self.__size.width//self._num_cells, self.__size.height//self._num_cells)

    def get_generation(self):
        return self._generation

    def check_cell_neighbors(self, cell):
        # MARK: TESTING
        cell_index = self.get_cell_num_for_pos(self.active_grid, Position(cell.x, cell.y))[1]
        neighbor_list = []
        try:
            north_neighbor = self.grids[self.active_grid][cell_index-1]
            south_neighbor = self.grids[self.active_grid][cell_index+1]
            east_neighbor = self.grids[self.active_grid][cell_index+self._num_cells]
            west_neighbor = self.grids[self.active_grid][cell_index-self._num_cells]
            north_east_neighbor = self.grids[self.active_grid][cell_index+self._num_cells-1]
            north_west_neighbor = self.grids[self.active_grid][cell_index-self._num_cells-1]
            south_east_neighbor = self.grids[self.active_grid][cell_index+self._num_cells+1]
            south_west_neighbor = self.grids[self.active_grid][cell_index-self._num_cells+1]

            neighbor_list.append(north_neighbor)
            neighbor_list.append(south_neighbor)
            neighbor_list.append(east_neighbor)
            neighbor_list.append(west_neighbor)
            
            neighbor_list.append(north_east_neighbor)
            neighbor_list.append(north_west_neighbor)

            neighbor_list.append(south_east_neighbor)
            neighbor_list.append(south_west_neighbor)
        except IndexError:
            print("invalid neighbor")
            
        self.neighbors = 0
        for neighbor in neighbor_list:
            if neighbor.is_alive() and neighbor.drawn:
                self.neighbors += 1

        if cell.is_alive() == False and cell.drawn == True and cell.neighbors == 3:
            cell.resurrect()

        elif cell.neighbors == 2 or cell.neighbors == 3:
            cell._draw_circle()

        elif cell.neighbors < 2:
            if cell.drawn == True:
                print("underpopulated")
                cell.kill()
        
        elif cell.neighbors > 3:
            if cell.drawn == True:
                print("overpopulated")
                cell.kill()

        #if cell.alive == False and cell.neighbors ==3:
            #cell.resurrect()
        #if cell.neighbors in range(2,4) and cell.alive == True: #cell has 2 or 3 neighbors
            #Do Nothing
        #if cell.neighbors < 2 or cell.neighbors >3: 
            #cell.kill()
        
        return cell

    def increase_generation(self):
        # TODO: animate position based on this value?
        self._generation += 1
        for index in range(self._num_cells*self._num_cells):
            cell = self.grids[self.active_grid][index]

            next_generation = self.check_cell_neighbors(cell)

            self.grids[self.inactive_grid()][index] = next_generation        
        self.active_grid = self.inactive_grid()

    def is_interactable(self):
        return self._is_user_interaction_enabled

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
                self.grids[1][(self._num_cells*x)+y] = rect
                
        
    
    def draw_grid(self, grid_num, choice=None):
        """Create the grid using the current size and generation
            set_grid(0, 0) grids[0] - all dead
            set_grid(1, 1) grids[1] - all alive
            set_grid(0) grids[0] - random
            set_grid(1) grids[None] - random 
        """        
        self.increase_generation()
        # TODO: Improve performance (do we need a nested for loop?)
        # TODO: Draw generation label
        from game import SCREEN
        self._is_user_interaction_enabled = False
        #makes grids of cell_size() (pixels) such that it fits the window size
        # MARK: None/Random choice
        if choice == None:
            for grid in self.grids[grid_num]:
                grid.draw()
                # draw = random.choice([0,1])
                # if draw == 1:
                #     grid._draw_circle()
                # else:
                #     grid._clear _circle()
                #self.check_cell_neighbors(grid)
        self.grids[self.active_grid][7]
        self.draw_status_bar(SCREEN)

        # MARK: Direct Draw
        #self.grids[0][0]._draw_circle(self.grids[0][0].surface)
        #self.grids[0][24]._draw_circle(self.grids[0][1].surface)

        # MARK: Coordinate Draw (preferred)
        #self.get_cell_num_for_pos(0, (Position(self.size().width//2, self.size().height//2)))[0]._draw_circle()
        #self.get_cell_num_for_pos(0, (Position(0, 0)))._draw_circle()

    def draw_status_bar(self, screen):
        """draw user options (window size, num cells, etc)"""
        """draw the current generation in the lower right corner"""
        
        from messages import Button
        
        pygame.display.set_caption(f"Conway's Game of Life")
        #TODO: Move to lower right corner, just under grid
        #rect = pygame.Rect(0, self._size.height, self._size.width, 80)
        status_bar = pygame.Surface((self.__size.width, self.status_bar_height))        
        status_bar.fill(WHITE)
        
        messages.message_display(f"Generation: {self._generation}", status_bar, Position(status_bar.get_rect().width, status_bar.get_rect().height))
        test_button = Button("test", (0,0), status_bar, (255,0,0), fill_color=(255,0,0), text_color = WHITE)
        screen.blit(status_bar, (0, self.__size.height))        
        #TODO: Create options allowing user to change window size, number of cells, etc