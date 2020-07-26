import pygame
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
        self._size = Size(window_width, window_height)
    
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

    def set_board_size(self, num_cells):
        # TODO
        """Set the size of the board in a square (ie 25 is 25x25)"""
    
    def draw_grid(self):
        """Create the grid using the current size and generation"""
        self.increase_generation()
        # TODO: Improve performance (do we need a nested for loop?)
        # TODO: Draw generation label
        from game import SCREEN
        from game import BLACK
        self._is_user_interaction_enabled = False
        #makes grids of _size (pixels) such that it fits the window size
        for x in range(self._num_cells):            
            for y in range(self._num_cells):
                rect = pygame.Rect(x*self.cell_size().width, y*self.cell_size().height,
                                self.cell_size().width, self.cell_size().height)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)

    def draw_status_bar(self):
        """draw the generation in the lower right corner"""
        pygame.display.set_caption(f"Generation: {self._generation}")
        #TODO: Move to lower right corner, just under grid
        #TODO: Create options allowing user to change window size, number of cells, etc