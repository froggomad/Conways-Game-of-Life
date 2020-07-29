import pygame
import sys
from board import Board
import messages
from public_UI import *

pygame.init()

board = Board(0, WINDOW_WIDTH, WINDOW_HEIGHT, None, 50)
pause = False
def paused():
    global pause
    board._is_user_interaction_enabled = True
    while pause == True:        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    board._is_user_interaction_enabled = True
                    unpause()
        board_size = board.size()
        pause_line_1 = messages.message_display("Paused".upper(), SCREEN, Position(board_size.width//2, board_size.height//2), RED)
        #line 2
        messages.message_display("(press 'p' to continue)", SCREEN, Position(board_size.width//2, board_size.height//2 + pause_line_1.height), CYAN)
        pygame.display.update()

def unpause():
    global pause
    pause = False
    board._is_user_interaction_enabled = False

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
        if event.type == pygame.MOUSEBUTTONDOWN and pause == True and board._is_user_interaction_enabled == True:            
            if event.button == 0:
                mouse_pos = pygame.mouse.get_pos()
                board.get_cell_num_for_pos(0, Position(mouse_pos[0], mouse_pos[1]))[0]._draw_circle()

# MARK: Testing
board.grids[0][(board._num_cells*board._num_cells)//2-1]._draw_circle()
board.grids[0][(board._num_cells*board._num_cells)//2]._draw_circle()
board.grids[0][(board._num_cells*board._num_cells)//2+1]._draw_circle()
SCREEN.fill(WHITE)
while True:
    print(f"######MAIN LOOP#######")
    # TODO: use dt to control movement speed of objects?
    dt = CLOCK.tick(FPS)
    #SCREEN.fill(WHITE)
    board.increase_generation()
    board.draw_grid(board.active_grid)
    #capture events (mouse clicks, closing the game, etc)
    handle_events()
    pygame.display.flip()


# MARK: Reference (unused)

#animation x value wrap around - x is an iterator
    # x = cell_size.width//2
    # if x >= board_size.width:
    #     x = cell_size.width//2
    # else:
    #     x += cell_size.width