import pygame
from public_UI import WHITE, BLACK, SCREEN

BLUE = (0,0,204)
RED = (255,51,51)

class GridCell:
    def __init__(self, x,  y, width, height):        
        super().__init__()
        # Position
        self.x = x
        self.y = y
        # Size
        self.width = width
        self.height = height
        # State
        self.drawn = False
        self.__alive = False       
        self.__color = BLUE
        self.neighbors = 0
        #create a clear surface to draw on
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
    def _draw_circle(self):
        self.drawn = True
        self.__alive = True
        center_y = self.height//2
        center_x = self.width//2

        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2

        return pygame.draw.circle(self.surface, self.__color, (center_x, center_y), radius)

    def _clear_circle(self):
        self.drawn = False
        center_y = self.height//2
        center_x = self.width//2
        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2
        pygame.draw.circle(self.surface, WHITE, (center_x, center_y), radius)
        
    def draw(self):        
        #from game import SCREEN, BLACK
        rect = pygame.Rect(0,0,
                           self.width, self.height)
        SCREEN.blit(self.surface, (self.x, self.y))
        return pygame.draw.rect(self.surface, BLACK, rect, 1)

    def is_alive(self):
        """returns True if alive, False if dead"""
        return self.__alive
    
    def get_color(self):
        """get the current color"""
        return self.__color
    
    def kill(self):
        """set _alive to False, change color, redraw"""
        if self.__alive:
            self.__color = RED
            self.__alive = False
            self._draw_circle()
    
    def revive(self):
        """set _alive to True"""
        self.__color = BLUE
        self.__alive = True        
    
    def change_color(self, color):
        # TODO: Change XYZ to something more appropriate
        """Use an RGB value"""
        self.__color = color

class Automata:
    #set initial state to alive
    def __init__(self, num, name):
        self.cells: GridCell = [None for num in range(num)]
        self.name = name

class Blinker(Automata):
    def __init__(self, cell_array):
        super().__init__(len(cell_array), "Blinker")
        self.cells = cell_array

    def draw_blink(self):
        for cell in self.cells:
            cell._draw_circle()
            