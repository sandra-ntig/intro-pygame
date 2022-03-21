# Import the pygame module
import pygame

# https://www.mrmichaelsclass.com/python-programming/python-projects/pygame-snake

# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.score = 0
        self.highScore = 0
        self.speed = 10
        self.dx = 0
        self.dy = 0


# Define the Player object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
""" class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(255, 255, 255)
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)) """


# Define the Apple object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'Apple'
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()

    def move(self):
        food.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        food.rect.y = random(50, SCREEN_HEIGHT - 50)


# Where to draw objects
snake = Snake()
snake.rect.x = SCREEN_WIDTH // 2
snake.rect.y = SCREEN_HEIGHT // 2

food = Food()
food.rect.x = random.randint(50, SCREEN_WIDTH - 50)
food.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

# Sprite groups
sprites_group = pygame.sprite.Group()
sprites_group.add(snake)
sprites_group.add(food)

# Initialize pygame
pygame.init()

# Start clock
clock = pygame.time.Clock()

FPS = 60  # 60 frames per second

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

delay = 1000  # 1 second
SPAWNAPPLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNAPPLE, delay)


# Variable to keep our main loop running
running = True

# Our main loop
while running:

    clock.tick(FPS)
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Move the sprite based on keypresses

    print(snake)

    snake.rect.x += snake.dx
    snake.rect.y += snake.dy

    if pressed_keys[K_UP]:
        snake.dx = 0
        snake.dy = -snake.speed
    if pressed_keys[K_DOWN]:
        snake.dx = 0
        snake.dy = snake.speed
    if pressed_keys[K_LEFT]:
        snake.dx = -snake.speed
        snake.dy = 0
    if pressed_keys[K_RIGHT]:
        snake.dx = snake.speed
        snake.dy = 0
"""
    # Keep player on the screen
    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    elif self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
 """

# Fill the screen with black
screen.fill((0, 0, 0))

""" # Draw all our sprites
for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

# Check if any enemies have collided with the player
if pygame.sprite.spritecollideany(player, apples):
    # If so, remove the player and stop the loop
    player.kill()
    running = False """

# Flip everything to the display
pygame.display.flip()
