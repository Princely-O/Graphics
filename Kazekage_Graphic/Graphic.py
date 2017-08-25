# sway ly
# practice lab
# draw graphic using new shapes learned, with different colours, offsets, for loops, and text
import datetime
import pygame
from math import pi

print (datetime.date.today())

pygame.init()
FPS = pygame.time.Clock()

# window
SCREEN_SIZE = (500, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("KAZEKAGE")

BLACK = (3, 5, 5)
WHITE = (247, 249, 250)
RED = (255, 0, 0)

PI = pi

done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.arc(screen, WHITE, [100, 150, 50, 200], 0, PI/2, 15) # square brackets rep. the rectangle the arc is within
    pygame.draw.arc(screen, WHITE, [100, 150, 50, 200], 3*PI/2, 2*PI, 15)
    pygame.draw.line(screen, WHITE, (125, 155), (340, 155), 15)
    pygame.draw.line(screen, WHITE, (333, 155), (333, 325), 15)
    pygame.draw.arc(screen, WHITE, [325.9999999999999, 260, 48, 90], PI, 2*PI, 15)
    for line_offset in range(0, 100, 50): # offset; start at line_offset = 0 and skips by 50 to 100. So, 2 lines will be printed
        pygame.draw.line(screen, WHITE, (170, 220 + line_offset), (299, 220 + line_offset), 15)

    for vertline_offset in range(0, 230, 115):
        pygame.draw.line(screen, WHITE, (177.5 + vertline_offset, 220), (177.5 + vertline_offset, 270), 15)

    pygame.draw.line(screen, WHITE, (232.5, 200), (232.5, 330), 15)
    pygame.draw.line(screen, WHITE, (150, 340), (304, 320), 15)
    pygame.draw.arc(screen, WHITE, [150, 150, 160, 50], 6*PI/5, 2*PI, 15)
    pygame.draw.arc(screen, WHITE, [150, 285, 160, 90], 22*PI/12, PI/4, 15)

    # text
    #font
    font = pygame.font.Font("C:\\Windows\\Fonts\\Carlito-Bold.ttf", 90) # selecting font and size

    text = font.render("KAZEKAGE", True, RED) # creating font stamp to be used
    # if second parameter is False, text appears more jagged (not anti-aliased)

    screen.blit(text, [55, 430])


    # use offset for middle rectangle
    pygame.display.update() # IMPORTANT: update screen after any change

    FPS.tick(60)
pygame.quit()
# end