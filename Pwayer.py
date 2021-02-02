import pygame
import time
import math

class Player :
    def __init__(self, _x, _y, _size, _window):
        self.body = pygame.Rect(_x, _y, _size, _size)
        self.color = (26, 7, 109)
        self.__speed = 1
        self.window = _window

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.body)

    def MovePlayer(self, Direction):
        if Direction == "Left":
            self.body = self.body.move(-self.__speed, 0)
        elif Direction == "Right":
            self.body = self.body.move(self.__speed, 0)



