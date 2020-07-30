import pygame
from public_UI import WHITE, BLACK, SCREEN, FILL_COLOR, DEAD_COLOR, ALIVE_COLOR
from messages import *

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
        self.__age = 1
        self.max_age = 101
        self.__color = self.age_color()
        self.neighbors = 0
        #create a clear surface to draw on
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
        
    
    def get_age(self):
        return self.__age

    def __str__(self):
        return (f"x: {self.x}, y: {self.y}, width: {self.width}, color: {self.color}, alive: {self.alive}")
        
    def _draw_circle(self):
        self.__alive = True
        #message_display(f"{self.neighbors}", self.surface)
        pygame.draw.ellipse(self.surface, self.__color, self.surface.get_rect())
        
    def _clear_circle(self):
        self.__alive = False        
        pygame.draw.ellipse(self.surface, DEAD_COLOR, self.surface.get_rect())
        
    def draw(self):
        SCREEN.blit(self.surface, (self.x, self.y))

    def is_alive(self):
        """returns True if alive, False if dead"""
        return self.__alive
    
    def get_color(self):
        """get the current color"""
        return self.age_color()
    
    def kill(self):
        """mark to be cleared on next generation"""
        if self.__alive:
            self.__alive = False

    def age_color(self):
        #rgb value percentage based on age        
        #0-youth
        if self.get_age() >= self.max_age:
            self.__age = 1
        current = self.get_age()/self.max_age
        youth = 0.25*self.max_age
        if self.get_age() <= youth:            
            return (0,255*current+50,0)
        #youth-midlife
        elif self.get_age() <= int(0.5*self.max_age):
            return (255*current,0,0)
        #midlife-old_age
        elif self.get_age() <= int(0.75*self.max_age):
            return (0,0,255*current)
        #old_age
        else:
            #max age, step up to 1
            blue = self.__color[2]
            sure = blue + current*255
            max = 255
            if sure > max:
                sure = max
            return (0,current*255,sure)
    
    def revive(self):
        # TODO: Special Effects
        """mark to be drawn on next generation"""
        self.__color = self.age_color()
        self.__alive = True
        self.__age += 1
    
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
            