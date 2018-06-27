import pygame

# initizalize pygame:
pygame.init()

# set the width and height of the game window:
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# set the caption which is displayed above
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

# colors definition :
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# load the car image 
carImg = pygame.image.load('car.png')


# display the car image function

def draw_car(x, y):
    # blit is for drawing stuff to the background
    gameDisplay.blit(carImg, (x, y))

x = (display_width * 0.40)
y = (display_height * 0.7)


crashed = False

# the game loop
while not crashed:
    # pygame get each event that happens
    for event in pygame.event.get():
        print(event)
        # set crashed to false if user wants to quit the game
        if event.type == pygame.QUIT :
            crashed = True
    #change the background color
    gameDisplay.fill(white)
    draw_car(x, y)
    # update the front surface
    pygame.display.update()
    clock.tick(60)

# the end of the game
pygame.quit()
quit()
