import pygame
import Pwayer
import time
import math

res = (640, 480)

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res, pygame.RESIZABLE)
print(pygame.display.Info())

playerOne = Pwayer.Player(60, 60, 20, surface)


def keyDownAction():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerOne.MovePlayer("Left")
    if keys[pygame.K_RIGHT]:
        playerOne.MovePlayer("Right")


ciel = (30, 144, 255)
launched = True

while launched:

    clock.tick(60)
    surface.fill(ciel)

    playerOne.draw()

    pygame.display.flip()

    keyDownAction()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            print("exit")
