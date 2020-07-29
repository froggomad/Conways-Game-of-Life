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
        self.__alive = False       
        self.__color = BLUE
        self.neighbors = 0
        #create a clear surface to draw on
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def __str__(self):
        return (f"x: {self.x}, y: {self.y}, width: {self.width}, color: {self.color}, alive: {self.alive}")
        
    def _draw_circle(self):
        self.__alive = True
        return pygame.draw.ellipse(self.surface, self.__color, self.surface.get_rect())
        
    def _clear_circle(self):
        self.__alive = False
        return pygame.draw.ellipse(self.surface, WHITE, self.surface.get_rect())
        
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
        """mark to be cleared on next generation"""
        if self.__alive:
            self.__color = RED
            self.__alive = False
    
    def revive(self):
        # TODO: Special Effects
        """mark to be drawn on next generation"""
        self.__color = BLUE
        self.__alive = True
    
    def change_color(self, color):
        """Use an RGB or pre-defined color value"""
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
            