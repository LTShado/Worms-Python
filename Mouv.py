import pygame
import time
import math

res = (640,480)

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Worms")
surface = pygame.display.set_mode(res, pygame.RESIZABLE)
print(pygame.display.Info())

sound = pygame.mixer.Sound("musique/wormstheme.mp3")
sound.set_volume(0.30)
rocket = pygame.mixer.Sound("musique/rocketlauncher.mp3")
grenade = pygame.mixer.Sound("musique/grenade.mp3")
explosion = pygame.mixer.Sound("musique/explosion.mp3")
#sound.play()

bullet_color = (109,7,26)

arial_font = pygame.font.SysFont("arial",50)
arial_font_fps = pygame.font.SysFont("arial",10)
test_text = arial_font.render("WORMS",True,bullet_color)

ciel = (30,144,255)
surface.fill(ciel)

pnj_color = (26,7,109)
pnj = pygame.Rect(300,200,20,20)
pygame.draw.rect(surface,pnj_color,pnj)

bullet = pygame.Rect(pnj.x,pnj.y,20,20)
pygame.draw.rect(surface, bullet_color, bullet)

ground_color = (155,118,53)
ground = pygame.Rect(0,440,640,40)
pygame.draw.rect(surface,ground_color,ground)

text_x = 250
text_y = 20

surface.blit(test_text, [text_x,text_y])
pygame.display.flip()

AB = 0
AC = 0
angle_radian = 0
angle_degree = 0
vitesse = 0
x_souris = 0
y_souris = 0

launched = True
while launched:
    clock.tick(60)
    surface.fill(ciel)
    if bullet.y >= 420:
        bullet.y = 420

    text_fps = arial_font_fps.render(f"{clock.get_fps():.2f} FPS", True, pnj_color)
    angle_number = arial_font_fps.render(f"{angle_degree} °", True, pnj_color)
    AB_number = arial_font_fps.render(f"AB = {AB}", True, bullet_color)
    AC_number = arial_font_fps.render(f"AC = {AC}", True, bullet_color)
    vitesse_number = arial_font_fps.render(f"vitesse = {vitesse}", True, pnj_color)

    surface.blit(text_fps, [10, 10])
    surface.blit(angle_number, [500, 10])
    surface.blit(AB_number, [500, 20])
    surface.blit(AC_number, [500, 30])
    surface.blit(vitesse_number, [500, 40])

    pygame.draw.rect(surface, pnj_color, pnj)
    pygame.draw.rect(surface, ground_color, ground)
    pygame.draw.line(surface, bullet_color, [pnj.centerx, pnj.centery], [x_souris, y_souris])

    AB = math.sqrt(((x_souris - (pnj.centerx)) ** 2) + ((y_souris - (pnj.centery)) ** 2))
    AC = x_souris - (pnj.centerx)

    if round(AB / 2, 0) > 100:
        vitesse = 100

    else:
        vitesse = round(AB / 2, 0)

    if AB == 0:
        AB == 1
    else:
        angle_radian = round(math.acos(AC / AB), 4)
        if y_souris > pnj.y:
            angle_degree = round(360 - (angle_radian * 180 / math.pi), 0)
        else:
            angle_degree = round(angle_radian * 180 / math.pi, 0)

    surface.blit(test_text, [text_x, text_y])
    pygame.display.flip()


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

                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_DOWN:
                print("bas")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.y += 10

                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_LEFT:
                print("gauche")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.x -= 10

                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_RIGHT:
                print("droite")

                time.sleep(.05)
                surface.fill(ciel)
                pnj.x += 10

                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

            elif event.key == pygame.K_a:
                #grenade.play()

                bullet.x=pnj.x
                bullet.y=pnj.y
                t = 0
                x0 = pnj.x
                y0 = pnj.y

                while not ground.colliderect(bullet) and bullet.x<1260 and bullet.y<940:
                    time.sleep(.05)
                    surface.fill(ciel)

                    t += 0.5
                    if(y_souris>pnj.y):
                        angle = angle_radian
                    else:
                        angle = -angle_radian

                    v0 = vitesse * math.cos(angle)
                    w0 = vitesse * math.sin(angle)

                    g = 9.81
                    bullet[0] = x0 + v0 * t
                    bullet[1] = 0.5 * g * (t ** 2) + w0 * t + y0

                    pygame.draw.rect(surface, bullet_color, bullet)
                    pygame.draw.rect(surface, pnj_color, pnj)
                    pygame.draw.rect(surface, ground_color, ground)

                    pygame.draw.line(surface, bullet_color, [pnj.centerx, pnj.centery], [x_souris, y_souris])

                    surface.blit(test_text, [text_x, text_y])
                    pygame.display.flip()

                    i = 0.5 * g * (t ** 2) + w0 * t + y0

                explosion.play()

            elif event.key == pygame.K_SPACE:

                jump = 0

                for jump_h in range(10):
                    time.sleep(.05)
                    surface.fill(ciel)

                    pnj.y -= jump_h

                    pygame.draw.rect(surface, pnj_color, pnj)
                    pygame.draw.rect(surface, ground_color, ground)

                    pygame.draw.line(surface, bullet_color, [bullet[0], bullet[1]], [pnj.x, pnj.y])

                    surface.blit(test_text, [text_x, text_y])
                    pygame.display.flip()

                for jump_d in range(10):
                    time.sleep(.05)
                    surface.fill(ciel)

                    pnj.y += jump_d

                    pygame.draw.rect(surface, pnj_color, pnj)
                    pygame.draw.rect(surface, ground_color, ground)

                    pygame.draw.line(surface, bullet_color, [bullet[0], bullet[1]], [pnj.x, pnj.y])

                    surface.blit(test_text, [text_x, text_y])
                    pygame.display.flip()


            else:
                print("Autre key")

        elif event.type == pygame.MOUSEMOTION:
            #print("{}".format(event.pos))

            surface.fill(ciel)
            x_souris = event.pos[0]
            y_souris = event.pos[1]

            pygame.draw.rect(surface, pnj_color, pnj)
            pygame.draw.rect(surface, ground_color, ground)

            pygame.draw.line(surface, bullet_color, [pnj.centerx, pnj.centery], [event.pos[0],event.pos[1]])

            surface.blit(test_text, [text_x, text_y])



            surface.blit(AB_number, [500, 20])
            surface.blit(AC_number, [500, 30])
            surface.blit(vitesse_number, [500, 40])



            surface.blit(angle_number, [500, 10])

            clock.tick(60)
            surface.blit(text_fps, [10, 10])

            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("{}".format(event.pos))

            #rocket.play()

            time.sleep(.005)
            surface.fill(ciel)
            text_x = event.pos[0]
            text_y = event.pos[1]

            pygame.draw.rect(surface, pnj_color, pnj)
            pygame.draw.rect(surface, ground_color, ground)

            surface.blit(test_text, [text_x, text_y])

            clock.tick(60)
            surface.blit(text_fps, [10, 10])
            pygame.display.flip()
