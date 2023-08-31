import pygame
import random

mapSize = 400
chunkSize = 10
delta = 0.3333333
clock = pygame.time.Clock()


class chunk:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y


class SnakeGame:
    head = None
    lasthead = None
    food = None
    tail = None
    vel = None

    def __init__(self):
        head = chunk(0, 0)

        print(type(head))

        lasthead = chunk(0, 0)
        food = chunk(random.randint(0, int(mapSize / chunkSize)-1), random.randint(0, int(mapSize / chunkSize)-1))
        tail = [chunk(0, 0), chunk(0, 0), chunk(0, 0)]
        vel = [0, 1]
    
    def getEvent(self, event):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if vel[1] == 0:
                vel[1] = -1
                vel[0] = 0
        elif pressed[pygame.K_DOWN]:
            if vel[1] == 0:
                vel[1] = 1
                vel[0] = 0
        elif pressed[pygame.K_RIGHT]:
            if vel[0] == 0:
                vel[0] = 1
                vel[1] = 0
        elif pressed[pygame.K_LEFT]:
            if vel[0] == 0:
                vel[0] = -1
                vel[1] = 0

    def update(self):
        lasthead = chunk(head.x, head.y)
        head.x += vel[0]
        head.x = head.x % (400 / chunkSize)
        head.y += vel[1]
        head.y = head.y % (400 / chunkSize)

        tail[len(tail) - 1].x = lasthead.x
        tail[len(tail) - 1].y = lasthead.y

        tmp = tail[len(tail) - 1]
        tail.remove(tmp)
        tail.insert(0, tmp)

        if head.x == food.x and head.y == food.y:
            food = chunk(random.randint(0, int(mapSize / chunkSize)-1), random.randint(0, int(mapSize / chunkSize)-1))
            tail.append(chunk(-1,-1))
    
        for i in tail:
            if head.x == i.x and head.y == i.y:
                #Set GameOver
                break

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 150, 10),
            pygame.Rect(head.x * chunkSize, head.y * chunkSize, chunkSize, chunkSize),
        )
        for i in tail:
            pygame.draw.rect(
                screen,
                (150, 255, 76),
                pygame.Rect(i.x * chunkSize, i.y * chunkSize, chunkSize, chunkSize),
            )
        pygame.draw.rect(
            screen,
            (50, 255, 150),
            pygame.Rect(food.x * chunkSize, food.y * chunkSize, chunkSize, chunkSize),
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

