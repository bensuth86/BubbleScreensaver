

import pygame
import random
import sys

class Bubble():

        vy = 1
        expandrate = 5

        def __init__(self):

                self.x = random.randrange(0,Screensaver.screen_width) #random positions along screen width
                self.y = random.randrange(0,Screensaver.screen_height)# ""                                      "" height
                self.radius = 1

        # Define Bubble radius as function of height
        def calculate_radius(self):


                self.radius = (Screensaver.screen_height- self.y) * (Bubble.expandrate/ 100)
                self.radius = int(self.radius)

                #set minimum bubble radius
                if self.radius < 2:
                        self.radius = 1

        def rising(self):

                self.y -= Bubble.vy # Increase bubble height
                self.y = int(self.y) # vy controlled by slider which returns float (no good!)

                self.calculate_radius()

                #Check if above screen
                if self.y < 0:

                        self.x = random.randrange(Screensaver.screen_width) # random position along x
                        self.y = random.randrange(Screensaver.screen_height+5,Screensaver.screen_height+20) # set y position within range from 5-20 below screen edge

                        self.radius = 1   # reset starting radius to 1 if bubble height off screen

        def draw(self,screen):

                pygame.draw.circle(screen, Screensaver.WHITE, [self.x,self.y],self.radius,1)


##                        bubble_pop.play()

class Slider():



        def __init__(self, name, val, maxi, mini, pos):

                self.val = val  # start value
                self.maxi = maxi  # maximum at slider position right
                self.mini = mini  # minimum at slider position left
                self.xpos = pos  # x-location on screen
                self.ypos = 600
                self.surf = pygame.surface.Surface((100, 50))
                self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

                self.font = pygame.font.SysFont("Verdana", 12) # Font for slider icons

                self.txt_surf = self.font.render(name, 1, Screensaver.BLACK)
                self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

                # Static graphics - slider background #
                self.surf.fill((100, 100, 100))
                pygame.draw.rect(self.surf, Screensaver.GREY, [0, 0, 100, 50], 3)
                pygame.draw.rect(self.surf, Screensaver.ORANGE, [10, 10, 80, 10], 0)
                pygame.draw.rect(self.surf, Screensaver.WHITE, [10, 30, 80, 5], 0)

                self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

                # dynamic graphics - button surface #
                self.button_surf = pygame.surface.Surface((20, 20))
                self.button_surf.fill(Screensaver.TRANS)
                self.button_surf.set_colorkey(Screensaver.TRANS)
                pygame.draw.circle(self.button_surf, Screensaver.BLACK, (10, 10), 6, 0)
                pygame.draw.circle(self.button_surf, Screensaver.ORANGE, (10, 10), 4, 0)

        def draw(self,screen):

                """ Combination of static and dynamic graphics in a copy of
                the basic slide surface
                """
                # static
                surf = self.surf.copy()

                # dynamic
                pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
                self.button_rect = self.button_surf.get_rect(center=pos)
                surf.blit(self.button_surf, self.button_rect)
                self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

                # screen
                screen.blit(surf, (self.xpos, self.ypos))

        def move(self,event):
                """
                The dynamic part; reacts to movement of the slider button.
                """
##                self.val = 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()

                        if self.button_rect.collidepoint(pos):
                                self.hit = True

                elif event.type == pygame.MOUSEBUTTONUP:
                        self.hit = False

                if self.hit:

                        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini

                        if self.val < self.mini:
                                self.val = self.mini

                        if self.val > self.maxi:
                                self.val = self.maxi

                return self.val


class Screensaver():


        # Define some colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        GREY = (200, 200, 200)
        ORANGE = (200, 100, 50)
        TRANS = (1, 1, 1)

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

                # Create initial bubbles
                self.all_bubbles += self.createbubbles(self.total)
##                print(len(self.all_bubbles))

                # Create Sliders
                self.vy_slider = Slider("Speed", 1, 6, 1, 200) # bubble speed slider
                self.expand_slider = Slider("ExpandRate", 5, 20, 5, 400) # bubble expansion slider
                self.nosbubbles_slider = Slider("NosBubbles", 0, 500, 0, 600) # add new bubbles slider


        def createbubbles(self,nos):

                newbubbles = []

                for i in range(nos): # create n bubbles

                        self.bubble = Bubble()
                        self.bubble.calculate_radius()

                        newbubbles.append(self.bubble)
##                        print(len(newbubbles))

                return newbubbles


        def run(self):

                c = 0

                nosbub_previous = 0
                print("A",len(self.all_bubbles))

                while True:
                    # --- Main event loop
                        c += 1
                        for event in pygame.event.get():

                                if event.type == pygame.QUIT:
                                        pygame.quit() # Close the window and quit.
                                        sys.exit()

                                Bubble.vy = self.vy_slider.move(event) # return new vy value from speed slider
                                Bubble.expandrate = self.expand_slider.move(event) # return new expandrate value from speed slider

                                nosbub = self.nosbubbles_slider.move(event) # nos of new bubbles to add
                                nosbub = int(nosbub)
##                                print("NosBub:", nosbub)


##                        if nosbub > nosbub_previous:

                        while len(self.all_bubbles) < self.total + nosbub:

##                                print("NosBub:", nosbub)
##                                print("HH",self.total + nosbub)

                                self.all_bubbles += self.createbubbles(1)

##                                print("B",len(self.all_bubbles))
##                                print("NosBub:", nosbub)
##                                print()


                        if nosbub < nosbub_previous:

                                while len(self.all_bubbles) > self.total + nosbub:

                                        del self.all_bubbles[-1]
        ##                                print("C",len(self.all_bubbles))

                       # --- Game logic should go here
##                        print(nosbub_previous)
                        nosbub_previous = nosbub # compare nos of bubbles to previous loop

##                        print(nosbub_previous)
                        for bubble in self.all_bubbles:

                                bubble.rising()

                        self.draw()

                        # --- Limit to 60 frames per second
                        self.clock.tick(120)
##                        break


        def draw(self):

                # If you want a background image, replace this clear with blit'ing the background image    .
                self.screen.blit(self.background_image,[0,0])

                # Draw sliders
                self.vy_slider.draw(self.screen)
                self.expand_slider.draw(self.screen)
                self.nosbubbles_slider.draw(self.screen)

                for bubble in self.all_bubbles:

                        bubble.draw(self.screen)

                # --- Go ahead and update the screen with what we've drawn.
                pygame.display.flip()

##bubble_pop = pygame.mixer.Sound("pop.ogg")


if __name__ =="__main__":
        NewGame = Screensaver(10).run()
