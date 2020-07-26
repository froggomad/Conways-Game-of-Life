import pygame
import sys
from board import Board
from automata import Line_Three

pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1650
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 5
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)

board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, 25)
cell_size = board.cell_size()
board_size = board.size()
x = cell_size.width//2
line = Line_Three()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

while True:
    # TODO: use dt to control movement speed of objects?
    dt = CLOCK.tick(FPS)
    SCREEN.fill(WHITE)
    board.draw_grid()
    line.draw(SCREEN, x, cell_size.width, cell_size.height, 0, 3)
    #capture events (mouse clicks, closing the game, etc)
    handle_events()

    if x >= board_size.width:
        x = cell_size.width//2
    else:
        x += cell_size.width
    # double buffers by default
    pygame.display.flip()

    