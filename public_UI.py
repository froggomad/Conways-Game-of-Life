import pygame

class Size:
    """creates an object with a height and width rather than using a tuple"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return(f"width: {self.width}, height: {self.height}")

class Position:
    """creates an object with an x and y coordinate rather than using a tuple"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return (f"x: {self.x}, y: {self.y}")

# MARK: Colors
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
GRAY = (105,105,105)
RED = (255, 0, 0)
CYAN = (0,186,186)
BLUE = (0,0,204)
GREEN = (0,204,0)

FILL_COLOR = BLACK
DEAD_COLOR = FILL_COLOR
ALIVE_COLOR = RED

# MARK: Screen Parameters
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 40
pause = True