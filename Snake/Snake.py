import pygame
import random

mapSize = 400
chunkSize = 10
delta = 0.3333333
clock = pygame.time.Clock()


class Chunk:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y


class SnakeGame:
    def __init__(self):

        self.lasthead = Chunk(0, 0)

        self.head = Chunk(0, 0)

        self.food = Chunk(random.randint(0, int(mapSize / chunkSize)-1), random.randint(0, int(mapSize / chunkSize)-1))

        self.tail = [Chunk(0, 0), Chunk(0, 0), Chunk(0, 0)]

        self.vel = [0, 1]
    
    def getEvent(self, event):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if self.vel[1] == 0:
                self.vel[1] = -1
                self.vel[0] = 0
        elif pressed[pygame.K_DOWN]:
            if self.vel[1] == 0:
                self.vel[1] = 1
                self.vel[0] = 0
        elif pressed[pygame.K_RIGHT]:
            if self.vel[0] == 0:
                self.vel[0] = 1
                self.vel[1] = 0
        elif pressed[pygame.K_LEFT]:
            if self.vel[0] == 0:
                self.vel[0] = -1
                self.vel[1] = 0

    def update(self):
        self.lasthead = Chunk(self.head.x, self.head.y)

        self.head.x += self.vel[0]
        self.head.x = self.head.x % (400 / chunkSize)
        self.head.y += self.vel[1]
        self.head.y = self.head.y % (400 / chunkSize)

        self.tail[len(self.tail) - 1].x = self.lasthead.x
        self.tail[len(self.tail) - 1].y = self.lasthead.y

        tmp = self.tail[len(self.tail) - 1]
        self.tail.remove(tmp)
        self.tail.insert(0, tmp)

        if self.head.x == self.food.x and self.head.y == self.food.y:
            self.food = Chunk(random.randint(0, int(mapSize / chunkSize)-1), random.randint(0, int(mapSize / chunkSize)-1))
            self.tail.append(Chunk(-1,-1))
    
        for i in self.tail:
            if self.head.x == i.x and self.head.y == i.y:
                #Set GameOver
                break

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 150, 10),
            pygame.Rect(self.head.x * chunkSize, self.head.y * chunkSize, chunkSize, chunkSize),
        )
        for i in self.tail:
            pygame.draw.rect(
                screen,
                (150, 255, 76),
                pygame.Rect(i.x * chunkSize, i.y * chunkSize, chunkSize, chunkSize),
            )
        pygame.draw.rect(
            screen,
            (50, 255, 150),
            pygame.Rect(self.food.x * chunkSize, self.food.y * chunkSize, chunkSize, chunkSize),
        )


pygame.init()
screen = pygame.display.set_mode((mapSize, mapSize))
game = SnakeGame()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            game.getEvent(event)

    game.update()

    screen.fill((10, 120, 200))

    game.draw(screen)

    pygame.display.flip()

    delta = clock.tick(20) / 1000

pygame.quit()

