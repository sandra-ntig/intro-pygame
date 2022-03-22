# The snake object
class Player():
    # Initialization
    def __init__(self):
        self.x = screen_width/2
        self.y = screen_height/2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 'stop'
        self.body = []
        self.head_color = green
        self.body_color = brown
    # Draws the snake on the given surface
    def draw_player(self, surface):
        self.seg = []
        self.head = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)
                self.seg.append(segment)
    # Increases length of snake
    def add_unit(self):
        if len(self.body) != 0:
            index = len(self.body)-1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x,y])
        else:
            self.body.append([1000,1000])
    # Checks if there is any collision
    def is_collision(self):
        # Collision with itself
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
        # Collision with the boundaries
        if self.y < 0 or self.y > screen_height - self.height or self.x < 0 or self.x > screen_width - self.width:
            return True
    # Moves the snake in the direction of head
    def move(self):
        for index in range(len(self.body)-1, 0, -1):
            x = self.body[index-1][0]
            y = self.body[index-1][1]
            self.body[index] = [x,y]
        if len(self.body) > 0:
            self.body[0] = [self.x, self.y]
        if self.direction == 'up':
            self.y -= self.velocity
        if self.direction == 'down':
            self.y += self.velocity
        if self.direction == 'left':
            self.x -= self.velocity
        if self.direction == 'right':
            self.x += self.velocity
    # Changes direction of head
    def change_direction(self, direction):
        if self.direction != 'down' and direction == 'up':
            self.direction = 'up'
        if self.direction != 'right' and direction == 'left':
            self.direction = 'left'
        if self.direction != 'up' and direction == 'down':
            self.direction = 'down'
        if self.direction != 'left' and direction == 'right':
            self.direction = 'right'