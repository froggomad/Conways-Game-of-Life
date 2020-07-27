#message_display helper
import pygame
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, surface, position=Position(0,0), color=(0,0,0)):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText, color)
    # I don't really want to manipulate the center property, but couldn't figure out how to access x and y directly
    # So, use the center, but adjust so it's actually using the x,y passed in to position the text rectangle
    if position.x > surface.get_rect().width//2:
        text_x = position.x - (TextRect.width//2)
    elif position.x < surface.get_rect().width//2:
        text_x = position.x + (TextRect.width//2)
    else:
        text_x = position.x

    if position.y > surface.get_rect().height//2:
        text_y = position.y - (TextRect.height//2)
    elif position.y < surface.get_rect().height//2:
        text_y = position.y + (TextRect.height//2)
    else:
        text_y = position.y
    TextRect.center = (text_x, text_y)
    # draw it
    surface.blit(TextSurf, TextRect)
    return TextRect