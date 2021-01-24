import pygame

res = (640,480)

pygame.init()

pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res, pygame.RESIZABLE)
print(pygame.display.Info())

ciel = (30,144,255)
surface.fill(ciel)

pygame.display.flip()

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            print("exit")

        if event.type == pygame.K_F11:
            print("test")
