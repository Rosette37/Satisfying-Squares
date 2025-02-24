import pygame
from random import *

class Critter:
    pos = pygame.math.Vector2()
    target = pygame.math.Vector2()
    following_target = False
    speed = 0 #distance moved in a second
    distance = 0 #distance that the critter can move
    leisure = 0 #secs between moving
    leisure_counter = 0 #ticks of leisure so far
    color = (0, 0, 0)
    size = 0
    screen_size = (0, 0)
    screen_rect = pygame.Rect()

    def __init__(self, screen:tuple):
        self.target = pygame.math.Vector2()
        self.pos = pygame.math.Vector2()
        self.following_target = False
        self.pos.x = screen[0] / 2
        self.pos.y = screen[1] / 2
        self.speed = randint(75, 150)
        self.distance = 100 + 100 * random()
        self.leisure = .75 + .75 * random()
        self.leisure_counter = 0
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.size = randint(8, 18)
        self.screen_size = screen
        self.screen_rect = pygame.Rect((0, 0), self.screen_size)

    def update(self):
        if self.following_target == False:
            self.leisure_counter += 1
            if self.leisure_counter >= self.leisure * 60:
                while True: #emulating do-while loop
                    self.target.update(self.pos)
                    self.target.x += (self.distance - self.distance /2 * random()) * choice((-1, 1))
                    self.target.y += (self.distance - self.distance /2 * random()) * choice((-1, 1))
                    self.following_target = True
                    if(self.screen_rect.collidepoint(self.target)): #breaking only when the target position is within the screen
                        break
        else:
            self.pos.move_towards_ip(self.target, self.speed / 60)
            if self.pos.distance_to(self.target) == 0:
                self.following_target = False
                self.leisure_counter = 0
    
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.pos, (self.size, self.size))

    def get_color(self) -> tuple:
        return self.color