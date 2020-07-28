import pygame
import sys
from board import Board
from automata import Blinker
import messages
from public_UI import Size, Position


pygame.init()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1650
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 5
BLACK = (0, 0, 0)
WHITE = (245, 245, 245)
RED = (255, 0, 0)
CYAN = (0,186,186)

board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, 50)
cell_size = board.cell_size()
board_size = board.size()
x = cell_size.width//2
line = Blinker()
pause = False
def paused():
    global pause
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()
        pause_line_1 = messages.message_display("Paused".upper(), SCREEN, Position(board_size.width//2, board_size.height//2), RED)
        #line 2
        messages.message_display("(press 'p' to continue)", SCREEN, Position(board_size.width//2, board_size.height//2 + pause_line_1.height), CYAN)
        pygame.display.update()
        CLOCK.tick(15)

def unpause():
    global pause
    pause = False

def handle_events():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = True
                paused()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    board.get_cell_num_for_pos(0, Position(mouse_pos[0], mouse_pos[1]))._draw_circle()
                    

while True:
    # TODO: use dt to control movement speed of objects?
    dt = CLOCK.tick(FPS)
    SCREEN.fill(WHITE)
    board.draw_grid(0)
    #capture events (mouse clicks, closing the game, etc)
    handle_events()
    #animation x value wrap around
    if x >= board_size.width:
        x = cell_size.width//2
    else:
        x += cell_size.width
    # double buffers by default
    pygame.display.flip()

    