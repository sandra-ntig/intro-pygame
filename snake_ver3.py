# Import the pygame module
import pygame

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
        super(Snake, self).__init__()
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 'stop'
        self.body = []

    def draw_snake(self, surface):
        self.segments = []
        self.head = pygame.Surface((10, 10))
        self.head.fill((34, 139, 34))
        self.rect = self.head.get_rect(
            center=(self.x, self.y))
        if len(self.body) > 0:
            for unit in self.body:
                segment = pygame.Surface((10, 10))
                segment.fill((34, 139, 34))
                rect = self.segment.get_rect(
                center=(self.x, self.y))
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)
                self.segments.append(segment)


# Define the Apple object extending pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'Apple'
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super(Apple, self).__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((34, 139, 34))
        self.rect = self.surf.get_rect(
            center=(random.randint(1, SCREEN_WIDTH), random.randint(1, SCREEN_HEIGHT)))


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

# Create our 'player'
snake = Snake()

# Create groups to hold Apple sprites, and every sprite
# - apples is used for collision detection and position updates
# - all_sprites is used for rendering
apples = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)

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
         # Spawn new apples, and add it to our sprite groups
        elif event.type == SPAWNAPPLE:
            apple = Apple()
            print(apple)
            apples.add(apple)
            all_sprites.add(apple)

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

     # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    snake.update(pressed_keys)

         # Move the sprite based on keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

   

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all our sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(snake, apples):
        # If so, remove the player and stop the loop
        snake.kill()
        running = False

    # Flip everything to the display
    pygame.display.flip()
