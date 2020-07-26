import pygame

class Board:
    """A square grid of `num_cells` size"""
    def __init__(self, generation, window_width, num_cells=25):
        self._generation = generation
        self._is_user_interaction_enabled = True
        self._num_cells = num_cells
        self._cell_size = window_width//num_cells
        self._size = window_width
    
    def size(self):
        return self._size

    def cell_size(self):
        return self._cell_size

    def get_generation(self):
        return self._generation

    def increase_generation(self):
        self._generation += 1

    def is_interactable(self):
        return self._is_user_interaction_enabled

    def set_board_size(self, num_cells):
        """Set the size of the board in a square (ie 25 is 25x25)"""
        self._num_cells = num_cells
        self._cell_size = num_cells
    
    def draw_grid(self):
        """Create the grid using the current size and generation"""
        # TODO: Improve performance (do we need a nested for loop?)
        # TODO: Draw generation label
        from game import WINDOW_HEIGHT
        from game import WINDOW_WIDTH
        from game import SCREEN
        from game import BLACK
        self._is_user_interaction_enabled = False
        #makes grids of _size (pixels) such that it fits the window size
        for x in range(WINDOW_WIDTH//self._num_cells):            
            for y in range(WINDOW_HEIGHT//self._num_cells):                
                    rect = pygame.Rect(x*self._cell_size, y*self._cell_size,
                                    self._cell_size, self._cell_size)
                    pygame.draw.rect(SCREEN, BLACK, rect, 1)

    def draw_status_bar(self):
        """draw the generation in the lower right corner"""