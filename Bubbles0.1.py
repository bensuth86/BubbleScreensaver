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


# Define Bubble radius as function of height

def radius(h):

        r = (screen_height-h)/20
        r = int(round(r))
        if r < 2:
                r=2

        return r


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)



pygame.init()


# Set the width and height of the screen [width, height]
screen_width = 1400
screen_height= 700
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size) # set screensize
 
pygame.display.set_caption("Bubbles")
 
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

star_list=[] # Bubbles stored as coordinate set [x, height] within list

##sys.exit()

# Assign bubble start co-ords
for i in range(20): # create 20 bubbles
        x = random.randrange(0,screen_width) #random positions along screen width
        y = random.randrange(0,screen_height)# ""                                      "" height
        star_list.append([x,y])

background_image = pygame.image.load("deep_sea.jpg").convert()
bubble_pop = pygame.mixer.Sound("pop.ogg")

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the background image    .
    screen.blit(background_image,[0,0])
         
    for item in star_list:
            
        item[1] -= 2 # Increase bubble height 
        
        if item[1] in range(0,screen_height):
                r = radius(item[1]) # function for increasing bubble size (radius), as function of height
        else:

                r = 2 # reset starting radius to 2 if bubble height off screen

        # --- Drawing code should go here
        pygame.draw.circle(screen, WHITE, item,r,1)
                
        
    

        if item[1] <= 0:
            item[1] = random.randrange(screen_height+5,screen_height+20)
            item[0] = random.randrange(screen_width)
            bubble_pop.play()
                 
    
    
##    pygame.draw.circle(screen, WHITE, item,r,1)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
