#Here's my landscape! 

# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
from PIL import Image
import random
import time

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
framecount = 0

building_x = 0
building_y = 200
sun_x = 340 
sun_y = 80
sun_speed = 4 
moon_speed = 4
moon_x = 340
moon_y = 360
star_x = 50
star_y = 50
cloud_x = 0
cloud_speed = 7

day_sky = pygame.Color("#87ceeb")
night_sky = pygame.Color("#4B0082")

day_window = "#A8CCD7"
night_window = "#F8DA77"
window_color = day_window
star_base_color = pygame.Color(255, 253, 179)
starcolor = night_sky.lerp(star_base_color, .5)

sun_inner = (255, 235, 150)
sun_outer = (255, 253, 179)
moon_outer = (255, 255, 255)
moon_inner = (230, 240, 255)


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

            
    ###DRAWING FUNCTIONS###

    #building drawing function
    def drawbuilding(building_x, building_y, building_color):
        pygame.draw.rect(screen, building_color, (building_x, building_y, 100, 480), 50)
        
        for y in range(15, 400, 45):
            pygame.draw.rect(screen, window_color, (building_x + 15, building_y + y, 25, 25), 15)
            pygame.draw.rect(screen, window_color, (building_x + 60, building_y + y, 25, 25), 15)

    #cloud drawing function 
    def drawcloud(cloud_x, cloud_y):
        pygame.draw.circle(screen, (190,190,215), (cloud_x, cloud_y), 20)
        pygame.draw.circle(screen, (190,190,215), (cloud_x + 20, cloud_y), 20)
        pygame.draw.circle(screen, (210,200,215), (cloud_x + 35, cloud_y), 20)
        pygame.draw.circle(screen, (190,190,215), (cloud_x + 50, cloud_y), 20)
        pygame.draw.circle(screen, (200,200,225), (cloud_x + 70, cloud_y), 20)
        pygame.draw.circle(screen, (200,190, 215), (cloud_x + 30, cloud_y - 20), 20)

    #star drawing function
    def drawstar(star_x, star_y):
        pygame.draw.polygon(screen, (star_base_color), ((star_x, star_y + 3), (star_x + 15, star_y - 20), (star_x + 30, star_y + 3)))
        pygame.draw.polygon(screen, (star_base_color), ((star_x, star_y - 12), (star_x + 15, star_y + 10), (star_x + 30, star_y - 12)))

    
    ###DRAWING COMMANDS###

    #make the sky colour fade depending on sun height
    sky_color = night_sky.lerp(day_sky, 70/sun_y)
    screen.fill(sky_color)

    #draw sun that rises and falls (hold mouse button)
    pygame.draw.circle(screen, sun_outer, (sun_x, sun_y), 50)
    pygame.draw.circle(screen, sun_inner, (sun_x, sun_y), 30)
    sun_y += sun_speed
    if sun_y == 80: 
        sun_speed = 0
        if framecount == 200:
            sun_speed = 4   
    elif sun_y == 360:
        sun_speed = 0
        if framecount == 200:
            sun_speed = -4
            #note: these statements differ by the (-) sign of the sun_speed (so the object reverses direction depending on top/bottom location), so they are separated 
            
    #draw moon that rises and falls opposite the sun
    pygame.draw.circle(screen, moon_outer, (moon_x, moon_y), 50)
    pygame.draw.circle(screen, moon_inner, (moon_x, moon_y), 30)
    moon_y -= moon_speed
    if moon_y == 80: 
        moon_speed = 0
        if framecount == 200:
            moon_speed = -4
            framecount = 0
    elif moon_y == 360:
        moon_speed = 0
        if framecount == 200:
            moon_speed = 4
            framecount = 0
    
            
    # draw buildings in various colors and sizes
    drawbuilding(building_x, building_y, (150, 180, 180))
    drawbuilding(building_x + 100, building_y - 50, (150, 200, 200))
    drawbuilding(building_x + 200, building_y + 20, (167, 167, 187))
    drawbuilding(building_x + 300, building_y + 50, (160, 140, 180))
    drawbuilding(building_x + 400, building_y - 10, (160, 160, 220))
    drawbuilding(building_x + 500, building_y + 40, (160, 190, 190))

    #daytime effects
    if sun_y < 180:
        #turn off window lights
        window_color = day_window

        #animate clouds across the sky
        drawcloud(cloud_x, 70)
        drawcloud(cloud_x + 70, 40)
        drawcloud(cloud_x + 220, 90)
        cloud_x += cloud_speed
    
    #nighttime effects
    elif sun_y > 270:
        cloud_x = 0
        #turn on window lights
        window_color = night_window

        #staggered star appearance time
        if framecount > 70:
            drawstar(30, 60)
            if framecount > 80:
                drawstar(75, 125)
                if framecount > 90:
                    drawstar(150, 35)
                    if framecount > 95:
                        drawstar(230, 80)
                        if framecount > 100:
                            drawstar(420, 154)
                            if framecount > 105:
                                drawstar(260, 170)
                                if framecount > 110:
                                    drawstar(440, 40)

    framecount += 1
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
