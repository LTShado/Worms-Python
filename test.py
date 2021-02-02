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

ground = list()
ground_color = (155,118,53)
colide = pygame.Rect(0,440,300,40)
pygame.draw.rect(surface,ground_color,colide)
ground.append(colide)
colide = pygame.Rect(301,440,640,40)
pygame.draw.rect(surface,ground_color,colide)
ground.append(colide)
colision = dict()

g = 9.81

colision["ground"] = ground

playerOne = Pwayer.Player(60, 60, 20, surface, ground)


def keyDownAction():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerOne.MovePlayer("Left")
    if keys[pygame.K_RIGHT]:
        playerOne.MovePlayer("Right")
    if keys[pygame.K_SPACE] and playerOne.isGrounded():
        playerOne.Jump()


ciel = (30, 144, 255)
launched = True

while launched:

    clock.tick(60)
    surface.fill(ciel)

    for collide in ground:
        pygame.draw.rect(surface, ground_color, collide)

    playerOne.fall(g)

    playerOne.draw()
    pygame.display.flip()

    keyDownAction()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            print("exit")
