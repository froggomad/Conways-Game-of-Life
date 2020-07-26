import pygame

BLUE = (0,0,204)
RED = (255,51,51)

class Automata:
    #set initial state to alive
    def __init__(self):
        self._alive = True
        # TODO: Change this to an appropriate value (RGB?)
        self._color = BLUE
    
    def is_alive(self):
        """returns True if alive, False if dead"""
        return self._alive

    def get_color(self):
        """get the current color"""
        return self._color

    def kill(self):
        """set _alive to False"""
        self._color = RED
        self._alive = False

    def revive(self):
        """set _alive to True"""
        self._color = BLUE
        self._alive = True

    def change_color(self, color):
        # TODO: Change XYZ to something more appropriate
        """Use an XYZ value"""
        self._color = color

class Line_Three(Automata):
    def __init__(self, ):
        super().__init__()
        
    def draw(self, screen, x, cell_size):
        pygame.draw.circle(screen, self._color, (x, cell_size//2), 15, 2)
        pygame.draw.circle(screen, self._color, (x, int(cell_size*1.5)), 15, 2)
        pygame.draw.circle(screen, self._color, (x, int(cell_size*2.5)), 15, 2)