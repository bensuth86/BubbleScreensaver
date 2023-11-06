"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
import sys

class Bubble():

        def __init__(self, vy, grow_rate):

                self.x = random.randrange(0,Screensaver.screen_width) #random positions along screen width
                self.y = random.randrange(0,Screensaver.screen_height)# ""                                      "" height
                self.vy = vy
                self.growrate = grow_rate
                self.radius = 1

        # Define Bubble radius as function of height
        def calculate_radius(self):


                self.radius = (Screensaver.screen_height- self.y)/self.growrate
                self.radius = int(self.radius)

                #set minimum bubble radius
                if self.radius < 2:
                        self.radius=3

        def rising(self):

                self.y -= self.vy # Increase bubble height

                self.calculate_radius()

                #Check if above screen
                if self.y < 0:

                        self.x = random.randrange(Screensaver.screen_width) # random position along x
                        self.y = random.randrange(Screensaver.screen_height+5,Screensaver.screen_height+20) # set y position within range from 5-20 below screen edge

                        self.radius = 2   # reset starting radius to 2 if bubble height off screen

##                        bubble_pop.play()

class Screensaver():


        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)

        # Set the width and height of the screen [width, height]
        screen_width = 1400
        screen_height= 700
        size = (screen_width, screen_height)

        def __init__(self, total): #total bubbles

                # initilise pygame window
                pygame.init()
                pygame.display.set_caption("Bubbles")

                self.clock = pygame.time.Clock() # Used to manage how fast the screen updates

                self.screen = pygame.display.set_mode(Screensaver.size) # set screensize
                self.background_image = pygame.image.load("deep_sea.jpg").convert()

                self.total = total
                self.all_bubbles=[] # Bubbles objects stored to

                # Create bubbles
                for i in range(self.total): # create 20 bubbles

                                    #Bubble(speed, grow_rate)
                        self.bubble = Bubble(1,20)
                        self.bubble.calculate_radius()

                        self.all_bubbles.append(self.bubble)

        def run(self):


                while True:
                    # --- Main event loop

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit() # Close the window and quit.
                                        sys.exit()

                        # --- Game logic should go here
                        for bubble in self.all_bubbles:

                                bubble.rising()

                        self.draw()

                        # --- Limit to 60 frames per second
                        self.clock.tick(120)


        def draw(self):

                # If you want a background image, replace this clear with blit'ing the background image    .
                self.screen.blit(self.background_image,[0,0])

                for bubble in self.all_bubbles:

                        pygame.draw.circle(self.screen, Screensaver.WHITE, [bubble.x,bubble.y],bubble.radius,1)

                # --- Go ahead and update the screen with what we've drawn.
                pygame.display.flip()

##bubble_pop = pygame.mixer.Sound("pop.ogg")

if __name__ =="__main__":
        NewGame = Screensaver(100).run()
