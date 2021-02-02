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
sound.play()

bullet_color = (109,7,26)
bullet = [10,400]
pygame.draw.circle(surface, bullet_color, bullet, 10)

arial_font = pygame.font.SysFont("arial",50)
arial_font_fps = pygame.font.SysFont("arial",10)
test_text = arial_font.render("WORMS",True,bullet_color)

ciel = (30,144,255)
surface.fill(ciel)

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

c = 0
b = 0
angle_radian = 0
launched = True
while launched:
    clock.tick(60)
    surface.fill(ciel)

    text_fps = arial_font_fps.render(f"{clock.get_fps():.2f} FPS", True, pnj_color)
    angle_number = arial_font_fps.render(f"{angle_radian} °", True, pnj_color)
    c_number = arial_font_fps.render(f"c = {c}", True, bullet_color)
    b_number = arial_font_fps.render(f"b = {b}", True, bullet_color)

    surface.blit(text_fps, [10, 10])
    surface.blit(angle_number, [600, 10])
    surface.blit(c_number, [500, 20])
    surface.blit(b_number, [500, 30])

    pygame.draw.circle(surface, bullet_color, bullet, 10)

    pygame.draw.rect(surface, pnj_color, pnj)
    pygame.draw.rect(surface, ground_color, ground)
    pygame.draw.line(surface, bullet_color, [bullet[0], bullet[1]], [pnj.x, pnj.y])
    pygame.draw.circle(surface, bullet_color, [pnj.x, bullet[1]], 10)

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
                grenade.play()

                i = bullet[1]
                t = 0
                x0 = bullet[0]
                y0 = bullet[1]

                if i >= 400:
                    i=0

                while i < 400:
                    time.sleep(.05)
                    surface.fill(ciel)

                    t += 0.5
                    angle = -1.39626
                    v0 = 75 * math.cos(angle)
                    w0 = 75 * math.sin(angle)

                    g = 9.81
                    bullet[0] = x0 + v0 * t
                    bullet[1] = 0.5 * g * (t ** 2) + w0 * t + y0

                    pygame.draw.circle(surface, bullet_color, bullet, 10)
                    pygame.draw.rect(surface, pnj_color, pnj)
                    pygame.draw.rect(surface, ground_color, ground)

                    pygame.draw.line(surface, bullet_color, [bullet[0], bullet[1]], [pnj.x, pnj.y])

                    surface.blit(test_text, [text_x, text_y])
                    pygame.display.flip()

                    i = 0.5 * g * (t ** 2) + w0 * t + y0

            elif event.key == pygame.K_r:
                print("reset")
                explosion.play()

                time.sleep(.05)
                surface.fill(ciel)

                bullet[0]=10
                bullet[1]=400

                pygame.draw.circle(surface, bullet_color, bullet, 10)
                pygame.draw.rect(surface, pnj_color, pnj)
                pygame.draw.rect(surface, ground_color, ground)

                surface.blit(test_text, [text_x, text_y])
                pygame.display.flip()

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
            print("{}".format(event.pos))

            time.sleep(.005)
            surface.fill(ciel)
            pnj.x = event.pos[0]
            pnj.y = event.pos[1]

            pygame.draw.circle(surface, bullet_color, bullet, 10)

            pygame.draw.rect(surface, pnj_color, pnj)
            pygame.draw.rect(surface, ground_color, ground)

            pygame.draw.line(surface, bullet_color, [bullet[0], bullet[1]], [event.pos[0],event.pos[1]])
            pygame.draw.circle(surface, bullet_color, [pnj.x,bullet[1]], 10)

            surface.blit(test_text, [text_x, text_y])

            b= math.sqrt(((pnj.x-bullet[0])**2)+((pnj.y-bullet[1])**2))
            c = event.pos[0]-bullet[0]
            surface.blit(c_number, [500, 20])
            surface.blit(b_number, [500, 30])

            if b==0 and c>0:
                angle_radian = 0
            elif b==0 and c<0:
                angle_radian = 3.14159
            elif c==0 and b>0:
                angle_radian = 1.5708
            elif c==0 and b<0:
                angle_radian = 4.71239
            elif c==0 and b==0:
                continue
            else:
                angle_radian = c/-b

            surface.blit(angle_number, [600, 10])

            clock.tick(60)
            surface.blit(text_fps, [10, 10])

            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("{}".format(event.pos))

            rocket.play()

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
