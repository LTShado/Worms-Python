import pygame
import time
import math

res = (640,480)

pygame.init()

pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res, pygame.RESIZABLE)
print(pygame.display.Info())

ciel = (30,144,255)
surface.fill(ciel)

bullet_color = (109,7,26)
bullet = [300,400]
pygame.draw.circle(surface,bullet_color,bullet,10)

pygame.display.flip()

i= bullet[1]
t=0
x0 = bullet[0]
y0 = bullet[1]

while i<460:
    time.sleep(.05)

    t += 0.5
    angle = 30
    v0 = 75*math.cos(angle)
    w0 = 75*math.sin(angle)


    g = 9.81
    bullet[0] = x0 + v0*t
    bullet[1] = 0.5*g*(t**2)+w0*t+y0

    pygame.draw.circle(surface, bullet_color, bullet, 10)
    pygame.display.flip()

    i = 0.5*g*(t**2)+w0*t+y0

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            print("exit")
