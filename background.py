# # 

# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('F1 Bahrain GP Track')

# # Define colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Function to draw the Bahrain GP track
# def draw_bahrain_track(surface):
#     # Draw a simplified outline of the track
#     # You can adjust the coordinates to get a more accurate representation
#     pygame.draw.lines(surface, black, False, [
#         (100, 400), (150, 350), (200, 350), (250, 400), 
#         (300, 420), (350, 400), (400, 450), (450, 420), 
#         (500, 400), (550, 450), (600, 400), (650, 350), 
#         (700, 350), (750, 400), (700, 450), (650, 480),
#         (600, 500), (550, 480), (500, 500), (450, 480),
#         (400, 500), (350, 480), (300, 500), (250, 480),
#         (200, 500), (150, 480), (100, 450), (50, 400)
#     ], 5)

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the screen with white
#     screen.fill(white)

#     # Draw the track
#     draw_bahrain_track(screen)

#     # Update the display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()



# Initialize pygame and set the colors with captions 
import pygame
import sys
pygame.init() 
  
# Define color codes 
gray = (119, 118, 110) 
black = (0, 0, 0) 
red = (255, 0, 0) 
green = (0, 200, 0) 
blue = (0, 0, 200) 
bright_red = (255, 0, 0) 
bright_green = (0, 255, 0) 
bright_blue = (0, 0, 255) 
  
# Define display dimensions 
display_width = 800
display_height = 600
  
# Set up game display 
gamedisplays = pygame.display.set_mode((display_width,  
                                        display_height)) 
pygame.display.set_caption("car game") 
clock = pygame.time.Clock() 
  
# Load car image and background images 
carimg = pygame.image.load('car1.jpg') 
backgroundpic = pygame.image.load("download12.jpg") 
yellow_strip = pygame.image.load("yellow strip.jpg") 
strip = pygame.image.load("strip.jpg") 
intro_background = pygame.image.load("background.jpg") 
instruction_background = pygame.image.load("background2.jpg") 
  
# Set car width and initialize pause state 
car_width = 56
pause = False