# sway ly
# animation of the Rasengan Jutsu
# 2017-08-24

# imports
import pygame

# bones
pygame.init()
FPS = pygame.time.Clock()

# window
SCREEN = (500, 500)
screen = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("RASENGAN")

# colours
SKY_BLUE = (105, 210, 245)
WHITE = (255, 255, 255)
WHITE_BLUE = (141, 220, 247)
DARK_BLUE = (16, 149, 194)
DARK_BLUE_1 = (69, 200, 245)
SHADOW = (56, 56, 56)
SHADOW_1 = (124, 125, 125)

done = False

# original coordinates
location_x = 250 # center of circle is where its drawn from
location_y = 200
shadow_location_x = 135
shadow_location_y = 435

# offsets
shadow_width_offset = 0

# location change
location_x_change = 5
location_y_change = 5
shadow_location_x_change = 0.5
shadow_location_y_change = 0.5


colour = DARK_BLUE_1
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True # exit while loop



    screen.fill(WHITE_BLUE)
    for offset_1 in range(0, 90, 30):

        if offset_1 == 0:
            colour = DARK_BLUE_1

        elif offset_1 == 30:
            colour = SKY_BLUE

        elif offset_1 == 60:
            colour = WHITE_BLUE

        pygame.draw.circle(screen, colour, [location_x, location_y], (150 - (2 * offset_1)))

        location_x += location_x_change
        location_y += location_y_change

        if location_x > 260:
            location_x_change = location_x_change * -1

        if location_x < 200:
            location_x_change += 5

        if location_y > 260:
            location_y_change = location_y_change * -1

        if location_y < 200:
            location_y_change += 5


    pygame.draw.ellipse(screen, SHADOW_1, (shadow_location_x, shadow_location_y, 200 + shadow_width_offset, 50), 0)
    # leaving the final parameter in the .draw.ellipse fills the ellipse with the colour argument
    shadow_location_x += shadow_location_x_change

    shadow_width_offset += 20

    if shadow_width_offset > 100:
        shadow_width_offset = 0

    if shadow_location_x > 138:
        shadow_location_x_change += -1

    if shadow_location_x < 132:
        shadow_location_x_change += 1




    FPS.tick(60)
    pygame.display.update()


pygame.quit() # close program
# end
