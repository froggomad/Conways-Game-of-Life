#message_display helper
import pygame
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text, surface, position=Position(0,0)):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    # I don't really want to manipulate the center property, but couldn't figure out how to access x and y directly
    # So, use the center, but adjust so it's actually using the x,y passed in to position the text rectangle
    if position.x >= TextRect.width//2:
        text_x = position.x - (TextRect.width//2)
    else:
        text_x = position.x + (TextRect.width//2)

    if position.y >= TextRect.height//2:
        text_y = position.y - (TextRect.height//2)
    else:
        text_y = position.y + (TextRect.height//2)
    TextRect.center = (text_x, text_y)
    # draw it
    surface.blit(TextSurf, TextRect)
    return TextRect