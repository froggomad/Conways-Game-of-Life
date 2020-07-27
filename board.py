import pygame
import messages
from messages import Position

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
        self._size = Size(window_width, window_height-self.status_bar_height)
        self.__init_grids__()

    def cell_num_for_pos(self, grid_num, position=Position(0,0)):
        row = position.x//self.cell_size().width
        column = position.y//self.cell_size().height
        # TODO: change grid to be dynamic
        return (self.grids[grid_num][(self._num_cells*row)+column])
    
    def size(self):
        return self._size

    def cell_size(self):
        return Size(self._size.width//self._num_cells, self._size.height//self._num_cells)

    def get_generation(self):
        return self._generation

    def increase_generation(self):
        self._generation += 1

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
                rect = pygame.Rect(x*self.cell_size().width, y*self.cell_size().height,
                                self.cell_size().width, self.cell_size().height)

                self.grids[0][(self._num_cells*x)+y] = rect
                self.grids[1][(self._num_cells*x)+y] = rect
    
    def draw_grid(self, num):
        """Create the grid using the current size and generation"""        
        self.increase_generation()
        # TODO: Improve performance (do we need a nested for loop?)
        # TODO: Draw generation label
        from game import SCREEN
        from game import BLACK
        self._is_user_interaction_enabled = False
        #makes grids of cell_size() (pixels) such that it fits the window size
        for grid in self.grids[num]:
            pygame.draw.rect(SCREEN, BLACK, grid, 1)
        self.draw_status_bar(SCREEN)

    def draw_status_bar(self, screen):
        """draw the current generation in the lower right corner"""
        from game import WHITE
        pygame.display.set_caption(f"Conway's Game of Life")
        #TODO: Move to lower right corner, just under grid
        #rect = pygame.Rect(0, self._size.height, self._size.width, 80)
        status_bar = pygame.Surface((self._size.width, self.status_bar_height))
        status_bar.fill(WHITE)
        messages.message_display(f"Generation: {self._generation}", status_bar, Position(status_bar.get_rect().width, status_bar.get_rect().height))
        screen.blit(status_bar, (0, self._size.height))        
        #TODO: Create options allowing user to change window size, number of cells, etc