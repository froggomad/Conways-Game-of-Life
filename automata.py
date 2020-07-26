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
        # TODO: Think about the calculation for height and fix it
    def draw(self, surface, x, width, height, row):
        #surface, color, (x,y), radius, width
        center_y = height//2
        if width > height:
            radius = height//2
        else:
            radius = width//2

        pygame.draw.circle(surface, self._color, (x, int(row*height + center_y)), radius, 2)
        pygame.draw.circle(surface, self._color, (x, int( (row+1*height) + center_y)), radius, 2)
        pygame.draw.circle(surface, self._color, (x, int( (row+2*height) + center_y)), radius, 2)