import pygame
import time
# initizalize pygame:
pygame.init()

# set the width and height of the game window:
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
car_width = 150

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

def text_objects(message, font, color):
    textSurf = font.render(message, True, color)
    return textSurf, textSurf.get_rect()

def message_display(message):
    text = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(message, text, red)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    # update the front surface
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('you crashed')

def game_loop():
    x = (display_width * 0.40)
    y = (display_height * 0.7)
    x_change = 0
    y_change = 0
    gameExit = False

    # the game loop
    while not gameExit:
        # pygame get each event that happens
        for event in pygame.event.get():
            print(event)
            # set crashed to false if user wants to quit the game
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        #change the background color
        gameDisplay.fill(white)
        draw_car(x, y)

        if x > display_width - car_width or x < 0:
            crash()

        # update the front surface
        pygame.display.update()
        clock.tick(60)


game_loop()

# the end of the game
pygame.quit()
quit()
