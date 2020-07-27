import pygame

BLUE = (0,0,204)
RED = (255,51,51)

class Automata:
    #set initial state to alive
    def __init__(self):
        self._alive = True
        # TODO: Move to cell class
        self._color = BLUE
    # TODO: Move to cell class
    def is_alive(self):
        """returns True if alive, False if dead"""
        return self._alive
    # TODO: Move to cell class
    def get_color(self):
        """get the current color"""
        return self._color
    # TODO: Move to cell class
    def kill(self):
        """set _alive to False"""
        self._color = RED
        self._alive = False
    # TODO: Move to cell class
    def revive(self):
        """set _alive to True"""
        self._color = BLUE
        self._alive = True
    # TODO: Move to cell class
    def change_color(self, color):
        # TODO: Change XYZ to something more appropriate
        """Use an RGB value"""
        self._color = color
    # TODO: rename draw cell
    

class GridCell(Automata):
    def __init__(self, x,  y, width, height):        
        super().__init__()        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width, height))
        #self.draw()
        
    def _draw_circle(self, surface):
        center_y = self.height//2
        if self.width > self.height:
            radius = self.height//2
        else:
            radius = self.width//2
            #self.x, int(row*height + center_y)
            
        return pygame.draw.circle(surface, self._color, (self.width//2, center_y), radius)

    # def draw(self, x, y, width, height):
    def draw(self):        
        from game import SCREEN, BLACK
        rect = pygame.Rect(self.x*self.width, self.y*self.height,
                                self.width, self.height)
        return pygame.draw.rect(SCREEN, BLACK, rect, 1)


class Line_Three(Automata):
    def __init__(self):
        super().__init__()
        self.cells = []

    def draw(self, surface, x, width, height, starting_row, count):        
        #surface, color, (x,y), radius, width
        for row_num in range(starting_row, count):
            self.cells.append( self._draw_circle(surface, x, width, height, row_num) )

        #pygame.draw.circle(surface, self._color, (x, int( (row+1*height) + center_y)), radius, 2)
        # pygame.draw.circle(surface, self._color, (x, int( (row+2*height) + center_y)), radius, 2)