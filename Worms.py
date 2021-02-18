import pygame
import Pwayer
import time
import math

#test 2

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

arial_font_fps = pygame.font.SysFont("arial",10)
fps_color = (26,7,109)
traj_color = (109,7,26)
bullet_color = (109,7,26)

g = 9.81
AB = 0
AC = 0
angle_radian = 0
angle_degree = 0
vitesse = 0
x_souris = 0
y_souris = 0

weapon = 0
debug_mode = 0
wind_speed = 10

colision["ground"] = ground

playerOne = Pwayer.Player(60, 60, 20, surface, ground)
bullet = pygame.Rect(playerOne.body.x,playerOne.body.y,20,19.5)
traj_bullet = pygame.Rect(playerOne.body.x,playerOne.body.y,10,10)
traj_status = 0


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


    text_fps = arial_font_fps.render(f"{clock.get_fps():.2f} FPS", True, fps_color)
    angle_number = arial_font_fps.render(f"{angle_degree} °", True, fps_color)
    AB_number = arial_font_fps.render(f"AB = {AB}", True, traj_color)
    AC_number = arial_font_fps.render(f"AC = {AC}", True, traj_color)
    vitesse_number = arial_font_fps.render(f"vitesse = {vitesse}", True, traj_color)

    if weapon==0:
        weapon_name="grenade"
    elif weapon==1:
        weapon_name="rocket"

    weapon_render = arial_font_fps.render(f"Weapon : {weapon_name}", True,traj_color)
    wind_render = arial_font_fps.render(f"Wind speed : {wind_speed}", True,traj_color)

    AB = math.sqrt(((x_souris - (playerOne.body.centerx)) ** 2) + ((y_souris - (playerOne.body.centery)) ** 2))
    AC = x_souris - (playerOne.body.centerx)

    if round(AB / 2, 0) > 100:
        vitesse = 100

    else:
        vitesse = round(AB / 2, 0)

    if AB == 0:
        AB == 1
    else:
        angle_radian = round(math.acos(AC / AB), 4)
        if y_souris > playerOne.body.y:
            angle_degree = round(360 - (angle_radian * 180 / math.pi), 0)
        else:
            angle_degree = round(angle_radian * 180 / math.pi, 0)

    if debug_mode == 1:
        surface.blit(text_fps, [10, 10])
        surface.blit(angle_number, [500, 10])
        surface.blit(AB_number, [500, 20])
        surface.blit(AC_number, [500, 30])
        surface.blit(vitesse_number, [500, 40])
        surface.blit(weapon_render, [500, 50])
        surface.blit(wind_render, [500, 60])

    x0 = playerOne.body.centerx
    y0 = playerOne.body.centery

    if (y_souris > playerOne.body.y):
        angle = angle_radian
    else:
        angle = -angle_radian

    v0 = vitesse * math.cos(angle)
    w0 = vitesse * math.sin(angle)

    for i in range(0, 20):
        traj_bullet_x = x0 + v0 * (i * 0.5)
        traj_bullet_y = 0.5 * g * ((i * 0.5) ** 2) + w0 * (i * 0.5) + y0

        if traj_status == 1:
            pygame.draw.circle(surface, traj_color, [traj_bullet_x,traj_bullet_y],3)

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if traj_status == 0:
                    traj_status = 1
                elif traj_status == 1:
                    traj_status = 0

            elif event.key == pygame.K_TAB:
                if weapon==0:
                    weapon=1
                elif weapon==1:
                    weapon=0

            elif event.key == pygame.K_F3:
                if debug_mode==0:
                    debug_mode=1
                elif debug_mode==1:
                    debug_mode=0

        elif event.type == pygame.MOUSEMOTION:
            #print("{}".format(event.pos))

            surface.fill(ciel)
            x_souris = event.pos[0]
            y_souris = event.pos[1]

            playerOne.draw()
            pygame.draw.rect(surface, ground_color, collide)

            if debug_mode == 1:
                surface.blit(text_fps, [10, 10])
                surface.blit(AB_number, [500, 20])
                surface.blit(AC_number, [500, 30])
                surface.blit(vitesse_number, [500, 40])
                surface.blit(angle_number, [500, 10])
                surface.blit(weapon_render, [500, 50])
                surface.blit(wind_render, [500, 60])

            x0 = playerOne.body.centerx
            y0 = playerOne.body.centery

            if (y_souris > playerOne.body.y):
                angle = angle_radian
            else:
                angle = -angle_radian

            v0 = vitesse * math.cos(angle)
            w0 = vitesse * math.sin(angle)

            for i in range(0, 20):
                traj_bullet_x = x0 + v0 * (i*0.5)
                traj_bullet_y = 0.5 * g * ((i*0.5) ** 2) + w0 * (i*0.5) + y0

                if traj_status == 1:
                    pygame.draw.circle(surface, traj_color, [traj_bullet_x,traj_bullet_y],3)

            clock.tick(60)
            #surface.blit(text_fps, [10, 10])

            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # grenade.play()

            bullet.x = playerOne.body.x
            bullet.y = playerOne.body.y
            t = 0
            x0 = playerOne.body.x
            y0 = playerOne.body.y

            while not colide.colliderect(bullet) and bullet.x < 1260 and bullet.y < 940:
                time.sleep(.05)
                surface.fill(ciel)

                t += 0.5
                if (y_souris > playerOne.body.y):
                    angle = angle_radian
                else:
                    angle = -angle_radian

                v0 = vitesse * math.cos(angle)
                w0 = vitesse * math.sin(angle)

                if weapon == 0:
                    bullet[0] = x0 + v0 * t
                    bullet[1] = 0.5 * g * (t ** 2) + w0 * t + y0

                elif weapon == 1:
                    bullet[0] = x0 + ((v0*wind_speed) * (1))
                    bullet[1] = y0 + (((w0/wind_speed) + (g/wind_speed**2)) * (1)) - ((g*t)/wind_speed)

                pygame.draw.rect(surface, bullet_color, bullet)
                playerOne.draw()
                pygame.draw.rect(surface, ground_color, collide)

                pygame.display.flip()

                i = 0.5 * g * (t ** 2) + w0 * t + y0