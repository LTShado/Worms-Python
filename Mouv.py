import pygame
import time
import math

res = (640,480)

pygame.init()

pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res, pygame.RESIZABLE)
print(pygame.display.Info())

bullet_color = (109,7,26)

arial_font = pygame.font.SysFont("arial",50)
test_text = arial_font.render("WORMS",True,bullet_color)


ciel = (30,144,255)
surface.fill(ciel)


bullet = [300,300]
pygame.draw.circle(surface,bullet_color,bullet,10)

pnj_color = (26,7,109)
pnj = pygame.Rect(300,100,20,20)
pygame.draw.rect(surface,pnj_color,pnj)

ground_color = (155,118,53)
ground = pygame.Rect(0,440,640,40)
pygame.draw.rect(surface,ground_color,ground)

text_x = 250
text_y = 20

surface.blit(test_text, [text_x,text_y])
pygame.display.flip()



launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            print("exit")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("haut")
                time.sleep(.05)
                surface.fill(ciel)
                pnj.y -= 10

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                print("bas")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.y += 10

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_LEFT:
                print("gauche")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.x -= 10

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_RIGHT:
                print("droite")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.x += 10

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_a:
                i = bullet[1]
                t = 0
                x0 = bullet[0]
                y0 = bullet[1]

                while i < 460:
                    time.sleep(.05)
                    surface.fill(ciel)

                    t += 0.5
                    angle = 30
                    v0 = 75 * math.cos(angle)
                    w0 = 75 * math.sin(angle)

                    g = 9.81
                    bullet[0] = x0 + v0 * t
                    bullet[1] = 0.5 * g * (t ** 2) + w0 * t + y0

                    pygame.draw.circle(surface, bullet_color, bullet, 10)
                    pygame.draw.rect(surface, pnj_color, pnj)
                    pygame.draw.rect(surface, ground_color, ground)

                    surface.blit(test_text, [text_x, text_y])
                    pygame.display.flip()

                    i = 0.5 * g * (t ** 2) + w0 * t + y0

            elif event.key == pygame.K_r:
                print("reset")
                time.sleep(.05)
                surface.fill(ciel)

                bullet[0]=x0
                bullet[1]=y0

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            else:
                print("Autre key")

        elif event.type == pygame.MOUSEMOTION:
            print("{}".format(event.pos))

            time.sleep(.005)
            surface.fill(ciel)
            pnj.x = event.pos[0]
            pnj.y = event.pos[1]

            pygame.draw.circle(surface, bullet_color, bullet, 10)
            pygame.draw.rect(surface, pnj_color, pnj)
            pygame.draw.rect(surface, ground_color, ground)

            surface.blit(test_text, [text_x, text_y])
            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("{}".format(event.pos))

            time.sleep(.005)
            surface.fill(ciel)
            text_x = event.pos[0]
            text_y = event.pos[1]

            pygame.draw.circle(surface, bullet_color, bullet, 10)
            pygame.draw.rect(surface, pnj_color, pnj)
            pygame.draw.rect(surface, ground_color, ground)

            surface.blit(test_text, [text_x, text_y])
            pygame.display.flip()
